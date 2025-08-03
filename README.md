# Igor Tarasenko - Personal Website

Personal website and technical blog built with Astro, featuring articles about iOS development, AI/ML, and productivity.

🌐 **Live Site**: [tarasenko.dev](https://www.tarasenko.dev)

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev              # http://localhost:4321

# Build for production
npm run build            # Creates /dist folder
```

## 📝 Tech Stack

- **Framework**: [Astro](https://astro.build/) v5.11
- **Styling**: [Tailwind CSS](https://tailwindcss.com/) v4
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **Search**: [Pagefind](https://pagefind.app/)
- **Theme**: Based on [AstroPaper](https://github.com/satnaing/astro-paper)

## ✨ Features

- ⚡ Fast static site generation
- 🌙 Dark theme optimized design
- 🔍 Full-text search with Pagefind
- 📱 Fully responsive design
- 🎨 AI-powered header image generation
- 📊 Privacy-focused analytics (Plausible)
- 📬 Newsletter subscription (ConvertKit)
- 🤖 SEO optimized with dynamic OG images

## 📁 Project Structure

```
src/
├── data/blog/          # Blog posts (each in subdirectory)
├── pages/              # Routes and API endpoints
├── components/         # Reusable Astro components
├── layouts/            # Page layouts
├── styles/             # Global styles and typography
├── config.ts           # Site configuration
└── constants.ts        # Social links and constants

scripts/                # Python image generation tools
public/                 # Static assets
```

## 🛠️ Development

### Available Commands

```bash
npm run dev              # Start development server
npm run build            # Build for production
npm run preview          # Preview production build
npm run format           # Format code with Prettier
npm run lint             # Lint with ESLint
npm run sync            # Generate TypeScript types
```

### Creating Blog Posts

1. Create a new directory in `src/data/blog/your-post-name/`
2. Add `index.md` with frontmatter and content
3. Place images in `assets/` subdirectory
4. Generate header image using the provided scripts

### Image Generation

Generate professional header images for blog posts:

```bash
# Basic generation (requires FAL_KEY env var)
scripts/image.py "your prompt" output.png --aspect-ratio 21:9

# Template-based generation
scripts/generate-header.py --template ios-ai --title "Your Title" output.png
```

Available templates: `ios-ai`, `ios-dev`, `ai-ml`, `coreml`, `productivity`, `swift`, `mobile-dev`

## 🚀 Deployment

The site builds to static files suitable for any static hosting provider:

```bash
npm run build            # Generates /dist folder
# Deploy /dist to your hosting provider
```

### Docker Support

```bash
# Using Docker Compose
docker compose up -d

# Using Dockerfile
docker build -t personal-website .
docker run -p 4321:80 personal-website
```

## 🔗 Connect

- **GitHub**: [@Saik0s](https://github.com/Saik0s)
- **X (Twitter)**: [@sa1k0s](https://x.com/sa1k0s)
- **Website**: [tarasenko.dev](https://www.tarasenko.dev)

## 📄 License

MIT License - feel free to use this code for your own projects, but not the content.

---

Built with ❤️ by Igor Tarasenko
