#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fal-client",
#   "requests",
# ]
# ///

import os
import fal_client
import argparse
import requests


def on_queue_update(update):
    """Handle queue updates during image generation."""
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(f"[Progress] {log['message']}")


def generate_image(prompt: str, output_path: str, aspect_ratio: str = "16:9"):
    """
    Generate an image using Flux Kontext model.

    Args:
        prompt (str): Text description of the image to generate
        output_path (str): Path where to save the output image
        aspect_ratio (str): Aspect ratio for the image (default: 16:9)
    """
    try:
        print(f"Generating image with Flux Kontext...")
        print(f"Prompt: {prompt}")
        print(f"Aspect ratio: {aspect_ratio}")
        
        result = fal_client.subscribe(
            "fal-ai/flux-pro/kontext/max/text-to-image",
            arguments={
                "prompt": prompt,
                "guidance_scale": 3.5,
                "num_images": 1,
                "safety_tolerance": "2",
                "output_format": "png",
                "aspect_ratio": aspect_ratio
            },
            with_logs=True,
            on_queue_update=on_queue_update,
        )
        
        # Get the image URL from result
        image_url = result["images"][0]["url"]
        print(f"Image generated: {image_url}")

        # Download and save the image
        print("Downloading image...")
        response = requests.get(image_url)

        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"✓ Image saved to {output_path}")
        else:
            print(f"Failed to download image - HTTP {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Generate header images and illustrations using Flux Kontext"
    )
    parser.add_argument(
        "prompt",
        help="Text prompt describing the image to generate"
    )
    parser.add_argument(
        "output",
        help="Output file path (e.g., header.png)"
    )
    parser.add_argument(
        "--aspect-ratio",
        default="16:9",
        choices=["1:1", "4:3", "3:2", "16:9", "21:9", "3:4", "2:3", "9:16", "9:21"],
        help="Aspect ratio for the image (default: 16:9)"
    )

    args = parser.parse_args()

    # Check if FAL_KEY is set
    if not os.getenv("FAL_KEY"):
        print("Error: FAL_KEY environment variable not set")
        print("Get your API key from https://fal.ai/")
        return

    generate_image(args.prompt, args.output, args.aspect_ratio)


if __name__ == "__main__":
    main()