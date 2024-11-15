import os
import fal_client
import argparse
from typing import List, Tuple
import re

# Valid options from the API
VALID_STYLES = {
    "any",
    "realistic_image",
    "digital_illustration",
    "vector_illustration",
    "realistic_image/b_and_w",
    "realistic_image/hard_flash",
    "realistic_image/hdr",
    "realistic_image/natural_light",
    "realistic_image/studio_portrait",
    "realistic_image/enterprise",
    "realistic_image/motion_blur",
    "digital_illustration/pixel_art",
    "digital_illustration/hand_drawn",
    "digital_illustration/grain",
    "digital_illustration/infantile_sketch",
    "digital_illustration/2d_art_poster",
    "digital_illustration/handmade_3d",
    "digital_illustration/hand_drawn_outline",
    "digital_illustration/engraving_color",
    "digital_illustration/2d_art_poster_2",
    "vector_illustration/engraving",
    "vector_illustration/line_art",
    "vector_illustration/line_circuit",
    "vector_illustration/linocut",
}

VALID_SIZES = {
    "square_hd",
    "square",
    "portrait_4_3",
    "portrait_16_9",
    "landscape_4_3",
    "landscape_16_9",
}


def hex_to_rgb(hex_color: str) -> dict:
    """Convert hex color to RGB dict format."""
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return {"r": r, "g": g, "b": b}


def parse_size(size: str) -> dict:
    """Parse size string into proper format."""
    if size in VALID_SIZES:
        return size

    # Parse custom size in format "widthxheight"
    match = re.match(r"(\d+)x(\d+)", size)
    if match:
        width, height = map(int, match.groups())
        return {"width": width, "height": height}

    raise ValueError(
        f"Invalid size format. Use one of {VALID_SIZES} or WIDTHxHEIGHT format"
    )


def generate_image(
    prompt: str, style: str, size: str, colors: List[str], output_path: str
):
    """
    Generate an image using Recraft V3 model.

    Args:
        prompt (str): Text description of the image to generate
        style (str): Style to use for generation
        size (str): Image size (predefined or custom WIDTHxHEIGHT)
        colors (List[str]): List of hex color codes
        output_path (str): Path where to save the output image
    """
    if style not in VALID_STYLES:
        print(f"Error: Invalid style '{style}'")
        raise ValueError(f"Invalid style. Valid options are: {VALID_STYLES}")

    # Convert hex colors to RGB format
    rgb_colors = [hex_to_rgb(color) for color in colors]

    # Parse and validate size
    image_size = parse_size(size)

    try:
        # Call the API
        print("Calling Recraft V3 API...")
        api_args = {
            "prompt": prompt,
            "style": style,
            "image_size": image_size,
            "colors": rgb_colors,
        }
        print(f"API arguments: {api_args}")

        result = fal_client.subscribe("fal-ai/recraft-v3", arguments=api_args)
        print("Successfully received API response")

        # Get the image URL from result
        image_url = result["images"][0]["url"]
        print(f"Image URL received: {image_url}")

        # Download and save the image
        import requests

        print("Downloading image...")
        response = requests.get(image_url)

        if response.status_code == 200:
            print(f"Download successful, saving to {output_path}")
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"Image successfully saved to {output_path}")
        else:
            print(f"Failed to download image - HTTP {response.status_code}")
            print(f"Response content: {response.text}")

    except Exception as e:
        print(f"Error generating image: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback

        print(f"Full traceback:\n{traceback.format_exc()}")


def main():
    parser = argparse.ArgumentParser(description="Generate images using Recraft V3")
    parser.add_argument(
        "--style",
        default="digital_illustration/hand_drawn_outline",
        help=f"Style to use for generation. Options: {', '.join(VALID_STYLES)}",
    )
    parser.add_argument(
        "--size",
        default="landscape_16_9",
        help=f"Image size. Use predefined ({', '.join(VALID_SIZES)}) or WIDTHxHEIGHT format",
    )
    parser.add_argument(
        "--colors",
        nargs="*",
        default=["#1c2128", "#da532c", "#858585"],
        help="List of hex color codes (e.g., #FF0000 #00FF00)",
    )
    parser.add_argument("--prompt", help="Text prompt describing the image to generate")
    parser.add_argument("--output", help="Output file path")

    args = parser.parse_args()

    # Check if FAL_KEY is set
    if not os.getenv("FAL_KEY"):
        print("Error: FAL_KEY environment variable not set")
        return

    generate_image(args.prompt, args.style, args.size, args.colors, args.output)


if __name__ == "__main__":
    main()
