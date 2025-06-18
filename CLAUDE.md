# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is Igor Tarasenko's personal website built with Hugo and the DoIt theme. The site features technical blog posts about iOS development, AI, and productivity.

## Development Commands

### Local Development
```bash
# Start the Hugo development server
make serve
# or
hugo server --watch -D --renderToMemory
```

### Build Site
```bash
# Build the static site
hugo
```

### Generate Header Images
The repository includes a uv script for generating blog post header images using Flux Kontext:
```bash
# Requires FAL_KEY environment variable
scripts/image.py "your prompt" path/to/image.png

# With custom aspect ratio (default is 16:9)
scripts/image.py "your prompt" header.png --aspect-ratio 21:9
```

## Architecture & Structure

### Content Organization
- Blog posts are located in `content/posts/`
- Each post is a directory containing:
  - `index.md` - The main content file
  - `header.png` or `header.webp` - Featured image
  - `header_preview.png` - Preview thumbnail
  - `assets/` - Additional images and resources
  - `workflows/` - JSON workflow files (for ComfyUI tutorials)

### Configuration
- Main site configuration: `hugo.toml`
- Theme: DoIt (located in `themes/DoIt/`)
- Custom styling: `assets/css/_custom.scss` and `_override.scss`

### Key Features
- Giscus comments integration (configured for GitHub discussions)
- Plausible analytics
- Dark theme as default
- Social links (GitHub: Saik0s, X: sa1k0s)

## Content Guidelines

### Creating New Posts
1. Create a new directory under `content/posts/`
2. Add `index.md` with proper frontmatter
3. Include featured images (header.png/webp and header_preview.png)
4. Place additional assets in an `assets/` subdirectory

### Frontmatter Template
```yaml
---
title: "Your Title"
subtitle: "Optional subtitle"
date: 2025-01-21T03:46:18+01:00
lastmod: 2025-01-21T03:46:18+01:00
draft: false
authors: ["Igor"]
description: ""
tags: []
categories: []
series: []
hiddenFromHomePage: false
hiddenFromSearch: false
featuredImage: "header.webp"
featuredImagePreview: "header_preview.png"
math:
  enable: false
toc:
  enable: true
  auto: true
code:
  maxShownLines: 100
  lineNos: false
  wrap: false
  header: true
lightgallery: false
license: ""
---
```

## Deployment
- The site uses Staticfile for deployment configuration
- Deployment settings are in `Staticfile` and `nixpacks.toml`