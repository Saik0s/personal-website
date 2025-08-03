# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with Igor Tarasenko's personal website.

## 🚀 Quick Start

```bash
# Development
npm run dev              # Start dev server at http://localhost:4321
npm run preview          # Preview built site

# Before committing (ALWAYS run these)
npm run format           # Format code with Prettier
npm run lint             # Check for linting issues

# Build & deploy
npm run build            # Astro check + build + Pagefind indexing
```

## 📁 Project Structure

**Tech Stack**: Astro 5.11 + AstroPaper theme + TypeScript + Tailwind CSS 4
**Content**: Technical blog posts about iOS development, AI/ML, and productivity
**Author**: Igor Tarasenko (GitHub: @Saik0s, X: @sa1k0s)

### Key Directories

```
src/
├── data/blog/          # Blog posts with subdirectories per post
│   └── post-name/      # Each post has its own directory
│       ├── index.md    # Post content with frontmatter
│       └── assets/     # Images, videos, ComfyUI workflows
├── config.ts           # Site configuration (URLs, author, pagination)
├── constants.ts        # Social links and sharing options
├── content.config.ts   # Blog content schema validation
├── pages/
│   ├── index.astro     # Homepage
│   ├── about.md        # About page
│   └── api/            # API endpoints (newsletter)
├── styles/
│   ├── global.css      # CSS variables and dark theme
│   └── typography.css  # Typography styles
└── components/         # Reusable Astro components

scripts/                # Python image generation tools
├── image.py            # Basic FAL.ai FLUX image generator
└── generate-header.py  # Template-based header generator
```

## 📝 Content Management

### Blog Post Structure

Each blog post lives in its own subdirectory under `src/data/blog/`:

```yaml
---
title: "Your Post Title"
pubDatetime: 2025-01-21T03:46:18+01:00
modDatetime: 2025-01-21T03:46:18+01:00  # Optional
author: Igor  # Defaults to "Igor Tarasenko"
description: "SEO description (150-160 chars)"
tags:
  - ios-development
  - ai
  - productivity
featured: false
draft: false
ogImage: "assets/header.png"  # Relative to post directory
---

## Table of contents

Your content here...
```

### Image Generation

```bash
# Generate header images (requires FAL_KEY env var)
scripts/image.py "your prompt" output.png --aspect-ratio 21:9

# Use template-based generator for consistent style
scripts/generate-header.py --template ios-ai --title "Your Title" output.png
# Available templates: ios-ai, ios-dev, ai-ml, coreml, productivity, swift, mobile-dev
```

## ⚙️ Configuration

### Site Config (`src/config.ts`)
- `SITE.website`: "https://www.tarasenko.dev/"
- `SITE.author`: "Igor Tarasenko"
- `SITE.postPerPage`: 4 (pagination)
- `SITE.lightAndDarkMode`: false (single dark theme)

### Theme Colors (`src/styles/global.css`)
```css
/* Dark theme (default) */
--background: #212737;
--foreground: #eaedf3;
--accent: #ff6b4a;  /* Orange accent */
--muted: #343f60bf;
--border: #343f60;
```

## 🛠️ Available Commands

```bash
# Core commands
npm run dev              # Start development server
npm run build            # Full build with type checking and Pagefind
npm run preview          # Preview production build
npm run sync            # Generate TypeScript types

# Code quality
npm run format           # Format with Prettier
npm run format:check     # Check formatting
npm run lint             # ESLint validation
```

## 📦 TypeScript Path Aliases

Use these aliases instead of relative imports:
```typescript
@components  // ./src/components
@layouts     // ./src/layouts
@pages       // ./src/pages
@styles      // ./src/styles
@utils       // ./src/utils
@content     // ./src/content
```

## 🚀 Deployment

The site builds to static files in `/dist`:
```bash
npm run build            # Creates /dist folder
# Deploy /dist to any static hosting
```

Deployment configs available:
- `nixpacks.toml` - Nixpacks configuration
- `Dockerfile` - Multi-stage Docker build
- `docker-compose.yml` - Development container

## 🔌 Key Features

- **Search**: Pagefind static site search
- **Analytics**: Plausible (privacy-focused)
- **Newsletter**: ConvertKit integration via API endpoint
- **Social**: GitHub (@Saik0s), X (@sa1k0s), Buy Me a Coffee
- **Custom Components**: PickMyBrainButton, BuyMeACoffeeButton, ConvertKitForm
