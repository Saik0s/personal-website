#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fal-client",
#   "requests",
#   "pillow",
#   "rich",
# ]
# ///

"""
Professional Header Image Generator for Igor Tarasenko's Blog

This script generates high-quality header images using FAL.ai's FLUX models,
specifically designed for technical blog posts about iOS development and AI.

Features:
- Pre-built professional templates for iOS/AI themes
- Custom prompt support with style enhancement
- Batch generation with variations
- Multiple aspect ratios and resolutions
- Progress tracking and error handling
- Professional styling aligned with website branding

Usage:
    python scripts/generate-header.py "CoreML optimization" --template ios-ai
    python scripts/generate-header.py "Custom prompt" --output ./headers/
    python scripts/generate-header.py --template-list
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime
from math import gcd

import fal_client
import requests
from PIL import Image
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.panel import Panel
from rich.table import Table
from rich.logging import RichHandler

# Initialize rich console
console = Console()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True)]
)
logger = logging.getLogger("header-generator")

# Professional prompt templates aligned with Igor's brand
PROMPT_TEMPLATES = {
    "ios-ai": {
        "name": "iOS + AI Integration",
        "base_prompt": "Professional minimalist illustration of iOS development with AI integration, featuring iPhone silhouette, neural network patterns, and CoreML symbols. Clean geometric design with tech blue and white color scheme. Modern gradient background. High-tech aesthetic.",
        "style_suffix": "Professional corporate design, clean lines, technical illustration style, subtle shadows, premium quality."
    },
    "ios-dev": {
        "name": "iOS Development Focus",
        "base_prompt": "Clean technical illustration of iOS app development, featuring Xcode interface elements, Swift code snippets, iPhone devices, and development tools. Professional blue and white color palette. Minimalist geometric design.",
        "style_suffix": "Corporate tech aesthetic, sharp vector-style graphics, professional presentation."
    },
    "ai-ml": {
        "name": "AI & Machine Learning",
        "base_prompt": "Sophisticated visualization of machine learning concepts with neural networks, data flow diagrams, and AI algorithms. Modern tech aesthetic with blue gradients and geometric patterns. Professional corporate design.",
        "style_suffix": "High-tech corporate style, clean geometric forms, professional color grading."
    },
    "coreml": {
        "name": "CoreML & On-Device AI",
        "base_prompt": "Technical illustration showcasing CoreML framework with iPhone, neural network visualization, and on-device AI processing. Clean Apple-inspired design with system colors and professional typography elements.",
        "style_suffix": "Apple design language inspired, professional tech illustration, clean modern aesthetic."
    },
    "productivity": {
        "name": "Productivity & Automation",
        "base_prompt": "Professional illustration of productivity tools and automation workflows. Clean geometric design featuring connected systems, workflow diagrams, and efficiency symbols. Corporate blue and white color scheme.",
        "style_suffix": "Business professional aesthetic, clean infographic style, corporate presentation quality."
    },
    "swift": {
        "name": "Swift Programming",
        "base_prompt": "Modern illustration of Swift programming language featuring clean code elements, swift bird symbolism, and iOS development tools. Professional orange and blue color palette inspired by Swift branding.",
        "style_suffix": "Programming language branding inspired, professional developer-focused design."
    },
    "mobile-dev": {
        "name": "Mobile Development",
        "base_prompt": "Comprehensive mobile development illustration with multiple device types, responsive design elements, and cross-platform development tools. Clean modern tech aesthetic with professional color grading.",
        "style_suffix": "Multi-platform professional design, corporate tech aesthetic, high-quality illustration."
    },
    "api-integration": {
        "name": "API & Integration",
        "base_prompt": "Technical visualization of API integrations and data flow between systems. Clean geometric design with connection lines, data nodes, and integration symbols. Professional blue and gray color scheme.",
        "style_suffix": "Technical diagram aesthetic, professional corporate design, clean geometric style."
    }
}

# Resolution presets for different use cases
RESOLUTION_PRESETS = {
    "blog-header": (1200, 675),      # 16:9 - Perfect for blog headers
    "social-media": (1200, 630),     # 1.91:1 - Facebook/Twitter optimized
    "hero-banner": (1920, 1080),     # 16:9 - High-res hero sections
    "thumbnail": (800, 450),          # 16:9 - Smaller preview images
    "square": (1080, 1080),          # 1:1 - Instagram square
    "story": (1080, 1920),           # 9:16 - Instagram/TikTok stories
}

class HeaderImageGenerator:
    """Professional header image generator using FAL.ai FLUX models."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("FAL_KEY")
        if not self.api_key:
            raise ValueError("FAL_KEY environment variable not set. Get your API key from https://fal.ai/")
        
        # Configure FAL client
        os.environ["FAL_KEY"] = self.api_key
    
    def enhance_prompt(self, base_prompt: str, template: Optional[str] = None, custom_style: Optional[str] = None) -> str:
        """Enhance a base prompt with professional styling and template-specific elements."""
        
        if template and template in PROMPT_TEMPLATES:
            template_data = PROMPT_TEMPLATES[template]
            enhanced_prompt = f"{template_data['base_prompt']}, {base_prompt}"
            
            # Add template-specific styling
            if template_data.get('style_suffix'):
                enhanced_prompt += f", {template_data['style_suffix']}"
        else:
            enhanced_prompt = base_prompt
        
        # Add custom style if provided
        if custom_style:
            enhanced_prompt += f", {custom_style}"
        
        # Add general professional enhancements for Igor's brand
        professional_suffix = " Professional quality, clean composition, high contrast, suitable for technical blog header, modern tech aesthetic, premium design quality."
        enhanced_prompt += professional_suffix
        
        return enhanced_prompt
    
    def calculate_aspect_ratio(self, width: int, height: int) -> str:
        """Calculate aspect ratio string from dimensions."""
        # Common aspect ratios mapping
        ratio_map = {
            (16, 9): "16:9",
            (4, 3): "4:3",
            (3, 2): "3:2",
            (21, 9): "21:9",
            (1, 1): "1:1",
            (3, 4): "3:4",
            (2, 3): "2:3",
            (9, 16): "9:16",
            (9, 21): "9:21"
        }
        
        # Find GCD to simplify ratio
        ratio_gcd = gcd(width, height)
        simplified_w = width // ratio_gcd
        simplified_h = height // ratio_gcd
        
        return ratio_map.get((simplified_w, simplified_h), f"{simplified_w}:{simplified_h}")
    
    def generate_image(
        self,
        prompt: str,
        output_path: str,
        template: Optional[str] = None,
        resolution: str = "blog-header",
        custom_dimensions: Optional[Tuple[int, int]] = None,
        model: str = "fal-ai/flux-pro/kontext/max/text-to-image",
        guidance_scale: float = 3.5,
        safety_tolerance: str = "2",
        custom_style: Optional[str] = None
    ) -> bool:
        """
        Generate a professional header image.
        
        Args:
            prompt: Base description of the image
            output_path: Where to save the generated image
            template: Template to use for professional styling
            resolution: Resolution preset or 'custom'
            custom_dimensions: Custom (width, height) if resolution is 'custom'
            model: FAL.ai model to use
            guidance_scale: How closely to follow the prompt (1.0-20.0)
            safety_tolerance: Safety filter tolerance (1-6)
            custom_style: Additional style instructions
            
        Returns:
            bool: True if successful, False otherwise
        """
        
        try:
            # Determine dimensions
            if resolution == "custom" and custom_dimensions:
                width, height = custom_dimensions
            elif resolution in RESOLUTION_PRESETS:
                width, height = RESOLUTION_PRESETS[resolution]
            else:
                logger.error(f"Unknown resolution preset: {resolution}")
                return False
            
            aspect_ratio = self.calculate_aspect_ratio(width, height)
            
            # Enhance the prompt
            enhanced_prompt = self.enhance_prompt(prompt, template, custom_style)
            
            logger.info(f"Generating image: {Path(output_path).name}")
            logger.info(f"Resolution: {width}x{height} ({aspect_ratio})")
            logger.info(f"Template: {template or 'None'}")
            
            if logger.level <= logging.DEBUG:
                logger.debug(f"Enhanced prompt: {enhanced_prompt}")
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                console=console,
                transient=True
            ) as progress:
                
                task = progress.add_task("Generating image...", total=100)
                
                def on_queue_update(update):
                    if isinstance(update, fal_client.InProgress):
                        for log in update.logs:
                            progress.update(task, advance=10, description=f"Processing: {log['message']}")
                
                # Generate image using FAL.ai
                result = fal_client.subscribe(
                    model,
                    arguments={
                        "prompt": enhanced_prompt,
                        "guidance_scale": guidance_scale,
                        "num_images": 1,
                        "safety_tolerance": safety_tolerance,
                        "output_format": "png",
                        "aspect_ratio": aspect_ratio
                    },
                    with_logs=True,
                    on_queue_update=on_queue_update,
                )
                
                progress.update(task, completed=90, description="Downloading image...")
                
                # Download the generated image
                image_url = result["images"][0]["url"]
                response = requests.get(image_url, timeout=30)
                
                if response.status_code != 200:
                    logger.error(f"Failed to download image - HTTP {response.status_code}")
                    return False
                
                # Ensure output directory exists
                output_dir = Path(output_path).parent
                output_dir.mkdir(parents=True, exist_ok=True)
                
                # Save the image
                with open(output_path, "wb") as f:
                    f.write(response.content)
                
                progress.update(task, completed=100, description="Complete!")
            
            # Verify and get image info
            try:
                with Image.open(output_path) as img:
                    actual_size = img.size
                    file_size = Path(output_path).stat().st_size / 1024  # KB
                    
                    console.print(f"✅ [green]Image generated successfully![/green]")
                    console.print(f"   📁 Saved to: {output_path}")
                    console.print(f"   📐 Size: {actual_size[0]}x{actual_size[1]} pixels")
                    console.print(f"   💾 File size: {file_size:.1f} KB")
                    
            except Exception as e:
                logger.warning(f"Could not verify image: {e}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error generating image: {e}")
            return False
    
    def batch_generate(
        self,
        prompts: List[str],
        output_dir: str,
        template: Optional[str] = None,
        resolution: str = "blog-header",
        variations: int = 1,
        **kwargs
    ) -> List[str]:
        """
        Generate multiple images in batch.
        
        Args:
            prompts: List of prompts to generate
            output_dir: Directory to save all images
            template: Template to use for all images
            resolution: Resolution preset for all images
            variations: Number of variations per prompt
            **kwargs: Additional arguments for generate_image
            
        Returns:
            List of successfully generated image paths
        """
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        successful_images = []
        total_images = len(prompts) * variations
        
        console.print(f"\n🚀 [bold blue]Starting batch generation[/bold blue]")
        console.print(f"   📝 Prompts: {len(prompts)}")
        console.print(f"   🔄 Variations per prompt: {variations}")
        console.print(f"   📊 Total images: {total_images}")
        console.print(f"   📁 Output directory: {output_dir}")
        
        with Progress(console=console) as progress:
            main_task = progress.add_task("Overall progress", total=total_images)
            
            for i, prompt in enumerate(prompts, 1):
                # Clean prompt for filename
                safe_prompt = "".join(c for c in prompt[:50] if c.isalnum() or c in (' ', '-', '_')).strip()
                safe_prompt = safe_prompt.replace(' ', '_').lower()
                
                for variation in range(variations):
                    if variations > 1:
                        filename = f"{i:02d}_{safe_prompt}_v{variation + 1}.png"
                    else:
                        filename = f"{i:02d}_{safe_prompt}.png"
                    
                    output_file = output_path / filename
                    
                    console.print(f"\n📸 Generating: {filename}")
                    
                    success = self.generate_image(
                        prompt=prompt,
                        output_path=str(output_file),
                        template=template,
                        resolution=resolution,
                        **kwargs
                    )
                    
                    if success:
                        successful_images.append(str(output_file))
                    
                    progress.update(main_task, advance=1)
        
        # Summary
        console.print(f"\n✨ [bold green]Batch generation complete![/bold green]")
        console.print(f"   ✅ Successful: {len(successful_images)}/{total_images}")
        console.print(f"   📁 Location: {output_dir}")
        
        if len(successful_images) < total_images:
            console.print(f"   ⚠️  [yellow]Some images failed to generate[/yellow]")
        
        return successful_images

def list_templates():
    """Display available templates in a nice table."""
    table = Table(title="🎨 Available Professional Templates")
    table.add_column("Template ID", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Description", style="white")
    
    for template_id, template_data in PROMPT_TEMPLATES.items():
        # Truncate description for display
        description = template_data["base_prompt"]
        if len(description) > 80:
            description = description[:77] + "..."
        
        table.add_row(template_id, template_data["name"], description)
    
    console.print(table)
    
    console.print(f"\n💡 [bold blue]Usage examples:[/bold blue]")
    console.print(f"   [dim]# Use iOS-AI template[/dim]")
    console.print(f"   python scripts/generate-header.py \"CoreML optimization tips\" --template ios-ai")
    console.print(f"   [dim]# Custom prompt with productivity template[/dim]")
    console.print(f"   python scripts/generate-header.py \"Workflow automation\" --template productivity")

def list_resolutions():
    """Display available resolution presets."""
    table = Table(title="📐 Available Resolution Presets")
    table.add_column("Preset", style="cyan", no_wrap=True)
    table.add_column("Dimensions", style="magenta")
    table.add_column("Aspect Ratio", style="white")
    table.add_column("Best For", style="green")
    
    use_cases = {
        "blog-header": "Blog post headers",
        "social-media": "Facebook/Twitter shares",
        "hero-banner": "Website hero sections",
        "thumbnail": "Preview images",
        "square": "Instagram posts",
        "story": "Instagram/TikTok stories"
    }
    
    for preset, (width, height) in RESOLUTION_PRESETS.items():
        aspect_ratio = f"{width//gcd(width, height)}:{height//gcd(width, height)}"
        table.add_row(preset, f"{width}×{height}", aspect_ratio, use_cases.get(preset, "General use"))
    
    console.print(table)

def main():
    parser = argparse.ArgumentParser(
        description="🎨 Professional Header Image Generator for Igor's Blog",
        epilog="Generate high-quality header images optimized for technical blog posts about iOS development and AI.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Main arguments
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Text description of the image to generate"
    )
    
    parser.add_argument(
        "--output", "-o",
        default="./header.png",
        help="Output file path or directory for batch generation (default: ./header.png)"
    )
    
    # Template and styling
    parser.add_argument(
        "--template", "-t",
        choices=list(PROMPT_TEMPLATES.keys()),
        help="Professional template to use for styling"
    )
    
    parser.add_argument(
        "--custom-style", "-s",
        help="Additional custom styling instructions"
    )
    
    # Resolution and dimensions
    parser.add_argument(
        "--resolution", "-r",
        choices=list(RESOLUTION_PRESETS.keys()) + ["custom"],
        default="blog-header",
        help="Resolution preset (default: blog-header)"
    )
    
    parser.add_argument(
        "--custom-dimensions",
        type=str,
        help="Custom dimensions in format 'WIDTHxHEIGHT' (e.g., '1200x800')"
    )
    
    # Generation options
    parser.add_argument(
        "--model",
        default="fal-ai/flux-pro/kontext/max/text-to-image",
        help="FAL.ai model to use (default: FLUX Pro Kontext Max)"
    )
    
    parser.add_argument(
        "--guidance-scale",
        type=float,
        default=3.5,
        help="Guidance scale for generation (1.0-20.0, default: 3.5)"
    )
    
    parser.add_argument(
        "--safety-tolerance",
        default="2",
        choices=["1", "2", "3", "4", "5", "6"],
        help="Safety filter tolerance (default: 2)"
    )
    
    # Batch generation
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Enable batch generation mode (read prompts from file or stdin)"
    )
    
    parser.add_argument(
        "--batch-file",
        help="File containing prompts for batch generation (one per line)"
    )
    
    parser.add_argument(
        "--variations",
        type=int,
        default=1,
        help="Number of variations to generate per prompt in batch mode (default: 1)"
    )
    
    # Information commands
    parser.add_argument(
        "--template-list",
        action="store_true",
        help="List all available professional templates"
    )
    
    parser.add_argument(
        "--resolution-list",
        action="store_true",
        help="List all available resolution presets"
    )
    
    # Debug options
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Configure logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Handle information commands
    if args.template_list:
        list_templates()
        return
    
    if args.resolution_list:
        list_resolutions()
        return
    
    # Validate required arguments for generation
    if not args.prompt and not args.batch and not args.batch_file:
        console.print("❌ [red]Error: No prompt provided[/red]")
        console.print("Use --help for usage information, or --template-list to see available templates")
        sys.exit(1)
    
    try:
        # Initialize generator
        generator = HeaderImageGenerator()
        
        # Handle custom dimensions
        custom_dimensions = None
        if args.custom_dimensions:
            try:
                width, height = map(int, args.custom_dimensions.split('x'))
                custom_dimensions = (width, height)
            except ValueError:
                console.print(f"❌ [red]Invalid custom dimensions format: {args.custom_dimensions}[/red]")
                console.print("Use format 'WIDTHxHEIGHT' (e.g., '1200x800')")
                sys.exit(1)
        
        # Handle batch generation
        if args.batch or args.batch_file:
            prompts = []
            
            if args.batch_file:
                # Read prompts from file
                try:
                    with open(args.batch_file, 'r', encoding='utf-8') as f:
                        prompts = [line.strip() for line in f if line.strip()]
                except FileNotFoundError:
                    console.print(f"❌ [red]Batch file not found: {args.batch_file}[/red]")
                    sys.exit(1)
            elif args.prompt:
                # Single prompt in batch mode
                prompts = [args.prompt]
            else:
                console.print("❌ [red]No prompts provided for batch generation[/red]")
                sys.exit(1)
            
            if not prompts:
                console.print("❌ [red]No valid prompts found[/red]")
                sys.exit(1)
            
            # Generate batch
            successful = generator.batch_generate(
                prompts=prompts,
                output_dir=args.output,
                template=args.template,
                resolution=args.resolution,
                custom_dimensions=custom_dimensions,
                variations=args.variations,
                model=args.model,
                guidance_scale=args.guidance_scale,
                safety_tolerance=args.safety_tolerance,
                custom_style=args.custom_style
            )
            
            if not successful:
                sys.exit(1)
                
        else:
            # Single image generation
            success = generator.generate_image(
                prompt=args.prompt,
                output_path=args.output,
                template=args.template,
                resolution=args.resolution,
                custom_dimensions=custom_dimensions,
                model=args.model,
                guidance_scale=args.guidance_scale,
                safety_tolerance=args.safety_tolerance,
                custom_style=args.custom_style
            )
            
            if not success:
                sys.exit(1)
    
    except KeyboardInterrupt:
        console.print("\n⚠️  [yellow]Generation cancelled by user[/yellow]")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose:
            console.print_exception()
        sys.exit(1)

if __name__ == "__main__":
    main()