---
title: "Index"
subtitle: ""
date: 2025-04-30T04:48:17+02:00
lastmod: 2025-04-30T04:48:17+02:00
draft: true
authors: []
description: ""

tags: []
categories: []
series: []

hiddenFromHomePage: false
hiddenFromSearch: false

featuredImage: ""
featuredImagePreview: ""

toc:
  enable: true
math:
  enable: false
lightgallery: false
license: ""
---

<!--more-->

*Learn how to turn a text prompt into a vertical TikTok-style AI video using **ComfyUI**, the **Flux** image model, and **LTX Video** – all without coding. We’ll start by generating a portrait image and then animate it into a short video. This guide is written by an AI enthusiast in a casual, hands-on style, so let’s dive in!*

## What is ComfyUI, Flux, and LTX Video?

**ComfyUI** is a powerful, node-based graphical interface for Stable Diffusion image generation ([Beginner's Guide to ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/comfyui/#:~:text=What%20is%20ComfyUI%3F)). Instead of writing code, you visually connect **blocks (nodes)** to build an AI pipeline. For example, one node loads an AI model, another takes your text prompt, another generates an image, etc. You chain these nodes to create workflows for images or even videos. It’s like building a flowchart that produces art!

**Flux** is a family of high-quality text-to-image diffusion models developed by Black Forest Labs ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Flux%20is%20a%20family%20of,SDXL%20%20and%20%2021)). As of late 2024, Flux models are considered some of the best open-source image models, often surpassing even Stable Diffusion XL in quality ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Flux%20is%20a%20family%20of,SDXL%20%20and%20%2021)). In simple terms, Flux is the AI “brain” we’ll use to generate a stunning portrait from your text prompt. (Flux was used to train specialized models like *RedCraft RealReveal5 ULTRA*, known for realistic portraits.)

**LTX Video** is an open-source *text-to-video* diffusion model developed by Lightricks. It takes an image (or text) and generates a short video clip by imagining motion ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=LTX%20Video%200,time%2C%20but%20very%20close)). LTX is optimized for speed – for instance, version 0.9.5 could render a 4-second video in ~17 seconds on an RTX 4090 ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=LTX%20Video%200,time%2C%20but%20very%20close)). It’s not magic movie maker – think of it as adding subtle motion (camera movements, slight subject movements, etc.) to a still image. We’ll use LTX to animate the image created by Flux.

**How they fit together:** First, **Flux** generates a vertical portrait image from a prompt (e.g. a person or scene you describe). Then **LTX Video** takes that image and a “motion prompt” (describing how the camera or subject should move) to produce a series of frames – in other words, a short video. ComfyUI is the glue that lets us run Flux and LTX in one workflow: the output of the image generation nodes will feed into the video generation nodes. Essentially, **text → image → video** all within ComfyUI, using Flux and LTX under the hood.

## How Does Text Become a Video?

At a high level, the process works in two stages:

- **Stage 1: Text-to-Image (Flux)** – You write a text prompt describing the portrait or scene you want. ComfyUI feeds this prompt into the Flux model, which diffuses random noise into an image that matches your description. This is done via a neural network that has learned to generate images from text. The result is a single AI-generated **portrait image** (we’ll make it vertical format for TikTok). *Example:* Prompt: *“A serene portrait of a young woman in sunlight, highly detailed.”* → Flux model → **[resulting portrait image]*.

- **Stage 2: Image-to-Video (LTX)** – Now take the image from Stage 1 and feed it, along with a **motion prompt**, into the LTX Video model. LTX generates additional frames as if the scene in the image is moving or the camera is moving. It does this by diffusing noise into new images while trying to stay consistent with the original picture. Essentially, it treats the Stage 1 image as the starting frame of a video, then creates subsequent frames based on your motion description. *Example:* Motion prompt: *“slowly pan the camera upward with a gentle breeze rustling her hair.”* → LTX model → **[sequence of video frames]*.

ComfyUI links these stages, so after Stage 1 finishes, Stage 2 can use the output automatically. The end result is a short video (several seconds long) where the initial AI image comes to life. You might see the camera zoom or pan, the subject’s expression change slightly, or environmental movement, depending on your motion prompt. It’s like those Harry Potter photos – still images that move a bit!

## What to Expect (and What *Not* to Expect)

Before we get into the nuts and bolts, let’s set realistic expectations:

- **Video Length & Quality:** The videos will be **very short** (on the order of 1–2 seconds, e.g. ~16–24 frames at 12–15 FPS). The idea is to produce a cool animated *moment* or looping clip, not a full movie. Quality can be surprisingly good for small motions and camera pans. For example, a gentle pan or the subject blinking can look natural. However, complex movements (like running, or multiple subjects interacting) will **not** look realistic – the model isn’t that advanced yet.

- **Speed:** Don’t expect real-time video rendering on typical hardware. Flux image generation might take several seconds per image (especially on higher resolutions or if your GPU is modest). LTX Video generation will take some seconds more to produce multiple frames. On a high-end GPU (e.g. Nvidia RTX 3080/4090), the process is quite fast – a few seconds for an image and perhaps 20–30 seconds for a short video ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=LTX%20Video%200,time%2C%20but%20very%20close)). On lower-end hardware (or Apple M1/M2), it will be slower (possibly a few minutes total). Still, this is *way faster* than traditional video rendering or earlier AI video models.

- **Realism Limits:** The output video is essentially a series of AI-generated images, so you might see minor flicker or differences frame to frame (the model works to keep them consistent, but it’s not perfect). The motions will be subtle. For instance, you can create a slow camera pan, slight subject movements (like a head turn or smile), or environmental effects (like leaves trembling). It excels at **small, smooth changes**. If you try something extreme (like “she starts dancing wildly”), the result will likely be strange or glitchy. **Don’t expect** the kind of coherence you’d get from a real video camera – think of it more like a moving painting.

- **Resolution:** We’ll use **576×1024** pixels (a vertical 9:16 aspect ratio) as an example. This is a decent resolution for preview/TikTok. Higher resolutions (e.g. 1080p) are possible but will be slower and may require a beefy GPU with lots of VRAM. It’s best to start smaller.

- **One scene only:** LTX does not *create new content per frame*; it transforms the given image. So if your image is a person standing, the video will be that same person – they won’t suddenly change clothes or location (unless your motion prompt somehow forces a change, but that often just yields artifacts). It’s essentially **the same scene with slight motion**. This is great for cinematic camera moves or a bit of life in a portrait, but not for storyboarding multi-scene sequences.

In short, **expect** a short, artsy moving portrait with mild motion. **Don’t expect** a full dynamic action sequence or a perfectly stable video on the first try. Part of the fun is experimenting and seeing what the AI can do within these limits!

## Requirements: Hardware and Software

Let’s make sure you have the right setup before we proceed.

**Operating System:** You can do this on **Windows or macOS**. (Linux works too, but this guide focuses on Win/Mac.) On Windows, you’ll need an **NVIDIA GPU** for GPU acceleration ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)). On macOS, you’ll need an **Apple Silicon** Mac (M1, M2, M3 chips) ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)) – the Desktop version of ComfyUI doesn’t support Intel Macs, and Apple Silicon provides the needed ML acceleration (Metal Performance Shaders).

**GPU and VRAM:** For Windows/NVIDIA users, a GPU with at least **8 GB VRAM** is recommended. 12GB+ will allow higher resolution and more frames. (Flux and LTX are heavy models; Flux’s all-in-one FP8 model is ~11 GB on disk and typically wants ~16 GB VRAM to run comfortably ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=You%20need%2016%20GB%20of,VRAM%20to%20run%20this%20workflow)) ([Flux Model Resource Collection | ComfyUI Wiki](https://comfyui-wiki.com/en/resource/flux#:~:text=Version%20Name%20License%20VRAM%20Requirement,0%2012GB%2BDownloadLightweight%20commercial%20version)), but it can work on 8–12 GB with optimizations or lower resolution.) For macOS M1/M2 users, at least **16 GB unified memory** is recommended (32 GB is better). Macs use the GPU integrated in the chip – it can run these models, but slower. Be prepared for longer generation times on Mac compared to a high-end PC GPU. If you have no dedicated GPU (and only a CPU), it’s technically possible to run ComfyUI, but it will be **extremely slow** (minutes per frame); this guide assumes you have some GPU capability.

**RAM and Disk:** Ensure you have sufficient disk space – the models are large (the Flux model ~11 GB, LTX model ~ >2 GB, plus another ~10 GB for a text encoder file). RAM isn’t usually a bottleneck beyond what’s needed to load models into VRAM, but having 16 GB+ system RAM is a good idea.

**Software:** We will use **ComfyUI Desktop** (the easy installer version). ComfyUI will handle all the heavy lifting (no need to install Python environments manually unless you want to). We’ll also use ComfyUI’s built-in **Manager** to install the needed **custom nodes** (the LTX extension, etc.). No coding required – just some downloads and clicking.

**Summary:**

- **Windows + NVIDIA GPU** (8GB+ VRAM, Windows 10/11) – Supported (ComfyUI Desktop for Windows) ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)).
- **macOS + Apple Silicon (M1/M2)** (16GB+ recommended) – Supported (ComfyUI Desktop for Mac) ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)).
- **macOS Intel or Windows with AMD GPU** – *Not directly supported by ComfyUI Desktop.* You would need to use the ComfyUI source/CLI with relevant hacks (beyond this guide). It’s possible via PlaidML or CPU, but not beginner-friendly.
- **Storage** – ~25 GB free for models/files.
- **Internet** – needed to download models and ComfyUI, but generation itself runs locally.

Now that we have what we need, let’s get everything set up.

## Installation: ComfyUI Desktop

ComfyUI Desktop is the easiest way to get up and running. It packages ComfyUI with a one-click installer and manages all the Python dependencies for you ([MacOS Desktop Version - ComfyUI](https://docs.comfy.org/installation/desktop/macos#:~:text=ComfyUI%20Desktop%20is%20a%20standalone,settings%2C%20models%2C%20workflows%2C%20and%20files)). No need to use the command line (unless you want to).

### Windows Installation (ComfyUI Desktop)

1. **Download ComfyUI for Windows:** Go to the official [ComfyUI download page](https://comfy.org/download) and click **“Download Windows (NVIDIA) Beta”** ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=Download%20Windows%20)). This will download an installer (or a zip/executable). The Windows version requires an NVIDIA graphics card (CUDA support) ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=For%20Mac%3A%20Requires%20Apple%20Silicon)).
2. **Run the Installer:** Launch the installer and follow the prompts. It will install ComfyUI like a regular program. If it’s a zip, unzip it to a folder of your choice (e.g. `C:\ComfyUI\`). The installer will also fetch needed dependencies (it may download PyTorch, etc., which can be a few GB, so be patient).
3. **Launch ComfyUI:** After installation, run **ComfyUI**. You might see a console window and then a GUI. On first run, ComfyUI Desktop may present a setup screen – just proceed with default settings unless you have a previous ComfyUI install to import. It will set up the environment automatically ([MacOS Desktop Version - ComfyUI](https://docs.comfy.org/installation/desktop/macos#:~:text=ComfyUI%20Desktop%20is%20a%20standalone,settings%2C%20models%2C%20workflows%2C%20and%20files)). Once done, you should see the ComfyUI interface: a blank canvas area, a top menu/toolbar (with buttons like *Manager*, *Load*, *Save*, *Queue* etc.), and maybe a preview panel. Congrats, you have ComfyUI running!
4. **(Optional) Verify GPU:** ComfyUI usually auto-detects your GPU. You can check the console log for something like “Using device cuda” or check in the ComfyUI *Manager > Settings* if there’s a device option. By default it will use your NVIDIA GPU.

### macOS Installation (ComfyUI Desktop)

1. **Download ComfyUI for Mac:** On the [ComfyUI download page](https://comfy.org/download), click **“Download Mac (Apple Silicon) Beta”** ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=Download%20Windows%20)). You will get a disk image (`.dmg`) or zip for the ComfyUI Desktop app. (Make sure you have an M1/M2 Mac; the app is Apple Silicon only ([MacOS Desktop Version - ComfyUI](https://docs.comfy.org/installation/desktop/macos#:~:text=ComfyUI%20Desktop%20,Apple%20Silicon)).)
2. **Install the App:** Open the downloaded `.dmg` file. You should see a window instructing you to drag **ComfyUI** into your Applications folder ([MacOS Desktop Version - ComfyUI](https://docs.comfy.org/installation/desktop/macos#:~:text=ComfyUI%20Desktop%20Installation%20Steps)). Do the drag-drop to Applications.
3. **First Launch:** Navigate to your Applications, find **ComfyUI**, and open it. The first time, you might need to right-click and choose “Open” (to bypass Gatekeeper since it’s from an unidentified developer) ([MacOS Desktop Version - ComfyUI](https://docs.comfy.org/installation/desktop/macos#:~:text=Double,Applications%20folder%20following%20the%20arrow)). ComfyUI Desktop will then start an **Initialization** process – basically setting up its internal Python environment. Follow any on-screen steps. You might have to allow it to download PyTorch and other libraries (it will do this automatically; it’s a large download, ~15GB, so give it time).
4. **Complete Setup:** After initialization, ComfyUI should open its main window. On Mac, it might open a browser pointing to a local web UI (earlier versions of ComfyUI were browser-based). Newer Desktop versions have their own window. Either way, you should see the node editor interface. If prompted about analytics or updates, you can opt in or out.
5. **MPS Acceleration:** ComfyUI on Mac will use Apple’s Metal Performance Shaders (MPS) backend via PyTorch for GPU acceleration. This is automatic. Just note that on first run, PyTorch may compile certain kernels which could make the first generation slower. Subsequent runs get faster.

### Optional: ComfyUI via CLI (Advanced Users)

If you prefer not to use the Desktop app or want more control (or if you’re on an unsupported system like Linux or need AMD support), you can install ComfyUI manually:

- **Install from GitHub:** ComfyUI is open source. You can get it by cloning the [ComfyUI GitHub repo](https://github.com/comfyanonymous/ComfyUI) ([Download ComfyUI for Windows/Mac](https://www.comfy.org/download#:~:text=OR)). You’ll need Python 3.10+, Git, and do a `pip install -r requirements.txt`. This approach is for the technically inclined and is not covered in detail here, but ComfyUI’s README has instructions. Once installed, you typically run `python main.py` (or a provided `.bat`/`.sh` script) to launch the server and UI.
- **ComfyUI “CLI” mode:** ComfyUI can also be run headless or via command line for automated tasks, but that’s beyond our scope. We’ll stick to the GUI.

For most beginners, **ComfyUI Desktop** is the way to go. It simplifies updates as well (there’s an update button in the UI). Now, with ComfyUI open, let’s get the AI models we need.

## Downloading the Models (Flux and LTX)

We need to download two model files: the *Flux model* (for image generation) and the *LTX Video model* (for video generation). We’ll also grab a necessary **text encoder** file for LTX (and Flux) to understand prompts properly.

### 1. Flux Model – “RedCraft RealReveal5 ULTRA” (Flux-based)

Flux.1 is the core model, but here we’ll use a specialized **Flux checkpoint** that’s good for portraits. The creators of RedCraft RealReveal5 ULTRA (a Flux-based model) provided a ready-to-use safetensor file. Download it from Civitai using this link:

- **Flux model download:** [RedCraft RealReveal5 ULTRA (Flux, FP8, pruned) – safetensors, ~11GB】 ([RedCraft | 红潮 CADS | UPdated-Apr28 | Commercial & Advertising Design System - Reveal5[SFW]ULTRA | Flux Checkpoint | Civitai](https://civitai.green/models/958009/redcraft-or-cads-or-updated-apr15-or-commercial-and-advertising-design-system?modelVersionId=1576605#:~:text=Download%20%2811)) ([RedCraft | 红潮 CADS | UPdated-Apr28 | Commercial & Advertising Design System - Reveal5[SFW]ULTRA | Flux Checkpoint | Civitai](https://civitai.green/models/958009/redcraft-or-cads-or-updated-apr15-or-commercial-and-advertising-design-system?modelVersionId=1576605#:~:text=2%20Files)). (**Tip:** If clicking a direct download link doesn’t work in browser, you may copy it or use the Civitai page. On the Civitai page, look for a download button showing ~11.08 GB ([RedCraft | 红潮 CADS | UPdated-Apr28 | Commercial & Advertising Design System - Reveal5[SFW]ULTRA | Flux Checkpoint | Civitai](https://civitai.green/models/958009/redcraft-or-cads-or-updated-apr15-or-commercial-and-advertising-design-system?modelVersionId=1576605#:~:text=Download%20%2811)).)

Save this `.safetensors` file to a location you can find. (It might be named along the lines of `RedCraft_RealReveal5_ULTRA_15Steps_fp8_pruned.safetensors` – that’s just an example.)

### 2. LTX Video Model

Next, get the LTX model weights:

- **LTX model download:** Download **ltxv-2b-0.9.6-distilled-04-25.safetensors** from [Hugging Face – Lightricks LTX-Video repo】 ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=17,%E2%AD%90)). The file is around 2–3 GB. (This is the “0.9.6 distilled” version – a lighter, faster version of LTX 0.9.6 requiring only 8 diffusion steps per frame ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=1,Download%20from%20here)), great for quick results).

If you have trouble finding that exact file, you can use the direct link provided (in ComfyUI Manager you could also search for LTXVideo and see if it provides links). Ensure the file is named `ltxv-2b-0.9.6-distilled-04-25.safetensors` (or similar).

### 3. T5 XXL Text Encoder (for prompts)

Both Flux and LTX rely on a large text encoder (T5-XXL) to understand prompts with greater detail. Many Stable Diffusion models use CLIP by default, but Flux and LTX benefit from T5 (which can handle longer, more complex descriptions). We need to download this once:

- **T5 encoder download:** Download **t5xxl_fp16.safetensors** (9.79 GB) ([Lightricks LTX-Video Model | ComfyUI_examples](https://comfyanonymous.github.io/ComfyUI_examples/ltxv/#:~:text=If%20you%20don%E2%80%99t%20have%20it,it%20in%20your%20ComfyUI%2Fmodels%2Ftext_encoders%2F%20folder)) ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=ComfyUI%C2%A0)). This file can be obtained from Hugging Face (for example, from the `comfyanonymous/flux_text_encoders` repository ([RedCraft | 红潮 CADS | UPdated-Apr28 | Commercial & Advertising Design System - Reveal5[SFW]ULTRA | Flux Checkpoint | Civitai](https://civitai.green/models/958009/redcraft-or-cads-or-updated-apr15-or-commercial-and-advertising-design-system?modelVersionId=1576605#:~:text=If%20you%20don%27t%20have%20them%2C,download%20them%20from%20here)) or other Flux resources). It’s big – about 10 GB. (There are also FP8 or quantized versions, but we’ll stick with FP16 for compatibility unless disk space is an issue).

This T5 model will be used by ComfyUI to encode your text prompts for both the image and video stages, ensuring the AI fully grasps the nuances of your descriptions.

### 4. (Optional) CLIP Encoder (OpenCLIP-Large)

The Flux model can also make use of an OpenCLIP text encoder (`clip_l` for ViT-L/14). In many cases, the all-in-one Flux checkpoint already includes what it needs. If you find any errors about missing CLIP models, you can download **clip_l.safetensors** (the OpenCLIP Large text encoder) and place it similarly to T5. This file is smaller (~500 MB). It’s often included in Flux packages or available on Hugging Face ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Step%202%3A%20Download%20the%20CLIP,models)). Most likely, you won’t need this if using the pruned FP8 checkpoint which is all-in-one (AIO) ([RedCraft | 红潮 CADS | UPdated-Apr28 | Commercial & Advertising Design System - Reveal5[SFW]ULTRA | Flux Checkpoint | Civitai](https://civitai.green/models/958009/redcraft-or-cads-or-updated-apr15-or-commercial-and-advertising-design-system?modelVersionId=1576605#:~:text=The%20versions%20with%20AIO%20,as%20Checkpoint%20or%20Compact%20version)), but keep it in mind for troubleshooting.

### Placing the Model Files in ComfyUI

Now that we have the files, we need to put them where ComfyUI can find them. ComfyUI organizes models in a **`models/`** directory, with subfolders for different model types. If you used ComfyUI Desktop, it likely created this structure for you. We need to locate it:

- **Find the ComfyUI “models” folder:** If you’re using ComfyUI Desktop, the location can vary. A quick way: in the ComfyUI interface, click on the **“Manager”** button on the top toolbar, then look for an option or info about “Custom Nodes or Models directory”. If not obvious, you can use your OS search:
  - On Windows, if you installed for a single user, the models folder might be in `%LOCALAPPDATA%\ComfyUI\pc` or within the installation directory (e.g., `C:\Program Files\ComfyUI\models\`). If you see folders like `checkpoints`, `vae`, `clip`, etc., you’re in the right place.
  - On Mac, ComfyUI Desktop typically stores models in `~/Library/Application Support/ComfyUI/` or within the app container. Easiest way: use Finder’s Go->Go to Folder and enter `~/Library/Application Support/ComfyUI/` and look for a `models` folder. If not, it might be inside the app bundle (which is complex). Alternatively, upon first run, ComfyUI might have asked where to import models. If you have a `ComfyUI` folder in your home directory, check there too.
  - If all else fails, use the search function of your OS for the file `extra_models_config.yaml` (ComfyUI often has this in the config, listing model paths ([MacOS Desktop Version - ComfyUI](https://docs.comfy.org/installation/desktop/macos#:~:text=match%20at%20L399%20extra_models_config,should%20not%20be%20edited%20directly))).

Once you find the `models` directory, proceed to place the files:

- **Flux model:** Copy the `*.safetensors` file for RedCraft/Flux into `models/checkpoints/`. (Create the `checkpoints` folder if it doesn’t exist.) ComfyUI treats this like a standard Stable Diffusion checkpoint ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Download%20the%20Flux1%20dev%20FP8,checkpoint)). For example, the path might end up as:
  `.../ComfyUI/models/checkpoints/RedCraft-RealReveal5-ULTRA-15Steps-fp8.safetensors`
  (Your file name might differ; that’s okay.)

- **LTX model:** Also copy the `ltxv-2b-0.9.6-distilled-04-25.safetensors` file into `models/checkpoints/` ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Download%20ltx,checkpoints)). Essentially, ComfyUI will also load this as a “checkpoint” model (even though it’s for video). If you want, you can separate it by making a subfolder (like `models/checkpoints/video/ltx-video.safetensors`), but it’s not necessary.

- **T5 text encoder:** Copy the `t5xxl_fp16.safetensors` file into `models/text_encoders/` ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=ComfyUI%C2%A0)). (If that folder doesn’t exist, create it exactly with that name). This is where ComfyUI looks for additional text encoders. *Important:* Without this, the LTX model may not work or will produce black frames because it can’t understand the prompt. So don’t skip it!

- **(Optional) CLIP text encoder:** If you downloaded `clip_l.safetensors`, place it into `models/clip/` (or `models/clip_encoders/` depending on ComfyUI version – usually just `clip`). Again, you might not need to do this if the checkpoint is all-in-one. But if you run Flux and get a console error like “Clip model not found”, then add this.  ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Step%202%3A%20Download%20the%20CLIP,models))

After organizing these files, your ComfyUI models folder should look something like this:

- `models/checkpoints/`
  - `RedCraft-RealReveal5-ULTRA-15Steps-fp8.safetensors`
  - `ltxv-2b-0.9.6-distilled-04-25.safetensors`
- `models/text_encoders/`
  - `t5xxl_fp16.safetensors`
- `models/clip/` (if used)
  - `clip_l.safetensors`

**[screenshot of model files in their folders]**

Now we have all the pieces in place. Time to build the workflow in ComfyUI and generate our video!

## Step-by-Step Workflow in ComfyUI

We’ll create a two-part workflow in ComfyUI: **Step 1** generates a portrait image with Flux, and **Step 2** animates that image with LTX. You can do this in one continuous graph or treat them separately. For clarity, we’ll explain them separately, but you can combine them.

*(If you prefer, you can also load pre-made workflows instead of manually adding nodes. The ComfyUI community provides JSON workflow files for Flux and LTX that you can just drag into ComfyUI to populate all nodes. For learning purposes, we’ll outline the manual setup. Feel free to use the Manager’s “Load Workflow” or drag-and-drop a `.json` if you have one, then skip to running it.)*

### **Step 1: Generate a Portrait Image with Flux**

First, we’ll use the Flux model (RedCraft RealReveal5 ULTRA) to create a vertical portrait.

1. **Load the Flux Model:** In ComfyUI’s node menu (right-click on the canvas to open the list of nodes), find **“Checkpoint Loader”** (or it might be called **“Load Checkpoint”** under a Diffusion category). Add that node to the canvas. In its settings (click the node to see options), there’s a drop-down to select a model file. Choose the **RedCraft/Flux model** you placed in `checkpoints`. For example, select “*RedCraft RealReveal5 ULTRA…*” from the list. This node will load the model when the workflow runs.

   - *Settings:* Ensure **fp16** or **fp8** mode is correctly set if applicable (ComfyUI usually handles this automatically based on model file). The checkpoint loader will output a “Model” that other nodes can use.

2. **Add a Text Prompt:** We need a node to supply the text prompt for the image. ComfyUI typically uses a **Text Encode** node. Look for **“CLIP Text Encode”** (for SD1.x models) or any **“Text Encoder”** node that corresponds to your model. Since Flux uses a custom text encoder (T5 and possibly OpenCLIP), the exact node might be different. In recent ComfyUI, there’s a **“Dual Conditioning”** node or **“Load Text Encoder”** nodes, but to keep it simple: add a **Text Encoder node** (for example, “Clip Text Encode (large)” if available).

   - In the text encoder node’s properties, type your **prompt**. For a nice portrait, try something like:
     *“Ultra-detailed close-up portrait photo of a beautiful woman, soft natural lighting, high contrast, 8k realism.”*
     (Avoid NSFW terms as some models might be tuned to block them). This prompt will be encoded into embeddings that the diffusion model understands.

   - Optionally add a **Negative Prompt** (some text encoders have a second input for negative prompt). You can use a negative prompt to avoid certain things. A common negative prompt: *“low quality, blurry, distorted, extra limbs”*, etc. RedCraft’s example negative prompt included things like “lowres, worst quality, bad anatomy, (etc)” – you can include those to steer the model away from problems ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=Negative%20prompt%3A%20lowres%2C%20worst%20quality%2C,generated%2C%20open%20mouth)). This is optional but can improve output.

3. **Prepare the Image Generation Node (Sampler):** In ComfyUI, the actual image generation happens in a **Sampler** node. This node takes the model, the text conditioning, and generates an image latent. Add a sampler node, likely called **KSampler** or **DiffusionSampler**. ComfyUI has various samplers (Euler, DPM, etc.) built in. After adding it, do the following connections:

   - Connect the **“Model” output** of the Checkpoint Loader to the **“Model” input** of the Sampler node. This gives the sampler our Flux model.
   - Connect the **output of the Text Encode node** (the encoded conditioning) to the **conditioning input** of the Sampler. This input might be labeled like “Cond” or “Positive Conditioning”. If there’s a separate negative conditioning input, connect the negative prompt output accordingly.
   - We also need to provide an initial latent (noise) to the sampler. Usually, the sampler node in ComfyUI has an input for latent (often if left unconnected, it internally creates noise). To be explicit, we can add a **Noise (Latent) node**. Look for **“Noise”** or **“Empty Latent Image”** node. Add it and set the width to 576 and height to 1024 (our target resolution). Connect its output to the **latent input** of the Sampler (commonly labeled “Latent Image” or similar). This node will generate a random latent as the starting point (pure noise). Alternatively, some workflows use a “Noise seed” but a noise node is simplest.

   Now, configure the sampler node’s parameters:
   - **Sampler method:** Choose one of the recommended samplers: *Euler*, *DPM++ 2M*, or *DEIS* were suggested for this model ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)). For example, select **DPM++ 2M** Karras or **Euler a**.
   - **Steps:** Set **15** steps. The model was designed to give good results in ~15 steps ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)) (which is quite low; normally SD models use ~20-30, but Flux is powerful and RedCraft is optimized for fewer steps).
   - **CFG (Classifier-Free Guidance) scale:** Set **CFG = 1** ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)). Yes, just 1 – unusually low, but the authors specifically recommend a very low CFG for this model. (Flux/RedCraft has been trained to follow prompts strongly even at low CFG, higher values may overly constrain it).
   - **Scheduler (Noise schedule):** If available, choose **SGM_uniform** ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)). This is a scheduler that evenly distributes denoising; it was recommended (“SGM_uniform”) for this model to get the best results in few steps. If that option isn’t present, the default or “simple” scheduler is okay, but SGM_uniform can improve quality.
   - **Seed:** You can leave it random for now or set a numeric seed if you want reproducibility. A fixed seed means you’ll get the same image every time (with same prompt and settings). Random will surprise you each run.

4. **Decode the Image (VAE):** The sampler produces a latent representation (basically encoded image). We need to decode it to an actual image we can see. Add a **VAE Decoder** node (often called **“VAEDecode”**). Connect the **latent output** of the Sampler to the **VAE Decoder’s input**. Also connect the **Model output** of the Checkpoint Loader to the VAE Decoder’s “VAE” input if required. (If using the same checkpoint for VAE, some workflows have a separate Load VAE node. But in many cases, the checkpoint includes a VAE, so the sampler’s model output might carry VAE info. If not, add a “Load VAE” node and choose a VAE file – Flux may have a recommended VAE ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=Step%203%3A%20Download%20the%20VAE)). The RedCraft model likely uses a standard SD VAE or one provided in Flux VAE; if you have `flux_vae.safetensors`, you can load it. But often simply decoding with a generic SD1.5 VAE is fine for now.)

   The VAE Decoder will output an image (usually as a tensor). We want to preview or save it.

5. **Preview/Save the Image:** Add an **Image Preview** or **Save Image** node. ComfyUI by default might show the final image output in the UI’s preview panel if the last node returns an image. But to be sure, add a **Save Image** node and connect the output of the VAE Decoder to it. In Save Image’s settings, you can specify a filename or leave it to auto-generate (it will save to ComfyUI’s output folder by default). Alternatively, a **Preview** node would just display it without saving. You can do both if you like.

Now the Step 1 graph is complete: **[flowchart of node connections for image generation]**. It should look something like:

*TextEncode* (prompt) → *Sampler* (with Flux model) → *VAE Decode* → *Image Output*. And *Noise* → *Sampler*, plus the Checkpoint loader feeding into sampler and VAE.

Double-check everything is connected properly.

6. **Run the Image Generation:** In the ComfyUI top bar, click **“Queue”** (some versions might say “Execute” or have a play button ▶️). The workflow will start. Watch the console for any errors. If all goes well, after a short while (a progress bar might appear on the sampler node), you’ll get a generated image appearing in the UI! **[result of generation]**

   If you used the example prompt, you should see a portrait of a woman with the described features, in vertical orientation. If it’s not to your liking, you can tweak the prompt or try a different seed and queue again. The beauty of ComfyUI is you can iteratively adjust nodes and re-run quickly.

7. **(Optional) Tweak and Improve:** If the image has issues (maybe weird hands, etc.), consider refining the prompt or negative prompt. Flux is pretty good with anatomy, but no model is perfect. You could add terms to negative prompt like “disfigured, extra hands, text, watermark” to avoid those. Also try the different sampler methods (Euler vs DPM++). Euler a may produce slightly sharper results, DPM++ 2M Karras might be smoother. **CFG** 1 is very low – if you feel the image isn’t following prompt enough or is too off-track, you could try CFG 2 or 3, but usually the recommendation is 1 to preserve detail. We’re following the model’s guidelines strictly here ([RedCarft 亚洲美女模型 - Civitai中文网](https://civitai.me/49143.html#:~:text=RedCraft%20RealReveal5%20ULTRA%C2%A015Steps)).

For now, once you have a nice portrait image, **save it** (if it wasn’t auto-saved). We’ll use it in the next step. If you used Save Image node, check the output directory (ComfyUI will typically output to `ComfyUI/output` with a timestamped filename). You can also right-click the Save node to open the folder.

*(You could also keep the image in-memory and feed it directly to LTX in one go, but saving it and reusing is simpler to explain.)*

### **Step 2: Animate the Image with LTX Video**

Now for the fun part – animating that still image. We’ll set up the LTX video generation nodes.

1. **Load the LTX Model:** Add another **Checkpoint Loader** node (you can copy the first one or add a new one). This time, select the **LTX Video model** (`ltxv-2b-0.9.6-distilled-04-25.safetensors`) in its model selection. This node will load the video diffusion model.

   - If ComfyUI has native support, it might not complain, otherwise ensure you installed the LTX custom nodes. (If the LTX model isn’t recognized, you might need to update ComfyUI to the latest version ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=provide%20useful%20tools%20for%20working,can%20be%20found%20%2083)), as LTX support was added in core around version 0.3.** and also install the **ComfyUI-LTXVideo** extension via the Manager. We’ll cover installing extensions in a moment if needed.)

2. **Prepare the Initial Frame (our image):** We need to feed the Stage 1 image into LTX as the starting frame. Add an **Image Loader** node (called **“Load Image”**). In its settings, browse and select the portrait image file we got from step 1 (e.g., the saved PNG). Alternatively, if you kept everything in one workflow, you could directly connect the output image from VAE to the LTX pipeline, but using a Load Image node is straightforward. Once loaded, this node will output the image.

3. **Encode the Image to Latent:** LTX works in latent space (like Stable Diffusion). So we must encode our loaded image into a latent representation. Add a **VAE Encode Image** node. Connect the **output of the Load Image node** to this VAE Encode’s input. Also connect the **LTX Checkpoint Loader’s model** output to this VAE Encode’s “VAE” input (if it requires a VAE). If the LTX model safetensors includes a VAE, it might use that; otherwise using the same VAE as the initial image’s model (Flux’s VAE) is fine because they’re both SD-based. In many cases, the default SD1.5 VAE is used for LTX as well. This VAE Encode node will output a **latent** frame (the starting frame latent).

4. **Motion Prompt (Text) for Video:** Now add another **Text Encode** node (or a prompt node specifically for LTX if provided by extension). This will be the description of the video motion and any scene details. Write a prompt that **describes what happens over the next few seconds** and also matches the content of the image. It’s important to *match the image* so the model knows what it’s animating ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Step%205%3A%20Revise%20the%20prompt)). For example, if your image is a woman in a sunny garden, your video prompt should mention that context, then describe motion:

   *Example motion prompt:* *“a close-up portrait of a young woman in a sunny garden, slight camera movement; slowly pan the camera upward from her torso to her face, her hair swaying gently in a breeze.”*

   This prompt contains the scene (so LTX knows it’s a woman in a garden) and the motion (pan upward, hair swaying). LTX works better with **long descriptive prompts** ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Step%205%3A%20Revise%20the%20prompt)), so don’t be shy to include detail. You can even ask ChatGPT or similar to expand a simple motion idea into a vivid description (as a fun tip from LTX docs ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=uploaded%20image%20and%20describe%20what,in%20the%20next%204%20seconds))).

   You might also use a negative prompt here (to avoid janky artifacts between frames – e.g. “low quality, flicker, glitch”). If the Text Encode node supports negative, use it similarly as before.

5. **Set up the LTX Video Sampler:** Now, this part depends on the custom nodes from the LTX extension. Typically, after encoding the initial frame and preparing the prompt, we need a node that **generates a series of frames**. In some LTX example workflows, this is done by a custom node called **“LTX Recurrent Scheduler”** or **“LTX Video Diffusion”**. The exact node name might be different, but conceptually:

   - Add the **LTX video generation node** (look for something like *“LTXVideo Diffuser”* or check under a “LTX” category if the extension is installed). If you don’t see any, you may need to install the LTXVideo extension: Click **Manager > Install Custom Nodes**, search for **“LTXVideo”** and install ([LTX Video - New Open Source Video Model with ComfyUI Workflows](https://www.reddit.com/r/StableDiffusion/comments/1gx9mv3/ltx_video_new_open_source_video_model_with/#:~:text=Update%20to%20the%20latest%20version,v0.9.safetensors%20into)). After a restart, you should have nodes for LTX.

   - Once you have it, place the LTX video node and connect:
     - **Model:** Connect the output of the LTX Checkpoint Loader to the model input of this node.
     - **Initial Frame:** Connect the encoded latent from step 3 (VAE Encode output) to the initial frame input.
     - **Text Conditioning:** Connect the output of the motion Text Encode to the conditioning input of the LTX node (likely labeled similarly to the image sampler’s conditioning).

   - Configure the LTX node’s parameters:
     - **Number of Frames:** e.g. **20** frames. This determines how many frames the video will have (not counting the initial one sometimes). 16–24 is a good range as noted, which at ~12 FPS gives ~1.3 to 2 seconds of video.
     - **FPS (frames per second):** Many workflows just output frames, and you can play them at whatever FPS you want. But if the node has an FPS setting for motion consistency, set it to **12** or **15**. (12 FPS will look a bit choppy but is easier for the model; 15 is slightly smoother; you can always interpolate if needed).
     - **Steps per Frame:** LTX 0.9.6 distilled is designed to use only **8 diffusion steps per frame** ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=1,Download%20from%20here)). Ensure it’s set to ~8 (if using the distilled model). If using the full 0.9.6, you might use more steps (and it will be slower).
     - **CFG Scale:** For LTX, something like **7–8** is typical (this is separate from the image CFG). Some LTX example flows use multiple CFG values through advanced schedulers, but to keep simple, try CFG ~7.
     - **Noise Schedule / Strength:** Some nodes might ask how strongly to deviate from the initial image each frame. Usually, leaving default or moderate values is fine. The model will try to keep things coherent.

   This LTX node will generate the series of latents for each frame of the video. Essentially it runs a diffusion process for each frame, conditioning on the previous frame’s output so that frames are related (hence “recurrent”).

6. **Decode and Combine Frames into Video:** After the LTX node, you will have multiple latents (one per frame). We need to decode them to images and then combine into an actual video file. There are a couple ways:

   - **Using a Video Combine node:** If you installed the **ComfyUI-VideoHelperSuite** or similar extension (which often is needed, and the LTX example workflows mention “VideoCombine” node ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=Example%20workflows))), you should have a node called **“Video Combine”**. This node can take a batch of images and output a video file (e.g. MP4). The LTX node likely outputs a batch of latent images or images. You may need to first decode the batch of latents:
     - Add a **VAE Decode** node that can handle batch (some VAE decode nodes automatically decode batches of latents into a batch of images if you pass all latents at once).
     - Connect the **frames output** of LTX node to the VAE Decode. This should output a list of images.
     - Then add **Video Combine** node. Connect the image batch to it. Set the frame rate in this node (should match the intended FPS, e.g. 12). You can also set output filename (`.mp4`) and quality (CRF value).
     - The Video Combine node will output a video file to your output folder (or a specified path).

   - **Alternative (manual):** If you don’t have a VideoCombine node, ComfyUI will at least display or allow saving of individual frames. You could use a **Save Image** node on the batch of images (it will save them as frame_001.png, frame_002.png, etc.). Then you can use an external tool like `ffmpeg` to encode those PNGs into an MP4. This requires extra steps, so using the extension node is easier for beginners.

   If you see **red nodes or errors** about missing nodes at this stage, it’s likely you need to install the custom node extensions:
   - Go to **Manager > Install Missing Custom Nodes** (ComfyUI might have a button that automatically fetches any nodes referenced in a loaded workflow, for example) ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Step%203%3A%20Install%20missing%20nodes)).
   - Specifically search and install **“LTXVideo”** (for the LTX nodes) ([LTX Video - New Open Source Video Model with ComfyUI Workflows](https://www.reddit.com/r/StableDiffusion/comments/1gx9mv3/ltx_video_new_open_source_video_model_with/#:~:text=LTX%20Video%20,v0.9.safetensors%20into)) and **“VideoHelperSuite”** or **“Video Nodes”** for the combine node. Once installed, restart ComfyUI and rebuild the connections if needed.

Now the Step 2 part of the graph is done. It should look like: **[flowchart of node connections for video generation]** – the loaded image goes into VAE encode, then into LTX model along with text, and outputs frames that go through VAE decode and into Video Combine.

7. **Run the Video Generation:** Ensure the Step 2 nodes are all connected properly. Click **Queue** again to run this part. If you left the image generation nodes in the same workflow and still connected, the entire thing will run from scratch (doing image and video). To avoid re-generating the image each time, you can *disable* the image part or simply start a new workflow for step 2, loading the saved image. If doing it separately, just ensure only the LTX part is queued.

   As it runs, you’ll see the model loading (it might take a moment to load the 2B LTX model into VRAM) and then it will iterate through frames. This might appear as multiple sampler steps in the console or just a progress bar. After it finishes, check your output:
   - If using Video Combine, look for the output video file (e.g., `ComfyUI/output/video.mp4`).
   - If saving frames, you’ll see a sequence of images in the output folder.
   - ComfyUI might also show a grid of the generated frames in the UI’s preview.

   Open the video or image sequence and watch your AI-generated clip! With luck, you’ll see your portrait come to life: maybe the camera moves upward, and her hair gently moves, as per the prompt. It can be mesmerizing to see a once-static image gain a bit of motion.

8. **Adjust and Refine:** If the video looks odd (common issues include a “breathing” effect where the AI slightly changes details back-and-forth), you can tweak:
   - Use a more detailed or constrained prompt to keep things stable (e.g. if her face changed unexpectedly, explicitly say “maintains the same face and expression” in the prompt).
   - If there’s flicker, try lowering CFG or using fewer diffusion steps, or add negative prompt terms like “no flicker, no change in background”.
   - Try a different type of motion – some motions might be too hard. Camera pans and slight zooms are usually safest. Large object movements can cause more artifacts.
   - Experiment with **frame count** and **FPS**. More frames (longer video) can compound errors, but you might get a slightly longer motion if your GPU can handle it. Fewer frames (like 12) might produce a very short subtle animation that can loop nicely.
   - Also note: The **distilled** LTX model we used prioritizes speed. The full-quality model (non-distilled) might give slightly better quality but needs more steps (like 20 steps/frame) and more VRAM/time. You could try that if you’re chasing quality and have the resources.

At this point, you’ve successfully generated a portrait and animated it with AI – congratulations! You can now iterate to produce different videos.

## Example Prompts and Settings

To help inspire you, here are a couple of example prompt combinations (Stage 1 prompt + Stage 2 motion prompt) you can try:

- **Example 1 – Portrait in Nature:**
  **Image Prompt:** *“Cinematic portrait of a 25-year-old woman with long flowing black hair, standing amid a field of sunflowers at golden hour, gentle smile, highly detailed face, natural light, bokeh background”*.
  *(Negative: low quality, blurry, deformed, extra arms)*
  Settings: 15 steps, CFG 1, Euler sampler, SGM_uniform scheduler.
  **Motion Prompt:** *“the same young woman standing in a sunflower field at sunset, camera slowly dollying forward towards her face, her hair and the sunflowers gently swaying in the breeze, warm sunlight flickering”*.
  FPS: 12, Frames: 20, CFG ~7, 8 steps/frame.
  **Expected Result:** A slow push-in camera movement; background and hair moving subtly as if wind is blowing.

- **Example 2 – Still Life Object:**
  **Image Prompt:** *“A crystal glass filled with water on a table, sunlight refraction, ultra-detailed, realistic photography”*.
  Settings: 20 steps, CFG 2 (since it’s an object, a bit higher CFG might be okay), DPM++ 2M.
  **Motion Prompt:** *“the crystal glass of water on the table in bright sunlight; camera rotates slowly around the glass, light glinting through the crystal and water; the reflections and refractions moving realistically”*.
  FPS: 15, Frames: 16.
  **Expected Result:** The glass stays the same, but you get a parallax effect as if the camera is orbiting, and the light sparkles change.

Feel free to mix and match. The key is to have a strong, clear image first, then apply a motion that makes sense for that scene.

## Troubleshooting FAQ

**Q: I hit “Queue” but got an error / red error box.**
A: Read the error message carefully. Common issues:
- *Missing model file:* Did you place the model files in the correct folders? If the Checkpoint Loader can’t find the model, double-check the filenames and paths. Make sure ComfyUI’s `extra_models_config.yaml` (if used) includes those folders. By default, `models/checkpoints` and `models/text_encoders` are loaded ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=Download%20ltx,checkpoints)). If you named something incorrectly (e.g., forgot “.safetensors”), fix that.
- *Missing custom node:* If you see something like “No such node: LTX*” or “VideoCombine not found”, you need to install the extension nodes. Go to **Manager > Custom Nodes** and install the LTX Video extension ([LTX Video - New Open Source Video Model with ComfyUI Workflows](https://www.reddit.com/r/StableDiffusion/comments/1gx9mv3/ltx_video_new_open_source_video_model_with/#:~:text=LTX%20Video%20,v0.9.safetensors%20into)) and any video helper nodes. After installing, restart ComfyUI and try again.
- *Load errors on Mac (MPS issues):* Sometimes you might see messages about MPS or data types. Ensure you’re on the latest ComfyUI and that the pruned FP8 model is supported on Mac. As of writing, pruned FP8 models now work on MPS with updated PyTorch ([Flux + ComfyUI on Apple Silicon Macs— 2024 | by Jason Griffin | Medium](https://medium.com/@tchpnk/flux-comfyui-on-apple-silicon-with-hardware-acceleration-2024-4d44ed437179#:~:text=This%20advice%20appears%20to%20come,fp8%29%20version%20instead)). If not, you might try using the full FP16 model version, but that might require more VRAM than the Mac has, leading to needing CPU. If nothing works, you may have to run in CPU mode (very slow) or use a cloud GPU.

**Q: The image generation (Flux) is running out of memory (OOM error).**
A: Flux models are big. If you have a lower VRAM GPU (say 8GB), try these:
- Use the FP8 pruned model (which we did) instead of full FP16 (which would definitely OOM on 8GB). The FP8 model is smaller but still borderline.
- Reduce the resolution. Instead of 576x1024, try 448x768 or even 384x640 to see if it runs, then upscale later if needed.
- Close other programs to free up GPU memory (and system RAM).
- On Windows, you can try running ComfyUI with the `--lowvram` or `--medvram` flags (if available, similar to AUTOMATIC1111) or enable settings in ComfyUI Manager like “disable some optimizations” – but ComfyUI’s defaults are usually optimized already.
- On the software side, if using CLI, you can launch with `--disable-safe-unpickle` or other flags but that’s not relevant here since we use safetensors (safe format).
- If you still OOM, you may need a smaller model. For example, try using **Flux Schnell** (the 4-step distilled model, smaller) ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=The%20Flux%20Schnell%20is%20for,is%20a%20bit%20lower%20quality)). It trades some quality for speed and memory. There’s also an *NF4 quantized* version that can run on 6GB cards ([Flux Model Resource Collection | ComfyUI Wiki](https://comfyui-wiki.com/en/resource/flux#:~:text=Flux%20FP8%20ComfyUI%208GB%2BDev%20%2F,lllyasviel%206GB%2BV2%20VersionRequires%20specific%20plugins)), but that requires a special loader extension (beyond our scope).

**Q: The video generation is super slow or OOM.**
A: Video means multiple images, so it multiplies load.
- If it’s slow but working, consider generating fewer frames (8–12 frames) or at lower resolution for testing. You can also try the non-distilled model if you want quality and don’t mind slow (not recommended on low VRAM though).
- If it OOMs during LTX: perhaps too many frames or too high res. Each frame generation might load a lot into memory. Try 10 frames at 512x912 or so to see if it passes. Also, ensure that after image gen, the big Flux model is not still hogging VRAM. If doing both in one go, both models might be loaded – which definitely can OOM. Instead, do them separately (unload Flux model before loading LTX – ComfyUI might unload automatically once that branch is done, but not sure). Worst case, restart ComfyUI and only load the LTX part with the saved image to ensure Flux isn’t sitting in memory.
- On M1/M2 Mac: the unified memory gets taxed by these large models. There’s not much to do except reduce workload (res, frames, steps). MPS backend also might not be as memory-efficient. Monitor your Activity Monitor memory pressure. If you push it too far, the Mac might start swapping (slowing things dramatically).

**Q: My video output is black / blank frames.**
A: If the output video is just black frames, a few potential causes:
- The text prompt might not have been applied. Make sure the motion Text Encode is properly connected to the LTX node. If it wasn’t, the model might not know what to do and output nothing meaningful (though pure black is unusual – usually you’d get noise or something).
- The **t5 text encoder model** wasn’t loaded. Black frames can happen if the model didn’t get any conditioning. Did you download and place `t5xxl_fp16.safetensors` in `models/text_encoders`? ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=ComfyUI%C2%A0)) Without it, the LTX model might not have a text encoder to use. Check the console log when you run LTX – if it says “T5 encoder not found”, that’s the issue. Put the file in the right place and restart.
- If using negative prompts with certain custom schedulers, sometimes a bug could cause odd outputs. Try a run without negative prompt to isolate the issue.
- It could also be an issue of the initial frame not being fed correctly. If the initial latent is not connected, the model might be generating from pure noise and if something fails, could yield black. Ensure the VAE Encode of the image is actually providing an output. You might test the VAE Encode + VAE Decode on the image alone to verify it reconstructs the input image (should output basically the same image).

**Q: The video has jarring flicker / the subject changes appearance mid-way.**
A: This is a common challenge in AI video. Some tips:
- Use a stronger prompt emphasis on consistency. E.g., add phrases like “the person’s face remains the same throughout” or “maintains consistent appearance”.
- If flicker is in background details, maybe simplify the background description so it’s less likely to introduce random elements.
- Decrease CFG scale for the video model. High CFG can cause the model to “fight itself” each frame, sometimes causing oscillation. Try CFG 5 or 6 instead of 7 or 8.
- If the model supports **frame interpolation or sequence conditioning** (the LTX 0.9.5 added some features ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=1,Commercial%20license%20availability))), you could explore those advanced nodes. For example, feeding the last frame back in to guide the next (but that’s likely happening internally already).
- Another trick: generate a slightly longer video and then drop the first or last few frames which might be more unstable. Sometimes the very start or end frame can be off.
- Ensure you’re using the distilled model correctly. If you inadvertently used the full model with only 8 steps, it might be under-processing leading to flicker. The full model needs more steps; the distilled one is okay with 8. Match the model to the step count.

**Q: ComfyUI crashes or closes suddenly.**
A: If it just disappears, it might be running out of system RAM or hitting some fatal error. Check if there’s a crash log or run ComfyUI from a terminal to see messages. On Windows, you might see a “Python has stopped working”. This could be memory (check if your RAM usage was maxed) or a bug. Try reducing load as above, and ensure you’re using the latest ComfyUI version, as many bugs are fixed in updates. Also, running too high resolution video frames can crash some video encoding nodes due to memory – try smaller.

**Q: The final video file won’t play or is not created.**
A: If using Video Combine, ensure you gave it a proper file path ending in `.mp4` or `.gif`. Some older versions default to `.webm` or raw. Use `.mp4` for broad compatibility. Also check the console for ffmpeg errors (VideoCombine uses ffmpeg in the back). If it didn’t save, maybe the node didn’t execute. You might have to connect a dummy output (like an Image Viewer) to force execution, depending on node implementation. If all else fails, save frames and compile externally.

**Q: How can I loop the video seamlessly?**
A: Seamless loops are tricky. One idea: make the last frame similar to the first. LTX 0.9.5 introduced a way to condition the last frame ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=1,Commercial%20license%20availability)). If you had a way to feed the first frame as also a “target” for the last, you could morph back. Without that, you can try a subtle approach: not too much change overall, so looping isn’t too jarring. Sometimes reversing the video and concatenating can create a boomerang effect that loops. This is more of a creative editing trick afterwards.

## Tips for Better Results and Experimentation

- **Experiment with Prompts:** The art of prompt crafting applies here as with any AI art. Because Flux is so good, you can try very descriptive prompts or even stylistic ones (photographic vs. painted styles). The LTX stage tends to work best with **literal, descriptive prompts** (imagine you’re describing the video to someone in detail). If you’re not sure, run your motion prompt by ChatGPT with *“Is this a clear description of a video scene?”* – sometimes refining language helps.

- **Use Seeds to Your Advantage:** If you find a seed that gives a great image, note it down. Similarly, LTX might allow a seed for noise in the motion (some workflows allow setting a “video seed”). Consistent seeds can reproduce results or allow you to vary one thing at a time. If you want different outcomes, randomize seeds. If you want the *same* general motion on a slightly different image (or vice versa), keep one seed constant and change the other.

- **Leverage Negative Prompts:** Don’t forget negative prompts in both stages. They can be powerful in removing unwanted artifacts. Common negatives for portraits: *“blurry, duplicate face, text, watermark, deformed, extra finger, mutated”*. For video: *“flicker, jump cut, glitch, distortion”* might help (no guarantee the model understands all those, but it might).

- **Play with Schedules and Advanced Nodes:** Once you get comfortable, you can explore advanced ComfyUI nodes like **STG (Sigma Threshold Gradient) or CFG schedules**. The LTX extension mentioned an “STGGuiderAdvanced” which can vary CFG over diffusion steps ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=We%20introduce%20the%20STGGuiderAdvanced%20node%2C,See%20the%20Example%20Workflows%20section)). These are more technical, but can improve quality if tuned. For example, high CFG in early steps and lower in later steps might reduce flicker.

- **Resolution Upscaling:** If you got a great result at low res, you can try to upscale the final video frames. You could use an AI upscaler frame by frame (like ESRGAN or CodeFormer via ComfyUI nodes, or an external tool). There’s no built-in video upscaler in ComfyUI, but you can save frames, upscale them as a batch, then recombine. This is extra work but can yield sharper videos.

- **Try Text-to-Video Directly:** LTX can also generate video purely from text (no initial image) ([How to use LTX Video 0.9.5 on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/ltx-video-0-9-5/#:~:text=,last%20frames%20in%20the%20video)). This is outside our main flow, but if you’re adventurous, you can attempt a text2video node with LTX. The results might be less coherent without an image anchor, but interesting for abstract or landscape motions. Usually you’d just not use an initial image and prompt the whole scene (the LTX extension likely has a node setup for that).

- **Use Community Workflows:** There are many ready ComfyUI workflows shared on forums (like on r/ComfyUI or the ComfyUI Examples page). For instance, the official ComfyUI examples GitHub has an LTX image-to-video workflow JSON you can download ([Lightricks LTX-Video Model | ComfyUI_examples](https://comfyanonymous.github.io/ComfyUI_examples/ltxv/#:~:text=Image%20to%20Video)) ([Lightricks LTX-Video Model | ComfyUI_examples](https://comfyanonymous.github.io/ComfyUI_examples/ltxv/#:~:text=Input%20image%3A%20Image)). Loading these can give you a baseline that you tweak. If you feel overwhelmed by node setups, don’t hesitate to use these as templates.

- **Keep an eye on VRAM usage:** ComfyUI doesn’t always show VRAM usage, but you can monitor with tools (Nvidia-SMI on Windows, Activity Monitor on Mac). If you’re close to the limit, smaller changes could push you over. Knowing your limits helps (e.g., if 1024x1024 is too much, stick to 768x768 etc.).

- **Document your workflow:** Once you have a working node setup, save the workflow (`File > Save Workflow` in ComfyUI). This lets you easily reuse it without rebuilding. You can create different workflows for different types of videos.

- **Patience and Iteration:** As a maker, you know iteration is key. Don’t be discouraged if the first video is meh. Treat it as a draft. Maybe the lighting changed weirdly – then you add “consistent lighting” to the prompt. Maybe the motion wasn’t noticeable – make it a bit more extreme or add more frames. Each iteration teaches you something about how the models respond.

## Learn More and Next Steps

You’ve now got the basics down! Where to go from here:

- **ComfyUI GitHub and Wiki:** The [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI) is a great place to check for updates (new versions often add features or performance improvements). The Wiki (like comfyui-wiki.com) has a wealth of tutorials and a **FAQ** for common questions. For example, you can learn about different samplers, using ControlNets, or other advanced models in ComfyUI.

- **Flux Model Info:** If you want to dive deeper into Flux, check out the Civitai community discussions or the [Flux Quickstart Guide on Civitai Education】(https://education.civitai.com/)** ([Flux + ComfyUI on Apple Silicon Macs— 2024 | by Jason Griffin | Medium](https://medium.com/@tchpnk/flux-comfyui-on-apple-silicon-with-hardware-acceleration-2024-4d44ed437179#:~:text=lot%20of%20confusion%20about%20whether,can%2C%20what%20the%20limitations%20are)). Flux is an evolving project – keep an eye out for Flux 2 or further refinements. Black Forest Labs might release new variants.

- **LTX Video Community:** LTX is relatively new, but there are Reddit threads (like r/StableDiffusion and r/ComfyUI) discussing it ([LTX Video Workflow Step-by-Step Guide - ComfyUI Wiki](https://comfyui-wiki.com/en/tutorial/advanced/ltx-video-workflow-step-by-step-guide#:~:text=LTX%20Video%20Workflow%20Step,There%20are%20two%20installation%20methods)). The developers (Lightricks) have shared example videos on Twitter and posts on how to use it. Following those can give you ideas (like using multiple control images, etc.). There’s also a YouTube tutorial “How To Use LTX: The FASTEST FREE AI Video Model” ([How To Use LTX: The FASTEST FREE AI Video Model - YouTube](https://www.youtube.com/watch?v=peSg06CzMdk#:~:text=How%20To%20Use%20LTX%3A%20The,on%20your%20own%20computer)) which might complement what you learned here with a visual walkthrough.

- **YouTube Tutorials:** Search YouTube for *“ComfyUI Flux tutorial”* or *“ComfyUI LTX video guide”*. There are many community-made videos. Some YouTubers show their node setups which can be enlightening. Seeing someone build a workflow can solidify your understanding. Also, tutorials on general ComfyUI usage (like making an animation with **AnimateDiff** or using **ControlNet for depth** in videos) could give you new tools to add to your pipeline.

- **Reddit and Discord:** The r/ComfyUI subreddit is active with people sharing workflows, problems, and art. If you run into unique issues, a search there might find someone who had the same trouble. Also, ComfyUI has an official Discord where you can ask questions in real-time and get help or just show off your results. The community is quite helpful to newcomers.

- **Try Other Extensions:** Once comfortable, you could install other ComfyUI extensions for more capabilities:
  - **ControlNet Nodes:** to guide images/video with sketches or depth maps.
  - **AnimateDiff:** an alternative text-to-video approach that you could experiment with inside ComfyUI.
  - **Upscalers and Post-processing:** nodes like ESRGAN upscaler, GIF export nodes, etc., to further polish your outputs.

- **Stay Updated:** AI moves fast. New versions of LTX or Flux may come. For instance, if LTX Video 1.0 releases, it might improve a lot. Check the LTX GitHub or HuggingFace for releases ([GitHub - Lightricks/ComfyUI-LTXVideo: LTX-Video Support for ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo#:~:text=17,%E2%AD%90)). ComfyUI’s Manager makes it easy to update nodes – do click “Update All” once in a while to get latest improvements ([How to install Flux AI model on ComfyUI - Stable Diffusion Art](https://stable-diffusion-art.com/flux-comfyui/#:~:text=ComfyUI%20has%20native%20support%20for,you%20haven%E2%80%99t%20already%20since%20then)).

Finally, approach this as a fun creative process. We now have the ability to create little AI cinematography pieces from our imagination – something that still blows my mind! Tweak prompts, try different subjects (not just people – landscapes, objects, even abstract patterns), and see what motion brings them to life. As Andrej Karpathy might say, it’s all about experimenting and *“seeing what sticks”*. And like Paul Graham might advise, focus on **projects that interest you** – maybe you’ll create a mini film portfolio of AI-generated mood shots.

Enjoy your journey in AI video generation. I hope this guide served as a helpful playbook to get you started. Now go create some cool stuff! 😃


