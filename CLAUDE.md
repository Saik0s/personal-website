# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with Igor Tarasenko's personal website.

## 🚀 Quick Start

```bash
# Start development server
npm run dev              # http://localhost:4321

# Before committing (ALWAYS run these)
npm run format           # Format code
npm run lint             # Check for issues
npm run typecheck        # Verify types

# Build & deploy
npm run build            # Generate static site in /dist
```

## 📁 Project Overview

**Tech Stack**: Astro + AstroPaper theme + TypeScript + Tailwind CSS  
**Content**: Technical blog posts about iOS development, AI, and productivity  
**Author**: Igor Tarasenko (GitHub: @Saik0s, X: @sa1k0s)

### Key Files & Locations

```
src/
├── data/blog/          # Blog posts (markdown/mdx)
├── config.ts           # Site configuration
├── constants.ts        # Social links, constants
├── pages/
│   ├── index.astro     # Homepage
│   ├── about.md        # About page
│   └── api/            # API endpoints
├── styles/
│   ├── global.css      # Tailwind config + theme colors
│   └── typography.css  # Typography styles
└── components/         # Reusable components

public/
├── toggle-theme.js     # Theme switching logic
└── assets/             # Static assets

scripts/                # Image generation scripts
```

## 📝 Content Management

### Creating Blog Posts

1. Create file in `src/data/blog/` (supports subdirectories)
2. Use this frontmatter template:

```yaml
---
title: "Your Title"
pubDatetime: 2025-01-21T03:46:18+01:00
modDatetime: 2025-01-21T03:46:18+01:00  # Optional, for updates
draft: false
author: Igor
tags:
  - ios-development
  - ai
  - productivity
description: "SEO description (150-160 chars)"
featured: false
ogImage: "header_preview.png"  # Optional
---

## Table of contents

Your content here...
```

### Image Generation

```bash
# Generate blog header images (requires FAL_KEY env var)
scripts/image.py "your prompt" header.png --aspect-ratio 21:9

# Use template-based generator
scripts/generate-header.py --template ios-ai --title "Your Title" output.png
# Templates: ios-ai, ios-dev, ai-ml, coreml, productivity, swift, mobile-dev
```

## ⚙️ Configuration

### Site Config (`src/config.ts`)

- `SITE.website`: Your deployed URL (required for production)
- `SITE.title`: Site name
- `SITE.author`: Default author name
- `SITE.postPerPage`: Posts per page (pagination)
- `SITE.lightAndDarkMode`: Enable theme switching

### Social Links (`src/constants.ts`)

- `SOCIALS`: Array of social media links
- `SHARE_LINKS`: Post sharing options

### Theme Colors (`src/styles/global.css`)

```css
/* Light theme */
:root {
  --background: #fdfdfd;
  --foreground: #282728;
  --accent: #006cac;
  --muted: #e6e6e6;
  --border: #ece9e9;
}

/* Dark theme */
html[data-theme="dark"] {
  --background: #212737;
  --foreground: #eaedf3;
  --accent: #ff6b01;
  --muted: #343f60bf;
  --border: #ab4b08;
}
```

## 🛠️ Development Commands

```bash
# Development
npm run dev              # Start dev server
npm run preview          # Preview built site

# Code Quality
npm run format           # Prettier formatting
npm run lint             # ESLint checks
npm run typecheck        # TypeScript validation

# Building
npm run build            # Build static site
npm run all              # Format + lint + typecheck + build

# Testing
npm run test             # Unit tests (Vitest)
npm run test:e2e         # E2E tests (Playwright)

# Utilities
npm run clean            # Clean build artifacts
npm run lighthouse       # Performance audit
npm run validate:content # Validate content structure
```

## 🔌 Integrations & Features

- **Comments**: Giscus (GitHub discussions-based)
- **Analytics**: Plausible (privacy-focused)
- **Search**: Pagefind (static site search)
- **Newsletter**: Custom API endpoint (`src/pages/api/newsletter.ts`)
- **Mentorship**: Custom offerings page
- **Social**: GitHub (@Saik0s), X (@sa1k0s)

## 🚀 Deployment

```bash
npm run build            # Generates /dist folder
# Deploy /dist to your hosting provider
```

Config: `nixpacks.toml` (for deployment configuration)

## 📦 TypeScript Path Aliases

```typescript
@components  // src/components
@layouts     // src/layouts
@pages       // src/pages
@styles      // src/styles
@utils       // src/utils
@content     // src/content
@config      // src/config
@types       // src/types
```

## 🐛 Common Issues

1. **Image generation fails**: Set `FAL_KEY` environment variable
2. **Build errors**: Run `npm run typecheck` to find type issues
3. **Theme not switching**: Check `/public/toggle-theme.js`
4. **Path import errors**: Use @ aliases instead of relative paths

## 📚 AstroPaper Documentation

For detailed AstroPaper theme documentation:
- Configuration: See deleted `how-to-configure-astropaper-theme.md`
- Styling: See deleted `customizing-astropaper-theme-color-schemes.md`
- Content: See deleted `adding-new-posts-in-astropaper-theme.md`
- Features: Check deleted blog posts in `src/data/blog/`

## 🎯 Important Reminders

- Always run format/lint/typecheck before committing
- Use existing files/components when possible
- Follow AstroPaper's design patterns
- Keep content minimal and focused
- Test dark/light theme compatibility