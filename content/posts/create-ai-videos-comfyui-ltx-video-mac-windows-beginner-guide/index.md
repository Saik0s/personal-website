---
title: "The $0 AI Video Playbook: ComfyUI + Flux + LTX-Video"
subtitle: "Create Jaw-Dropping Videos From Images (Even If You're Clueless)"
date: 2025-04-30T04:48:17+02:00
lastmod: 2025-04-30T04:48:17+02:00
draft: false
authors: ["Igor"]
description: "Tired of AI video hype that doesn't deliver? Get the exact steps to turn static images into pro-level videos using ComfyUI, Flux & LTX-Video. No BS, no prior skills needed. Works on Mac/Windows."

tags: ["ai", "comfyui"]
categories: ["AI & Machine Learning", "Tutorials"]
series: ["AI Video Creation"]

hiddenFromHomePage: false
hiddenFromSearch: false

featuredImage: "header.png"
featuredImagePreview: "header_preview.png"

math:
  enable: false
toc:
  enable: false
code:
  copy: true
lightgallery: false
license: ""
---

<!--more-->

*Turn text into living videos with AI. This guide shows you how to chain Flux (for images) and LTX-Video (for motion) in ComfyUI's visual programming interface.*

> 🎯 **Difficulty:** Like assembling IKEA furniture with instructions
>
> ⏱️ **Time Investment:** 1-2 hours setup, then 5-10 minutes per video
>
> 💻 **Hardware:** NVIDIA GPU (16GB+ VRAM) or M1/M2 Mac (16GB+ RAM)

## Intro

### The AI Video Pipeline Explained

1. **Text → Image (Flux)**
   - You describe a scene ("a cyberpunk detective smoking")
   - Flux generates a high-quality still image
   - *Think of this as writing a movie script for a single frame*

2. **Image → Video (LTX-Video)**
   - You describe motion ("slow zoom in, cigarette smoke rising")
   - LTX-Video animates the image over set number of frames
   - *This is where your still photo becomes a living scene*

### Core Concepts Made Simple

**Diffusion Models (How AI Creates)**
- Imagine starting with a blurry, static-filled TV screen
- The AI gradually clears up this static based on your description
- With each step, the picture becomes clearer until your image appears
- *It's like watching a Polaroid photo develop before your eyes*

**VAE (Variational Autoencoder)**
- Think of this as the translator between what you see (the image) and what the AI understands
- You don't need to worry about how it works - it happens automatically

**Text Encoders (Your Words to AI Language)**
- These turn your everyday English into special code the AI can understand
- Like having a personal interpreter who speaks both human and computer

**Samplers (Different Quality Settings)**
- Think of these as different quality modes on your camera
- "Quick mode" = faster but rougher results
- "Detailed mode" = slower but prettier results
- You'll mostly use the default, which is a good balance

**VRAM (Video Memory)**
- Model weights need to be loaded into VRAM to be used
- Bigger models require more VRAM
- 12GB VRAM is the minimum for most models
- 24GB VRAM is recommended for better performance

**Nodes - ComfyUI's Building Blocks**
- Each node does one specific job
- Connect them like LEGO to build workflows
- *Example pipeline:*
  1. `Text Prompt` → `Flux Sampler` → `Image`
  2. `Image + Motion Prompt` → `LTX Sampler` → `Video`

*Pro Tip:* FP16 gives better quality but needs more VRAM. FP8 is more efficient for testing ideas.

### The Full Assembly Line

1. **Load Models** (Flux + LTX)
2. **Text Prompt** → Flux generates image
3. **Image + Motion Prompt** → LTX generates video frames
4. **Save Video** (stitches frames together)

## Quick Start Guide

For those who want to jump right in, here's the TL;DR version:

1. **Install ComfyUI Desktop** (15-20 min)
   - Windows: Download and install ComfyUI Desktop from [comfy.org](https://comfy.org/download) (NVIDIA GPU required)
   - Mac: Download and install ComfyUI Desktop from [comfy.org](https://comfy.org/download) (Apple Silicon only)
   - Advanced users can alternatively use `pip install comfy-cli` for CLI installation

2. **Download Required Models** (20-30 min)
   - **Flux/RedCraft model** (~11GB)
     - ![redcraft](redcraft-download.png)
     - Download: [RedCraft RealReveal5 ULTRA (FP8, pruned)](https://civitai.green/models/958009?modelVersionId=1576605)
     - Save to: `models/unet/RedCraft_RealReveal5_ULTRA_15Steps_fp8_pruned.safetensors`
   - **LTX Video model** (~6GB)
     - Download: [ltxv-2b-0.9.6-distilled-04-25.safetensors](https://huggingface.co/Lightricks/LTX-Video/blob/main/ltxv-2b-0.9.6-distilled-04-25.safetensors)
     - Save to: `models/checkpoints/ltxv-2b-0.9.6-distilled-04-25.safetensors`
   - **T5 XXL text encoder** (4.89 GB)
     - Download: [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors)
     - Save to: `models/text_encoders/t5xxl_fp8_e4m3fn.safetensors`
   - **CLIP text encoder** (246 MB)
     - Download: [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors)
     - Save to: `models/clip/clip_l.safetensors`
   - **VAE** (168 MB)
     - Download: [diffusion_pytorch_model.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/vae/diffusion_pytorch_model.safetensors)
     - Save to: `models/vae/vae.safetensors` (rename `diffusion_pytorch_model.safetensors` to `vae.safetensors`)

3. **Run workflow** (2-10 minutes)
   - Open [Workflow file](./ltx_video_workflow.json)
   - Make sure correct models are selected in the nodes
   - Write descriptive prompt for first frame
   - Write motion prompt for the rest of the video
   - Run workflow

> 💡 **Pro Tip:** Start with simple camera movements like gentle pans or zooms for best results.

For detailed instructions and troubleshooting, continue reading below.

## What is ComfyUI, Flux, and LTX Video?

**ComfyUI** is a powerful, node-based graphical interface for image generation. Instead of writing code, you visually connect **blocks (nodes)** to build an AI pipeline. For example, one node loads an AI model, another takes your text prompt, another generates an image, etc. You chain these nodes to create workflows for images or even videos. It's like building a flowchart that produces art!

**Flux** is a family of high-quality text-to-image diffusion models developed by Black Forest Labs. As of early 2025, Flux models are considered some of the best image generation models. In simple terms, Flux is the AI "brain" we'll use to generate a stunning portrait from your text prompt. We will use a custom version of Flux model called *RedCraft RealReveal5 ULTRA* that is optimized for portraits.

**LTX Video** is an open-source video generation model developed by Lightricks. It takes an image (or text) and generates a short video clip by imagining motion. LTX is optimized for speed – for instance, version 0.9.5 could render a 4-second video in ~17 seconds on an RTX 4090. We will use 0.9.6-distilled version of LTX Video model which is even faster. It's not magic movie maker – think of it as adding subtle motion (camera movements, slight subject movements, etc.) to a still image.

**How they fit together:** First, **Flux** generates a vertical portrait image from a prompt (e.g. a person or scene you describe). Then **LTX Video** takes that image and a "motion prompt" (describing how the camera or subject should move) to produce a series of frames – in other words, a short video. ComfyUI is the glue that lets us run Flux and LTX in one workflow: the output of the image generation nodes will feed into the video generation nodes. Essentially, **text → image → video** all within ComfyUI, using Flux and LTX under the hood.

## How Does Text Become a Video?

At a high level, the process works in two stages:

- **Stage 1: Text-to-Image (Flux)** – You write a text prompt describing the portrait or scene you want. ComfyUI feeds this prompt into the Flux model, which diffuses random noise into an image that matches your description. This is done via a neural network that has learned to generate images from text. The result is a single AI-generated **portrait image** (we'll make it vertical format for TikTok).

![](portrait_1.png)

[AI Generation Description: A clean, minimalist technical diagram on a white background. Three connected boxes arranged horizontally, labeled "Text Input" (left), "Flux Model" (center), and "Generated Image" (right). Boxes are light blue (#E6F3FF) with dark blue borders (#2B5D9B). Black arrows (→) connect the boxes from left to right. Each box has a subtle drop shadow. The text is in a modern sans-serif font (Arial or Helvetica) in dark gray (#333333). The diagram has a professional, technical appearance similar to software documentation.]

- **Stage 2: Image-to-Video (LTX)** – Now take the image from Stage 1 and feed it, along with a **motion prompt**, into the LTX Video model. LTX generates additional frames as if the scene in the image is moving or the camera is moving. It does this by diffusing noise into new images while trying to stay consistent with the original picture. Essentially, it treats the Stage 1 image as the starting frame of a video, then creates subsequent frames based on your motion description.

[AI Generation Description: A horizontal strip showing 5 sequential video frames arranged left to right. Each frame captures the same young woman from the earlier portrait, showing a smooth camera pan from left to right. Her hair shows subtle, natural movement in the breeze across the frames. Frame 1: Camera positioned left, showing her profile. Frame 2-4: Progressive movement rightward, revealing more of her face. Frame 5: Final position showing three-quarter view. The lighting remains consistent across all frames, maintaining the warm, natural sunlight. Each frame is labeled with a small frame number in the corner. Style: Cinematic quality, 24fps motion blur, professional color grading.]

[AI Generation Description: A professional flowchart diagram showing the LTX video generation process. Four main elements arranged horizontally: 1) Two input boxes at left labeled "Initial Image" and "Motion Prompt" (stacked vertically), 2) Arrows flowing right to a central box, 3) A prominent center box labeled "LTX Model" with a subtle AI-themed icon, 4) An output box showing a filmstrip of multiple frames. The design uses a modern tech aesthetic with a blue and white color scheme (#2B5D9B, #FFFFFF). Connecting arrows are animated-style with gradient effects. The background is clean white with a subtle grid pattern. Text uses a modern sans-serif font. Style: Modern tech infographic, clean vector graphics.]

ComfyUI links these stages, so after Stage 1 finishes, Stage 2 can use the output automatically. The end result is a short video (several seconds long) where the initial AI image comes to life. You might see the camera zoom or pan, the subject's expression change slightly, or environmental movement, depending on your motion prompt. It's like those Harry Potter photos – still images that move a bit!

## What to Expect (and What *Not* to Expect)

Before we get into the nuts and bolts, let's set realistic expectations:

- **Video Length & Quality:** The model generates high-quality videos at **24 FPS** with support for up to **129 frames** (about 5.4 seconds). The idea is to produce cinematic sequences with smooth, natural motion. Quality can be surprisingly good for camera movements and subtle animations. For example, a gentle pan or the subject's expression changing can look very natural. However, complex movements (like running, or multiple subjects interacting) will **not** look realistic – the model isn't that advanced yet.

- **Speed:** The latest LTX Video model (0.9.6-distilled) is highly optimized and can generate videos faster than real-time playback at 24 FPS on high-end GPUs. On a high-end GPU (e.g. Nvidia RTX 3080/4090), you can expect generation times of 15-30 seconds for a typical video. On lower-end hardware (or Apple M1/M2), it will be slower (possibly a few minutes total), but still much faster than traditional video rendering or earlier AI video models. The distilled model achieves this speed by using only 8 diffusion steps per frame while maintaining quality.

- **Realism Limits:** The output video is essentially a series of AI-generated images, so you might see minor flicker or differences frame to frame (the model works to keep them consistent, but it's not perfect). The motions will be subtle. For instance, you can create a slow camera pan, slight subject movements (like a head turn or smile), or environmental effects (like leaves trembling). It excels at **small, smooth changes**. If you try something extreme (like "she starts dancing wildly"), the result will likely be strange or glitchy. **Don't expect** the kind of coherence you'd get from a real video camera – think of it more like a moving painting.

- **Resolution:** The model works on resolutions that are divisible by 32 and number of frames that are divisible by 8 + 1 (e.g. 257). In case the resolution or number of frames are not divisible by 32 or 8 + 1, the input will be padded with -1 and then cropped to the desired resolution and number of frames. The model works best on resolutions under 720 x 1280 and number of frames below 257. For optimal performance, **768×512** resolution is recommended, where it can generate videos faster than real-time playback.

- **One scene only:** LTX does not *create new content per frame*; it transforms the given image. So if your image is a person standing, the video will be that same person – they won't suddenly change clothes or location (unless your motion prompt somehow forces a change, but that often just yields artifacts). It's essentially **the same scene with slight motion**. This is great for cinematic camera moves or a bit of life in a portrait, but not for storyboarding multi-scene sequences.

In short, **expect** a short, artsy moving portrait with mild motion. **Don't expect** a full dynamic action sequence or a perfectly stable video on the first try. Part of the fun is experimenting and seeing what the AI can do within these limits!

## Requirements: Hardware and Software

Let's make sure you have the right setup before we proceed.

**Operating System:** You can do this on **Windows or macOS**. (Linux works too, but this guide focuses on Win/Mac.) On Windows, you'll need an **NVIDIA GPU** for GPU acceleration ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)). On macOS, you'll need an **Apple Silicon** Mac (M1, M2, M3 chips) ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)) – the Desktop version of ComfyUI doesn't support Intel Macs, and Apple Silicon provides the needed ML acceleration (Metal Performance Shaders).

**GPU and VRAM:** For Windows/NVIDIA users, a GPU with at least **8 GB VRAM** is recommended. 12GB+ will allow higher resolution (up to 720×1280) and more frames. (Flux and LTX are heavy models; Flux's all-in-one FP8 model is ~11 GB on disk and typically wants ~16 GB VRAM to run comfortably, but it can work on 8–12 GB with optimizations or lower resolution.) The LTX 0.9.6-distilled model is optimized for efficiency, requiring only 8 diffusion steps per frame. For macOS M1/M2 users, at least **16 GB unified memory** is recommended (32 GB is better). Macs use the GPU integrated in the chip – it can run these models, but slower. Be prepared for longer generation times on Mac compared to a high-end PC GPU. If you have no dedicated GPU (and only a CPU), it's technically possible to run ComfyUI, but it will be **extremely slow** (minutes per frame); this guide assumes you have some GPU capability.

**RAM and Disk:** Ensure you have sufficient disk space – the models are large (the Flux model ~11 GB, LTX model ~ >2 GB, plus another ~10 GB for a text encoder file). RAM isn't usually a bottleneck beyond what's needed to load models into VRAM, but having 16 GB+ system RAM is a good idea.

**Software:** We will use **ComfyUI Desktop** (the easy installer version). ComfyUI will handle all the heavy lifting (no need to install Python environments manually unless you want to). We'll also use ComfyUI's built-in **Manager** to install the needed **custom nodes** (the LTX extension, etc.). No coding required – just some downloads and clicking.

**Summary:**

- **Windows + NVIDIA GPU** (8GB+ VRAM, Windows 10/11) – Supported (ComfyUI Desktop for Windows) ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)).
- **macOS + Apple Silicon (M1/M2)** (16GB+ recommended) – Supported (ComfyUI Desktop for Mac) ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)).
- **macOS Intel or Windows with AMD GPU** – *Not directly supported by ComfyUI Desktop.* You would need to use the ComfyUI source/CLI with relevant hacks (beyond this guide). It's possible via PlaidML or CPU, but not beginner-friendly.
- **Storage** – ~35 GB free for models/files.
- **Internet** – needed to download models and ComfyUI, but generation itself runs locally.

Now that we have what we need, let's get everything set up.

## Installation: ComfyUI Desktop

ComfyUI Desktop is the easiest way to get up and running. It packages ComfyUI with a one-click installer and manages all the Python dependencies for you. No need to use the command line (unless you want to).

> ⚠️ **System Requirements Check**
> Before proceeding, verify you have:
> - Windows: NVIDIA GPU with 8GB+ VRAM, Windows 10/11
> - Mac: M1/M2/M3 chip, 16GB+ unified memory
> - ~35GB free disk space for models
> - Stable internet connection for downloads

### 🪟 Windows Installation (15-20 minutes)

1. **Download ComfyUI Desktop:** Go to the official [ComfyUI download page](https://comfy.org/download) and click **"Download for Windows (NVIDIA)"**. The Windows version requires an NVIDIA graphics card for CUDA support.

2. **Run the Installer:** Double-click the downloaded installation package. The installer will:
   - Create a ComfyUI Desktop shortcut on your desktop
   - Set up the required environment
   - Install dependencies (including PyTorch, which is several GB)

3. **First Launch & Setup:**
   - Double-click the ComfyUI Desktop shortcut
   - On first run, you'll see an initialization screen
   - Select "NVIDIA GPU (Recommended)" when prompted
   - Choose an installation location (preferably on an SSD with at least 15GB free space)
   - Optionally import settings from an existing ComfyUI installation
   - Configure preferences (updates, analytics, etc.)
   - Wait for the initialization to complete

4. **Verify Installation:**
   - The ComfyUI interface should open automatically
   - You'll see a blank canvas with a toolbar (Manager, Load, Save, Queue buttons)
   - Check the console for "Using device cuda" to confirm GPU detection

> 🔧 **Pro Tip:** Windows Defender might warn about Python components - this is normal as ComfyUI is a Python application. The software is open source and safe.

### 🍎 macOS Installation (15-20 minutes)

1. **Download ComfyUI Desktop:** On the [ComfyUI download page](https://comfy.org/download), click **"Download for MacOS"**. The app requires Apple Silicon (M1/M2/M3) - Intel Macs are not supported.

2. **Install the App:**
   - Open the downloaded .dmg file
   - Drag ComfyUI into your Applications folder
   - If you see a prohibition sign on the icon, your system may not be compatible

3. **First Launch & Setup:**
   - Find ComfyUI in Launchpad and click to open
   - Right-click and choose "Open" if you see a Gatekeeper warning
   - On the initialization screen, select "MPS (Recommended)" for GPU acceleration
   - Choose an installation location (ensure ~5GB free space)
   - Optionally import existing ComfyUI settings
   - Configure preferences (updates, analytics, etc.)
   - Wait for initialization to complete (includes downloading ~15GB of dependencies)

4. **Verify Installation:**
   - The ComfyUI interface should open automatically
   - You'll see the node editor interface
   - The app uses Metal Performance Shaders (MPS) for acceleration

> 🚨 **M1/M2/M3 Mac Note:** First run is slower due to PyTorch optimization compilation. Performance improves in subsequent runs.

### ⌨️ Optional: ComfyUI via CLI (Advanced Users)

If you're comfortable with the terminal or need features not available in the Desktop app (like AMD GPU support), you can use the CLI installation method:

1. **Install ComfyUI CLI:**
```bash
pip install comfy-cli
```

2. **Create and activate a Python environment:**
```bash
# Using conda
conda create -n comfy-env python=3.11
conda activate comfy-env

# Or using venv
python -m venv comfy-env
source comfy-env/bin/activate  # On Unix/Mac
comfy-env\Scripts\activate     # On Windows
```

3. **Install ComfyUI:**
```bash
comfy install
```

4. **Launch ComfyUI:**
```bash
comfy launch
```

The CLI version offers more flexibility and control, but requires more technical knowledge. For most users, **ComfyUI Desktop** is recommended as it handles updates and environment management automatically. Now, let's proceed to downloading the required AI models.

## Downloading the Models (Flux and LTX)

We need to download two model files: the *Flux model* (for image generation) and the *LTX Video model* (for video generation). We'll also grab a necessary **text encoder** file for LTX (and Flux) to understand prompts properly.

### 1. Flux Model – "RedCraft RealReveal5 ULTRA" (Flux-based)

Flux.1 is the core model, but here we'll use a specialized **Flux checkpoint** that's good for portraits. The creators of RedCraft RealReveal5 ULTRA (a Flux-based model) provided a ready-to-use safetensor file. Download it from Civitai using this link:

- **Flux model download:** [RedCraft RealReveal5 ULTRA (Flux, FP8, pruned) – safetensors, ~11GB】 ([RedCraft | 红潮 CADS | UPdated-Apr28 | Commercial & Advertising Design System - Reveal5[SFW]ULTRA | Flux Checkpoint | Civitai](https://civitai.green/models/958009/redcraft-or-cads-or-updated-apr15-or-commercial-and-advertising-design-system?modelVersionId=1576605#:~:text=Download%20%2811)) ([RedCraft | 红潮 CADS | UPdated-Apr28 | Commercial & Advertising Design System - Reveal5[SFW]ULTRA | Flux Checkpoint | Civitai](https://civitai.green/models/958009/redcraft-or-cads-or-updated-apr15-or-commercial-and-advertising-design-system?modelVersionId=1576605#:~:text=2%20Files)). (**Tip:** If clicking a direct download link doesn't work in browser, you may copy it or use the Civitai page. On the Civitai page, look for a download button showing ~11.08 GB ([RedCraft | 红潮 CADS | UPdated-Apr28 | Commercial & Advertising Design System - Reveal5[SFW]ULTRA | Flux Checkpoint | Civitai](https://civitai.green/models/958009/redcraft-or-cads-or-updated-apr15-or-commercial-and-advertising-design-system?modelVersionId=1576605#:~:text=Download%20%2811)).)

Save this `.safetensors` file to a location you can find. (It might be named along the lines of `RedCraft_RealReveal5_ULTRA_15Steps_fp8_pruned.safetensors` – that's just an example.)

### 2. LTX Video Model

Next, get the LTX model weights:

- **LTX model download:** Download **ltxv-2b-0.9.6-distilled-04-25.safetensors** from [Hugging Face – Lightricks LTX-Video repo](https://huggingface.co/Lightricks/LTX-Video). The file is around 2–3 GB. This is the "0.9.6 distilled" version – a highly optimized version of LTX that requires only 8 diffusion steps per frame while maintaining high quality output. It's specifically designed for fast generation, capable of producing 24 FPS videos at 768x512 resolution faster than they can be watched.

If you have trouble finding that exact file, you can use the direct link provided (in ComfyUI Manager you could also search for LTXVideo and see if it provides links). Ensure the file is named `ltxv-2b-0.9.6-distilled-04-25.safetensors` (or similar).

### 3. T5 XXL Text Encoder and CLIP (for prompts)

Both Flux and LTX rely on text encoders to understand prompts with greater detail. The T5-XXL encoder handles longer, more complex descriptions, while CLIP provides additional understanding capabilities. The good news is that ComfyUI Manager can automatically download and install these for you:

1. In ComfyUI, click the "Manager" button in the top toolbar
2. Look for any missing model notifications
3. Click to automatically download T5 and CLIP encoders

[AI Generation Description: A screenshot of the ComfyUI Manager interface window. The window has a dark theme background (#1E1E1E) with a clean, modern UI. At the top is a search bar and filter options. Below are listed model download cards arranged in a grid. Each card shows: model name in bold, file size, download progress bar, and an install/download button (blue #2B5D9B). The T5 and CLIP encoders are highlighted or marked as "Required". The interface includes typical UI elements like scroll bars, tooltips, and status indicators. Style: Modern software UI, high resolution, clear typography.]

Alternatively, you can manually download these files:

- **T5 encoder:** Download **t5xxl_fp8_e4m3fn.safetensors** (9.79 GB) from Hugging Face (e.g., `comfyanonymous/flux_text_encoders` repository)
- Place in `models/text_encoders/` folder

The text encoders will be used by ComfyUI for both the image and video stages, ensuring the AI fully grasps the nuances of your descriptions.

### 4. (Optional) Manual CLIP Installation

While ComfyUI Manager handles CLIP installation automatically, you can manually install it if needed. The Flux model uses an OpenCLIP text encoder (`clip_l` for ViT-L/14). If you see errors about missing CLIP models and prefer manual installation:

- Download **clip_l.safetensors** (~500 MB) from Hugging Face
- Place in `models/clip/` folder

Note: Most likely you won't need this manual step if:
1. You're using ComfyUI Manager (recommended)
2. Using the pruned FP8 checkpoint which is all-in-one (AIO)

### Placing the Model Files in ComfyUI

Now that we have the files, we need to put them where ComfyUI can find them. ComfyUI organizes models in a **`models/`** directory, with subfolders for different model types. If you used ComfyUI Desktop, it likely created this structure for you. We need to locate it:

- **Find the ComfyUI "models" folder:** If you're using ComfyUI Desktop, the location can vary. A quick way: in the ComfyUI interface, click on the **"Manager"** button on the top toolbar, then look for an option or info about "Custom Nodes or Models directory". If not obvious, you can use your OS search:
  - On Windows, if you installed for a single user, the models folder might be in `%LOCALAPPDATA%\ComfyUI\pc` or within the installation directory (e.g., `C:\Program Files\ComfyUI\models\`). If you see folders like `checkpoints`, `vae`, `clip`, etc., you're in the right place.
  - On Mac, ComfyUI Desktop typically stores models in `~/Library/Application Support/ComfyUI/` or within the app container. Easiest way: use Finder's Go->Go to Folder and enter `~/Library/Application Support/ComfyUI/` and look for a `models` folder. If not, it might be inside the app bundle (which is complex). Alternatively, upon first run, ComfyUI might have asked where to import models. If you have a `ComfyUI` folder in your home directory, check there too.

Once you find the `models` directory, proceed to place the files:

- **Flux model:** Copy the `*.safetensors` file for RedCraft/Flux into `models/checkpoints/`. (Create the `checkpoints` folder if it doesn't exist.) ComfyUI treats this like a standard Stable Diffusion checkpoint ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Download%20the%20Flux1%20dev%20FP8,checkpoint)). For example, the path might end up as:
  `.../ComfyUI/models/checkpoints/RedCraft-RealReveal5-ULTRA-15Steps-fp8.safetensors`
  (Your file name might differ; that's okay.)

- **LTX model:** Also copy the `ltxv-2b-0.9.6-distilled-04-25.safetensors` file into `models/checkpoints/` ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Download%20ltx,checkpoints)). Essentially, ComfyUI will also load this as a "checkpoint" model (even though it's for video). If you want, you can separate it by making a subfolder (like `models/checkpoints/video/ltx-video.safetensors`), but it's not necessary.

- **T5 text encoder:** Copy the `t5xxl_fp8_e4m3fn.safetensors` file into `models/text_encoders/` ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=ComfyUI%C2%A0)). (If that folder doesn't exist, create it exactly with that name). This is where ComfyUI looks for additional text encoders. *Important:* Without this, the LTX model may not work or will produce black frames because it can't understand the prompt. So don't skip it!

- **(Optional) CLIP text encoder:** If you downloaded `clip_l.safetensors`, place it into `models/clip/` (or `models/clip_encoders/` depending on ComfyUI version – usually just `clip`). Again, you might not need to do this if the checkpoint is all-in-one. But if you run Flux and get a console error like "Clip model not found", then add this.  ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Step%202%3A%20Download%20the%20CLIP,models))

After organizing these files, your ComfyUI models folder should look something like this:

- `models/checkpoints/`
  - `RedCraft-RealReveal5-ULTRA-15Steps-fp8.safetensors`
  - `ltxv-2b-0.9.6-distilled-04-25.safetensors`
- `models/text_encoders/`
  - `t5xxl_fp8_e4m3fn.safetensors`
- `models/clip/` (if used)
  - `clip_l.safetensors`

[AI Generation Description: A screenshot of a file explorer window showing the ComfyUI models directory structure. The window uses the system's default file explorer theme (light mode). The folder tree is expanded to show the hierarchy, with folder icons and nested indentation. The 'models' folder is the root, with three visible subfolders: 'checkpoints', 'text_encoders', and 'clip'. Each subfolder shows its contents with file icons and complete filenames in a monospace font. File sizes are visible in the size column. The window includes standard UI elements like address bar, navigation buttons, and view options. Style: Clean system UI, clear folder structure visualization.]

Now we have all the pieces in place. Time to build the workflow in ComfyUI and generate our video!

## Step-by-Step Workflow in ComfyUI

Let's break this down into three levels, starting with the simplest approach and building up to more advanced techniques:

### Level 1: Quick Start (Using Pre-made Workflow)

This is the fastest way to get your first AI video:

1. **Get a Ready-to-Use Workflow:**
   - Open ComfyUI
   - Click "Manager" in the top toolbar
   - Go to "Custom Nodes" tab
   - Search for "LTXVideo"
   - Install the extension and restart ComfyUI
   - After restart, click "Load" and select the basic workflow template

2. **Enter Your First Prompts:**
   - For the image prompt, try: "Portrait of a young woman smiling, high quality, detailed"
   - For the video prompt, try: "Camera slowly zooms in on her face, she blinks naturally"

3. **Click Queue and Watch!**

This gives you a working setup in minutes. Once you're comfortable with this, move to Level 2.

### Level 2: Understanding the Building Blocks

Now let's understand how the workflow actually works. We'll create it step by step:

### **Step 1: Generate a Portrait Image with Flux**

First, we'll use the Flux model (RedCraft RealReveal5 ULTRA) to create a vertical portrait.

1. **Load the Flux Model:** In ComfyUI's node menu (right-click on the canvas to open the list of nodes), find **"Checkpoint Loader"** (or it might be called **"Load Checkpoint"** under a Diffusion category). Add that node to the canvas. In its settings (click the node to see options), there's a drop-down to select a model file. Choose the **RedCraft/Flux model** you placed in `checkpoints`. For example, select "*RedCraft RealReveal5 ULTRA…*" from the list. This node will load the model when the workflow runs.

   - *Settings:* Ensure **fp16** or **fp8** mode is correctly set if applicable (ComfyUI usually handles this automatically based on model file). The checkpoint loader will output a "Model" that other nodes can use.

2. **Add a Text Prompt:** We need a node to supply the text prompt for the image. ComfyUI typically uses a **Text Encode** node. Look for **"CLIP Text Encode"** (for SD1.x models) or any **"Text Encoder"** node that corresponds to your model. Since Flux uses a custom text encoder (T5 and possibly OpenCLIP), the exact node might be different. In recent ComfyUI, there's a **"Dual Conditioning"** node or **"Load Text Encoder"** nodes, but to keep it simple: add a **Text Encoder node** (for example, "Clip Text Encode (large)" if available).

   - In the text encoder node's properties, type your **prompt**. For a nice portrait, try something like:
     *"Ultra-detailed close-up portrait photo of a beautiful woman, soft natural lighting, high contrast, 8k realism."*
     (Avoid NSFW terms as some models might be tuned to block them). This prompt will be encoded into embeddings that the diffusion model understands.

   - Optionally add a **Negative Prompt** (some text encoders have a second input for negative prompt). You can use a negative prompt to avoid certain things. A common negative prompt: *"low quality, blurry, distorted, extra limbs"*, etc. RedCraft's example negative prompt included things like "lowres, worst quality, bad anatomy, (etc)" – you can include those to steer the model away from problems ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=Negative%20prompt%3A%20lowres%2C%20worst%20quality%2C,generated%2C%20open%20mouth)). This is optional but can improve output.

3. **Prepare the Image Generation Node (Sampler):** In ComfyUI, the actual image generation happens in a **Sampler** node. This node takes the model, the text conditioning, and generates an image latent. Add a sampler node, likely called **KSampler** or **DiffusionSampler**. ComfyUI has various samplers (Euler, DPM, etc.) built in. After adding it, do the following connections:

   - Connect the **"Model" output** of the Checkpoint Loader to the **"Model" input** of the Sampler node. This gives the sampler our Flux model.
   - Connect the **output of the Text Encode node** (the encoded conditioning) to the **conditioning input** of the Sampler. This input might be labeled like "Cond" or "Positive Conditioning". If there's a separate negative conditioning input, connect the negative prompt output accordingly.
   - We also need to provide an initial latent (noise) to the sampler. Usually, the sampler node in ComfyUI has an input for latent (often if left unconnected, it internally creates noise). To be explicit, we can add a **Noise (Latent) node**. Look for **"Noise"** or **"Empty Latent Image"** node. Add it and set the width to 576 and height to 1024 (our target resolution). Connect its output to the **latent input** of the Sampler (commonly labeled "Latent Image" or similar). This node will generate a random latent as the starting point (pure noise). Alternatively, some workflows use a "Noise seed" but a noise node is simplest.

   Now, configure the sampler node's parameters:
   - **Sampler method:** Choose one of the recommended samplers: *Euler*, *DPM++ 2M*, or *DEIS* were suggested for this model ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)). For example, select **DPM++ 2M** Karras or **Euler a**.
   - **Steps:** Set **15** steps. The model was designed to give good results in ~15 steps ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)) (which is quite low; normally SD models use ~20-30, but Flux is powerful and RedCraft is optimized for fewer steps).
   - **CFG (Classifier-Free Guidance) scale:** Set **CFG = 1** ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)). Yes, just 1 – unusually low, but the authors specifically recommend a very low CFG for this model. (Flux/RedCraft has been trained to follow prompts strongly even at low CFG, higher values may overly constrain it).
   - **Scheduler (Noise schedule):** If available, choose **SGM_uniform** ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)). This is a scheduler that evenly distributes denoising; it was recommended ("SGM_uniform") for this model to get the best results in few steps. If that option isn't present, the default or "simple" scheduler is okay, but SGM_uniform can improve quality.
   - **Seed:** You can leave it random for now or set a numeric seed if you want reproducibility. A fixed seed means you'll get the same image every time (with same prompt and settings). Random will surprise you each run.

4. **Decode the Image (VAE):** The sampler produces a latent representation (basically encoded image). We need to decode it to an actual image we can see. Add a **VAE Decoder** node (often called **"VAEDecode"**). Connect the **latent output** of the Sampler to the **VAE Decoder's input**. Also connect the **Model output** of the Checkpoint Loader to the VAE Decoder's "VAE" input if required. (If using the same checkpoint for VAE, some workflows have a separate Load VAE node. But in many cases, the checkpoint includes a VAE, so the sampler's model output might carry VAE info. If not, add a "Load VAE" node and choose a VAE file – Flux may have a recommended VAE ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Step%203%3A%20Download%20the%20VAE)). The RedCraft model likely uses a standard SD VAE or one provided in Flux VAE; if you have `flux_vae.safetensors`, you can load it. But often simply decoding with a generic SD1.5 VAE is fine for now.)

   The VAE Decoder will output an image (usually as a tensor). We want to preview or save it.

5. **Preview/Save the Image:** Add an **Image Preview** or **Save Image** node. ComfyUI by default might show the final image output in the UI's preview panel if the last node returns an image. But to be sure, add a **Save Image** node and connect the output of the VAE Decoder to it. In Save Image's settings, you can specify a filename or leave it to auto-generate (it will save to ComfyUI's output folder by default). Alternatively, a **Preview** node would just display it without saving. You can do both if you like.

Now the Step 1 graph is complete:

[AI Generation Description: A detailed technical flowchart showing ComfyUI's image generation nodes and connections. Nodes are arranged in a logical flow pattern with clear hierarchy. Each node is a rounded rectangle with a unique color: Text Encoder (purple #9C27B0), Checkpoint Loader (blue #2196F3), Noise Generator (yellow #FFC107), Sampler (green #4CAF50), VAE Decode (orange #FF9800), and Save Image (red #F44336). Connecting arrows are black with white outlines for visibility. Node labels use a clear monospace font. Small icons indicate node types. The background is dark (#212121) with a subtle grid. Style: Technical software interface, high contrast, professional diagram.]

*TextEncode* (prompt) → *Sampler* (with Flux model) → *VAE Decode* → *Image Output*. And *Noise* → *Sampler*, plus the Checkpoint loader feeding into sampler and VAE.

Double-check everything is connected properly.

6. **Run the Image Generation:** In the ComfyUI top bar, click **"Queue"** (some versions might say "Execute" or have a play button ▶️). The workflow will start. Watch the console for any errors. If all goes well, after a short while (a progress bar might appear on the sampler node), you'll get a generated image appearing in the UI!

[Screenshot: ComfyUI interface showing generated portrait with progress bar]

   If you used the example prompt, you should see a portrait of a woman with the described features, in vertical orientation. If it's not to your liking, you can tweak the prompt or try a different seed and queue again. The beauty of ComfyUI is you can iteratively adjust nodes and re-run quickly.

7. **(Optional) Tweak and Improve:** If the image has issues (maybe weird hands, etc.), consider refining the prompt or negative prompt. Flux is pretty good with anatomy, but no model is perfect. You could add terms to negative prompt like "disfigured, extra hands, text, watermark" to avoid those. Also try the different sampler methods (Euler vs DPM++). Euler a may produce slightly sharper results, DPM++ 2M Karras might be smoother. **CFG** 1 is very low – if you feel the image isn't following prompt enough or is too off-track, you could try CFG 2 or 3, but usually the recommendation is 1 to preserve detail. We're following the model's guidelines strictly here ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)).

For now, once you have a nice portrait image, **save it** (if it wasn't auto-saved). We'll use it in the next step. If you used Save Image node, check the output directory (ComfyUI will typically output to `ComfyUI/output` with a timestamped filename). You can also right-click the Save node to open the folder.

*(You could also keep the image in-memory and feed it directly to LTX in one go, but saving it and reusing is simpler to explain.)*

### **Step 2: Animate the Image with LTX Video**

Now for the fun part – animating that still image. We'll set up the LTX video generation nodes.

1. **Load the LTX Model:** Add another **Checkpoint Loader** node (you can copy the first one or add a new one). This time, select the **LTX Video model** (`ltxv-2b-0.9.6-distilled-04-25.safetensors`) in its model selection. This node will load the video diffusion model.

   - If ComfyUI has native support, it might not complain, otherwise ensure you installed the LTX custom nodes. (If the LTX model isn't recognized, you might need to update ComfyUI to the latest version ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=provide%20useful%20tools%20for%20working,can%20be%20found%20%2083)), as LTX support was added in core around version 0.3.** and also install the **ComfyUI-LTXVideo** extension via the Manager. We'll cover installing extensions in a moment if needed.)

2. **Prepare the Initial Frame (our image):** We need to feed the Stage 1 image into LTX as the starting frame. Add an **Image Loader** node (called **"Load Image"**). In its settings, browse and select the portrait image file we got from step 1 (e.g., the saved PNG). Alternatively, if you kept everything in one workflow, you could directly connect the output image from VAE to the LTX pipeline, but using a Load Image node is straightforward. Once loaded, this node will output the image.

3. **Encode the Image to Latent:** LTX works in latent space (like Stable Diffusion). So we must encode our loaded image into a latent representation. Add a **VAE Encode Image** node. Connect the **output of the Load Image node** to this VAE Encode's input. Also connect the **LTX Checkpoint Loader's model** output to this VAE Encode's "VAE" input (if it requires a VAE). If the LTX model safetensors includes a VAE, it might use that; otherwise using the same VAE as the initial image's model (Flux's VAE) is fine because they're both SD-based. In many cases, the default SD1.5 VAE is used for LTX as well. This VAE Encode node will output a **latent** frame (the starting frame latent).

4. **Motion Prompt (Text) for Video:** Now add another **Text Encode** node (or a prompt node specifically for LTX if provided by extension). This will be the description of the video motion and any scene details. Write a prompt that **describes what happens over the next few seconds** and also matches the content of the image. It's important to *match the image* so the model knows what it's animating ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Step%205%3A%20Revise%20the%20prompt)). For example, if your image is a woman in a sunny garden, your video prompt should mention that context, then describe motion:

   *Example motion prompt:* *"a close-up portrait of a young woman in a sunny garden, slight camera movement; slowly pan the camera upward from her torso to her face, her hair swaying gently in a breeze. The lighting is warm and natural, likely from the setting sun, casting a soft glow on the scene. The scene appears to be real-life footage."*

   This prompt contains the scene (so LTX knows it's a woman in a garden) and the motion (pan upward, hair swaying). LTX works better with **long descriptive prompts** ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Step%205%3A%20Revise%20the%20prompt)), so don't be shy to include detail. You can even ask ChatGPT or similar to expand a simple motion idea into a vivid description (as a fun tip from LTX docs ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=uploaded%20image%20and%20describe%20what,in%20the%20next%204%20seconds))).

   You might also use a negative prompt here (to avoid janky artifacts between frames – e.g. "low quality, flicker, glitch"). If the Text Encode node supports negative, use it similarly as before.

5. **Set up the LTX Video Sampler:** Now, this part depends on the custom nodes from the LTX extension. Typically, after encoding the initial frame and preparing the prompt, we need a node that **generates a series of frames**. In some LTX example workflows, this is done by a custom node called **"LTX Recurrent Scheduler"** or **"LTX Video Diffusion"**. The exact node name might be different, but conceptually:

   - Add the **LTX video generation node** (look for something like *"LTXVideo Diffuser"* or check under a "LTX" category if the extension is installed). If you don't see any, you may need to install the LTXVideo extension: Click **Manager > Install Custom Nodes**, search for **"LTXVideo"** and install ([LTX Video - New Open Source Video Model with ComfyUI Workflows](https://www.reddit.com/r/StableDiffusion/comments/1gx9mv3/ltx_video_new_open_source_video_model_with/#:~:text=Update%20to%20the%20latest%20version,v0.9.safetensors%20into)). After a restart, you should have nodes for LTX.

   - Once you have it, place the LTX video node and connect:
     - **Model:** Connect the output of the LTX Checkpoint Loader to the model input of this node.
     - **Initial Frame:** Connect the encoded latent from step 3 (VAE Encode output) to the initial frame input.
     - **Text Conditioning:** Connect the output of the motion Text Encode to the conditioning input of the LTX node (likely labeled similarly to the image sampler's conditioning).

   - Configure the LTX node's parameters:
     - **Resolution:** Set to **768×512** pixels - this is the optimal resolution where the model can generate videos faster than real-time playback.
     - **FPS:** The model is optimized for **24 FPS** output, providing smooth, cinematic motion.
     - **Number of Frames:** The model supports up to **129 frames**, allowing for longer sequences up to 5.4 seconds. For testing, you might start with fewer frames and work up to the full length.
     - **Steps per Frame:** Use **8 diffusion steps per frame** with the 0.9.6 distilled model - this is optimized for the best balance of speed and quality.
     - **CFG Scale:** For LTX, something like **7–8** is typical (this is separate from the image CFG). Some LTX example flows use multiple CFG values through advanced schedulers, but to keep simple, try CFG ~7.
     - **Noise Schedule / Strength:** Some nodes might ask how strongly to deviate from the initial image each frame. Usually, leaving default or moderate values is fine. The model will try to keep things coherent.

   This LTX node will generate the series of latents for each frame of the video. Essentially it runs a diffusion process for each frame, conditioning on the previous frame's output so that frames are related (hence "recurrent").

6. **Decode and Combine Frames into Video:** After the LTX node, you will have multiple latents (one per frame). We need to decode them to images and then combine into an actual video file. There are a couple ways:

   - **Using a Video Combine node:** If you installed the **ComfyUI-VideoHelperSuite** or similar extension (which often is needed, and the LTX example workflows mention "VideoCombine" node ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=Example%20workflows))), you should have a node called **"Video Combine"**. This node can take a batch of images and output a video file (e.g. MP4). The LTX node likely outputs a batch of latent images or images. You may need to first decode the batch of latents:
     - Add a **VAE Decode** node that can handle batch (some VAE decode nodes automatically decode batches of latents into a batch of images if you pass all latents at once).
     - Connect the **frames output** of LTX node to the VAE Decode. This should output a list of images.
     - Then add **Video Combine** node. Connect the image batch to it. Set the frame rate in this node (should match the intended FPS, e.g. 12). You can also set output filename (`.mp4`) and quality (CRF value).
     - The Video Combine node will output a video file to your output folder (or a specified path).

   - **Alternative (manual):** If you don't have a VideoCombine node, ComfyUI will at least display or allow saving of individual frames. You could use a **Save Image** node on the batch of images (it will save them as frame_001.png, frame_002.png, etc.). Then you can use an external tool like `ffmpeg` to encode those PNGs into an MP4. This requires extra steps, so using the extension node is easier for beginners.

   If you see **red nodes or errors** about missing nodes at this stage, it's likely you need to install the custom node extensions:
   - Go to **Manager > Install Missing Custom Nodes** (ComfyUI might have a button that automatically fetches any nodes referenced in a loaded workflow, for example) ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Step%203%3A%20Install%20missing%20nodes)).
   - Specifically search and install **"LTXVideo"** (for the LTX nodes) ([LTX Video - New Open Source Video Model with ComfyUI Workflows](https://www.reddit.com/r/StableDiffusion/comments/1gx9mv3/ltx_video_new_open_source_video_model_with/#:~:text=LTX%20Video%20,v0.9.safetensors%20into)) and **"VideoHelperSuite"** or **"Video Nodes"** for the combine node. Once installed, restart ComfyUI and rebuild the connections if needed.

Now the Step 2 part of the graph is done. Here's how the nodes connect:

[AI Generation Description: A professional flowchart diagram illustrating the video generation pipeline. Elements are arranged in a logical left-to-right flow with clear connections. Nodes are represented as rounded rectangles in different colors: Input nodes (green #4CAF50), Processing nodes (blue #2196F3), and Output nodes (orange #FF9800). Arrows between nodes are solid black lines with directional arrowheads. Each node is labeled with clear, white text. The background is light gray (#F5F5F5) with a subtle grid. Small icons represent different operations (e.g., video camera for Video Combine, play button for Output). Style: Technical diagram, clean vector graphics, professional infographic design.]

7. **Run the Video Generation:** Ensure the Step 2 nodes are all connected properly. Click **Queue** again to run this part. If you left the image generation nodes in the same workflow and still connected, the entire thing will run from scratch (doing image and video). To avoid re-generating the image each time, you can *disable* the image part or simply start a new workflow for step 2, loading the saved image. If doing it separately, just ensure only the LTX part is queued.

   As it runs, you'll see the model loading (it might take a moment to load the 2B LTX model into VRAM) and then it will iterate through frames. This might appear as multiple sampler steps in the console or just a progress bar. After it finishes, check your output:
   - If using Video Combine, look for the output video file (e.g., `ComfyUI/output/video.mp4`).
   - If saving frames, you'll see a sequence of images in the output folder.
   - ComfyUI might also show a grid of the generated frames in the UI's preview.

   Open the video or image sequence and watch your AI-generated clip! With luck, you'll see your portrait come to life: maybe the camera moves upward, and her hair gently moves, as per the prompt. It can be mesmerizing to see a once-static image gain a bit of motion.

8. **Adjust and Refine:** If the video looks odd (common issues include a "breathing" effect where the AI slightly changes details back-and-forth), you can tweak:
   - Use a more detailed or constrained prompt to keep things stable (e.g. if her face changed unexpectedly, explicitly say "maintains the same face and expression" in the prompt).
   - If there's flicker, try lowering CFG or using fewer diffusion steps, or add negative prompt terms like "no flicker, no change in background".
   - Try a different type of motion – some motions might be too hard. Camera pans and slight zooms are usually safest. Large object movements can cause more artifacts.
   - Experiment with **frame count** and **FPS**. More frames (longer video) can compound errors, but you might get a slightly longer motion if your GPU can handle it. Fewer frames (like 12) might produce a very short subtle animation that can loop nicely.
   - Also note: The **distilled** LTX model we used prioritizes speed. The full-quality model (non-distilled) might give slightly better quality but needs more steps (like 20 steps/frame) and more VRAM/time. You could try that if you're chasing quality and have the resources.

At this point, you've successfully generated a portrait and animated it with AI – congratulations! Let's move on to Level 3 for those who want to explore more advanced techniques.

### Level 3: Advanced Techniques

Once you're comfortable with the basic workflow, try these advanced techniques to improve your results:

1. **Advanced Node Configurations:**
   - Use the STGGuiderAdvanced node for better motion control
   - Implement frame interpolation for smoother transitions
   - Add ControlNet nodes for precise motion guidance
   - Experiment with custom VAE configurations

2. **Multi-Stage Processing:**
   - Generate intermediate frames for complex movements
   - Use frame blending for smoother transitions
   - Implement motion vector guidance
   - Add post-processing effects (color grading, stabilization)

3. **Performance Optimization:**
   - Use model merging techniques
   - Implement efficient batching strategies
   - Optimize VRAM usage with advanced scheduling
   - Fine-tune parameters for speed vs. quality

4. **Quality Improvements:**
   - Use advanced prompt engineering techniques
   - Implement temporal consistency checks
   - Add motion refinement passes
   - Use advanced upscaling techniques

Now you can iterate to produce different videos using any of these three levels, depending on your needs and expertise.

## Example Prompts and Settings

To help inspire you, here are a couple of example prompt combinations (Stage 1 prompt + Stage 2 motion prompt) you can try:

- **Example 1 – Portrait in Nature:**
  **Image Prompt:** *"Cinematic portrait of a 25-year-old woman with long flowing black hair, standing amid a field of sunflowers at golden hour, gentle smile, highly detailed face, natural light, bokeh background. The lighting is warm and natural, likely from the setting sun, casting a soft glow on the scene. The scene appears to be real-life footage."*
  *(Negative: low quality, blurry, deformed, extra arms)*
  Settings: 15 steps, CFG 1, Euler sampler, SGM_uniform scheduler.
  **Motion Prompt:** *"the same young woman standing in a sunflower field at sunset, camera slowly dollying forward towards her face, her hair and the sunflowers gently swaying in the breeze, warm sunlight flickering. The lighting remains consistent throughout, maintaining the golden hour atmosphere. The motion is smooth and cinematic, with the camera movement feeling natural and professional."*
  FPS: 24, Frames: 25, CFG ~7, 8 steps/frame.
  **Expected Result:** A smooth, cinematic push-in camera movement at high quality 24 FPS; background and hair moving subtly as if wind is blowing.

- **Example 2 – Still Life Object:**
  **Image Prompt:** *"A crystal glass filled with water on a table, sunlight refraction, ultra-detailed, realistic photography. The glass is perfectly clear, with intricate facets catching and splitting the light. The scene has a professional studio quality with controlled lighting."*
  Settings: 20 steps, CFG 2 (since it's an object, a bit higher CFG might be okay), DPM++ 2M.
  **Motion Prompt:** *"the crystal glass of water on the table in bright sunlight; camera rotates slowly around the glass, light glinting through the crystal and water; the reflections and refractions moving realistically. The motion is smooth and precise, maintaining perfect focus throughout the rotation. The lighting remains consistent, creating a professional studio-quality look."*
  FPS: 24, Frames: 17, CFG ~7, 8 steps/frame.
  **Expected Result:** A high-quality, smooth camera orbit at 24 FPS; the glass stays perfectly stable while light and reflections change naturally with the movement.

Feel free to mix and match. The key is to have a strong, clear image first, then apply a motion that makes sense for that scene.

## 🔧 Troubleshooting FAQ

> 🚨 **Common Error Quick Reference**
> - Model not found → Check paths in `models/` folder
> - Red nodes → Install missing extensions via Manager
> - Black frames → Verify T5 encoder is installed
> - OOM errors → Reduce resolution or batch size
> - Crashes → Monitor VRAM usage, reduce load

### 🛑 Error Messages and Solutions

**Q: I hit "Queue" but got an error / red error box.**
A: Read the error message carefully. Common issues:
- *Missing model file:* Did you place the model files in the correct folders? If the Checkpoint Loader can't find the model, double-check the filenames and paths. By default, `models/checkpoints` and `models/text_encoders` are loaded. If you named something incorrectly (e.g., forgot ".safetensors"), fix that.
- *Missing custom node:* If you see something like "No such node: LTX*" or "VideoCombine not found", you need to install the extension nodes. Go to **Manager > Custom Nodes** and install the LTX Video extension and any video helper nodes. After installing, restart ComfyUI and try again.
- *Load errors on Mac (MPS issues):* Sometimes you might see messages about MPS or data types. Ensure you're on the latest ComfyUI and that the pruned FP8 model is supported on Mac. As of writing, pruned FP8 models now work on MPS with updated PyTorch. If not, you might try using the full FP16 model version, but that might require more VRAM than the Mac has, leading to needing CPU. If nothing works, you may have to run in CPU mode (very slow) or use a cloud GPU.

### 💾 Memory Management

**Q: The image generation (Flux) is running out of memory (OOM error).**

A: Flux models are memory-intensive. Here's how to handle OOM issues:

1. **Model Optimization**
   - Use FP8 pruned model
   - Try Flux Schnell for lower VRAM usage
   - Consider NF4 quantized version for 6GB cards

2. **Resolution Management**
   - Start with lower resolution
   - Upscale results after generation if needed

3. **System Optimization**
   - Close background applications
   - Use `--lowvram` or `--medvram` flags
   - Monitor VRAM usage with task manager

4. **Alternative Solutions**
   - Try Flux Schnell (4-step distilled model)
   - Use NF4 quantized version for 6GB cards
   - Consider cloud solutions for heavy workloads

### 🎬 Video Generation Issues

**Q: My video output is black / blank frames.**
A: If the output video is just black frames, a few potential causes:
- The text prompt might not have been applied. Make sure the motion Text Encode is properly connected to the LTX node. If it wasn't, the model might not know what to do and output nothing meaningful (though pure black is unusual – usually you'd get noise or something).
- The **t5 text encoder model** wasn't loaded. Black frames can happen if the model didn't get any conditioning. Did you download and place `t5xxl_fp8_e4m3fn.safetensors` in `models/text_encoders`? Without it, the LTX model might not have a text encoder to use. Check the console log when you run LTX – if it says "T5 encoder not found", that's the issue. Put the file in the right place and restart.
- If using negative prompts with certain custom schedulers, sometimes a bug could cause odd outputs. Try a run without negative prompt to isolate the issue.
- It could also be an issue of the initial frame not being fed correctly. If the initial latent is not connected, the model might be generating from pure noise and if something fails, could yield black. Ensure the VAE Encode of the image is actually providing an output. You might test the VAE Encode + VAE Decode on the image alone to verify it reconstructs the input image (should output basically the same image).

**Q: The video has jarring flicker / the subject changes appearance mid-way.**
A: This is a common challenge in AI video. Some tips:
- Use a stronger prompt emphasis on consistency. E.g., add phrases like "the person's face remains the same throughout" or "maintains consistent appearance".
- If flicker is in background details, maybe simplify the background description so it's less likely to introduce random elements.
- Decrease CFG scale for the video model. High CFG can cause the model to "fight itself" each frame, sometimes causing oscillation. Try CFG 5 or 6 instead of 7 or 8.
- If the model supports **frame interpolation or sequence conditioning** (the LTX 0.9.5 added some features), you could explore those advanced nodes. For example, feeding the last frame back in to guide the next (but that's likely happening internally already).
- Another trick: generate a slightly longer video and then drop the first or last few frames which might be more unstable. Sometimes the very start or end frame can be off.
- Ensure you're using the distilled model correctly. If you inadvertently used the full model with only 8 steps, it might be under-processing leading to flicker. The full model needs more steps; the distilled one is okay with 8. Match the model to the step count.

**Q: ComfyUI crashes or closes suddenly.**
A: If it just disappears, it might be running out of system RAM or hitting some fatal error. Check if there's a crash log or run ComfyUI from a terminal to see messages. On Windows, you might see a "Python has stopped working". This could be memory (check if your RAM usage was maxed) or a bug. Try reducing load as above, and ensure you're using the latest ComfyUI version, as many bugs are fixed in updates. Also, running too high resolution video frames can crash some video encoding nodes due to memory – try smaller.

**Q: The final video file won't play or is not created.**
A: If using Video Combine, ensure you gave it a proper file path ending in `.mp4` or `.gif`. Some older versions default to `.webm` or raw. Use `.mp4` for broad compatibility. Also check the console for ffmpeg errors (VideoCombine uses ffmpeg in the back). If it didn't save, maybe the node didn't execute. You might have to connect a dummy output (like an Image Viewer) to force execution, depending on node implementation. If all else fails, save frames and compile externally.

**Q: How can I loop the video seamlessly?**
A: Seamless loops are tricky. One idea: make the last frame similar to the first. LTX 0.9.5 introduced a way to condition the last frame. If you had a way to feed the first frame as also a "target" for the last, you could morph back. Without that, you can try a subtle approach: not too much change overall, so looping isn't too jarring. Sometimes reversing the video and concatenating can create a boomerang effect that loops. This is more of a creative editing trick afterwards.

## Tips for Better Results and Experimentation

- **Craft Detailed Video Prompts:** LTX works best with long, descriptive prompts that include:
  1. **Subject Description:** Clearly describe who/what is in the scene (e.g., "A woman with long brown hair and light skin, wearing a black jacket")
  2. **Scene Context:** Include setting and lighting details (e.g., "warm and natural lighting, likely from the setting sun")
  3. **Camera Movement:** Specify how the camera behaves (e.g., "camera slowly dollying forward", "camera remains stationary")
  4. **Motion Details:** Describe any movement in the scene (e.g., "her hair swaying gently", "waves crashing against rocks")
  5. **Atmosphere:** Add mood and quality indicators (e.g., "the scene appears to be real-life footage", "the lighting is dim, casting soft shadows")

Example prompt template:
*"[Subject description with specific details], [Action/pose], [Setting/location]. [Camera movement/angle]. [Lighting description]. [Motion details]. [Quality/style indicators]."*

Real examples from LTX documentation:
- *"A woman with long brown hair and light skin smiles at another woman with long blonde hair. The woman with brown hair wears a black jacket and has a small, barely noticeable mole on her right cheek. The camera angle is a close-up, focused on the woman with brown hair's face. The lighting is warm and natural, likely from the setting sun, casting a soft glow on the scene. The scene appears to be real-life footage."*
- *"The waves crash against the jagged rocks of the shoreline, sending spray high into the air. The rocks are a dark gray color, with sharp edges and deep crevices. The water is a clear blue-green, with white foam where the waves break against the rocks. The sky is a light gray, with a few white clouds dotting the horizon."*

- **Use Seeds to Your Advantage:** If you find a seed that gives a great image, note it down. Similarly, LTX might allow a seed for noise in the motion (some workflows allow setting a "video seed"). Consistent seeds can reproduce results or allow you to vary one thing at a time. If you want different outcomes, randomize seeds. If you want the *same* general motion on a slightly different image (or vice versa), keep one seed constant and change the other.

- **Leverage Negative Prompts:** Don't forget negative prompts in both stages. They can be powerful in removing unwanted artifacts. Common negatives for portraits: *"blurry, duplicate face, text, watermark, deformed, extra finger, mutated"*. For video: *"flicker, jump cut, glitch, distortion"* might help (no guarantee the model understands all those, but it might).

- **Play with Schedules and Advanced Nodes:** Once you get comfortable, you can explore advanced ComfyUI nodes like **STG (Sigma Threshold Gradient) or CFG schedules**. The LTX extension mentioned an "STGGuiderAdvanced" which can vary CFG over diffusion steps. These are more technical, but can improve quality if tuned. For example, high CFG in early steps and lower in later steps might reduce flicker.

- **Resolution Upscaling:** If you got a great result at low res, you can try to upscale the final video frames. You could use an AI upscaler frame by frame (like ESRGAN or CodeFormer via ComfyUI nodes, or an external tool). There's no built-in video upscaler in ComfyUI, but you can save frames, upscale them as a batch, then recombine. This is extra work but can yield sharper videos.

- **Try Text-to-Video Directly:** LTX can also generate video purely from text (no initial image)

- **Use Community Workflows:** There are many ready ComfyUI workflows shared on forums (like on r/ComfyUI or the ComfyUI Examples page).

- **Keep an eye on VRAM usage:** ComfyUI doesn't always show VRAM usage, but you can monitor with tools (Nvidia-SMI on Windows, Activity Monitor on Mac). If you're close to the limit, smaller changes could push you over. Knowing your limits helps (e.g., if 1024x1024 is too much, stick to 768x768 etc.).

- **Document your workflow:** Once you have a working node setup, save the workflow (`File > Save Workflow` in ComfyUI). This lets you easily reuse it without rebuilding. You can create different workflows for different types of videos.

- **Patience and Iteration:** As a maker, you know iteration is key. Don't be discouraged if the first video is meh. Treat it as a draft. Maybe the lighting changed weirdly – then you add "consistent lighting" to the prompt. Maybe the motion wasn't noticeable – make it a bit more extreme or add more frames. Each iteration teaches you something about how the models respond.

## Learn More and Next Steps

You've now got the basics down! Where to go from here:

- **ComfyUI GitHub and Wiki:** The [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI) is a great place to check for updates (new versions often add features or performance improvements). The Wiki (like comfyui-wiki.com) has a wealth of tutorials and a **FAQ** for common questions. For example, you can learn about different samplers, using ControlNets, or other advanced models in ComfyUI.

- **YouTube Tutorials:** Search YouTube for *"ComfyUI Flux tutorial"* or *"ComfyUI LTX video guide"*. There are many community-made videos. Some YouTubers show their node setups which can be enlightening. Seeing someone build a workflow can solidify your understanding. Also, tutorials on general ComfyUI usage (like making an animation with **AnimateDiff** or using **ControlNet for depth** in videos) could give you new tools to add to your pipeline.

- **Reddit and Discord:** The r/ComfyUI subreddit is active with people sharing workflows, problems, and art. If you run into unique issues, a search there might find someone who had the same trouble. Also, ComfyUI has an official Discord where you can ask questions in real-time and get help or just show off your results. The community is quite helpful to newcomers.

- **Try Other Extensions:** Once comfortable, you could install other ComfyUI extensions for more capabilities:
  - **ControlNet Nodes:** to guide images/video with sketches or depth maps.
  - **Upscalers and Post-processing:** nodes like ESRGAN upscaler, GIF export nodes, etc., to further polish your outputs.

Finally, approach this as a fun creative process. We now have the ability to create little AI cinematography pieces from our imagination – something that still blows my mind! Tweak prompts, try different subjects (not just people – landscapes, objects, even abstract patterns), and see what motion brings them to life.

Enjoy your journey in AI video generation. I hope this guide served as a helpful playbook to get you started. Now go create some cool stuff! 😃


