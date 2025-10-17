---
title: Website Update Implementation Plan - Drop-In Engineering Co-Pilot
type: project-spec
status: ready
signal: high
purpose: Complete implementation spec for updating tarasenko.dev with focused iOS + Agentic Engineering positioning
created: 2025-10-17
modified: 2025-10-17
action_plan_link: "CONSULTANCY - Land 2 enterprise AI projects (Q1 2025)"
---

# Website Update Implementation Plan

## Executive Summary

Transform tarasenko.dev from generic "AI & software" positioning to **focused specialist: iOS Engineering + Agentic Workflows + Developer Tooling**.

**Core positioning:** "iOS Engineer & Agentic Automation Specialist available for focused €200/hr engineering sessions."

**Key changes:**
- Sharpen homepage hero to specialist positioning
- Add "What I Help With" section (3 service areas)
- Create dedicated `/services` page with full offer details
- Update About page with proof-driven expertise
- Add Services navigation link

---

## Current Website Analysis

### Tech Stack
- **Framework:** Astro 5.11
- **Styling:** Tailwind CSS v4 (inline theme)
- **Font:** Monospace (font-mono)
- **Search:** Pagefind
- **Analytics:** Plausible

### Color Scheme (Dark Theme)
```css
--background: #2d2d2d  /* Dark gray background */
--foreground: #e8e8e8  /* Light gray text */
--accent: #ff6b4a      /* Coral/orange accent */
--muted: #808080       /* Mid gray */
--border: #3d3d3d      /* Darker gray borders */
```

### Current Navigation
- Blog (links to /posts)
- Projects
- About
- Search (icon)

### Existing Components
- `PickMyBrainButton.astro` - Pushable button variant + simple variant
- `Card.astro` - Blog post card
- `Header.astro` - Main navigation
- `Footer.astro` - Site footer
- `Hr.astro` - Horizontal rule

### Current Homepage Structure
```
Hero Section
  - H1: "Hey, I'm Igor. I craft AI & software people love."
  - P: Generic positioning (mentoring, advising, agentic workflows)
  - PickMyBrainButton (pushable variant)
  - Socials

Recent Posts (5 posts)
```

---

## Detailed Implementation Specifications

---

## 1. Homepage Updates (`src/pages/index.astro`)

### 1.1 Hero Section - BEFORE
```astro
<h1 class="fade-up mb-6 text-5xl font-bold leading-tight">
  Hey, I'm Igor.<br />
  I craft AI & software people love.
</h1>

<p class="fade-up mb-4 text-xl text-foreground/80" style="animation-delay: 0.1s">
  Mentoring devs, advising execs, and building agentic workflows that enhance productivity and creativity.
</p>

<p class="fade-up mb-8 text-lg text-foreground/70" style="animation-delay: 0.2s">
  Need practical insights on iOS, ComfyUI, LLMs, or automation? Let's talk.
</p>
```

### 1.2 Hero Section - AFTER
```astro
<h1 class="fade-up mb-6 text-5xl font-bold leading-tight">
  Hey, I'm Igor.<br />
  iOS Engineer & Agentic Automation Specialist.
</h1>

<p class="fade-up mb-4 text-xl text-foreground/80" style="animation-delay: 0.1s">
  Senior engineer available for focused sessions: iOS optimization, agentic workflows,
  dev tooling, and AI-powered automation.
</p>

<p class="fade-up mb-8 text-lg text-foreground/70" style="animation-delay: 0.2s">
  €200/hr · Book 1-10 hour sessions · No retainers, no BS.
</p>
```

**Changes:**
- Remove generic "craft AI & software people love"
- Add specific positioning: "iOS Engineer & Agentic Automation Specialist"
- Replace vague "mentoring/advising" with concrete service offerings
- Add pricing transparency in subhead
- Direct, no-fluff tone

### 1.3 CTA Button - BEFORE
```astro
<PickMyBrainButton
  variant="pushable"
  duration="60min"
  text="Pick My Brain"
/>
```

### 1.4 CTA Button - AFTER
```astro
<PickMyBrainButton
  variant="pushable"
  duration="60min"
  text="Book Engineering Session"
/>
```

**Note:** Update `PickMyBrainButton.astro` default text or create new `BookSessionButton.astro`

### 1.5 NEW SECTION: "What I Help With" (Insert after Hero, before Recent Posts)

```astro
<Hr />

<!-- What I Help With Section -->
<section id="services-preview" class="py-12">
  <h2 class="fade-up mb-8 text-2xl font-semibold" style="animation-delay: 0.4s">
    What I Help With
  </h2>

  <div class="fade-up grid gap-6 md:grid-cols-3" style="animation-delay: 0.5s">
    <!-- Service Card 1: iOS Engineering -->
    <div class="service-card group rounded-lg border border-border bg-background/50 p-6 transition-all hover:border-accent/50 hover:bg-background/80">
      <h3 class="mb-3 text-lg font-semibold text-accent">iOS Engineering</h3>
      <ul class="space-y-2 text-sm text-foreground/80">
        <li>• App architecture & modularization</li>
        <li>• Build time optimization</li>
        <li>• Swift/SwiftUI best practices</li>
        <li>• Configuration & debugging</li>
      </ul>
    </div>

    <!-- Service Card 2: Agentic Workflows -->
    <div class="service-card group rounded-lg border border-border bg-background/50 p-6 transition-all hover:border-accent/50 hover:bg-background/80">
      <h3 class="mb-3 text-lg font-semibold text-accent">Agentic Workflows</h3>
      <ul class="space-y-2 text-sm text-foreground/80">
        <li>• Repository setup for AI agents</li>
        <li>• Workflow automation & tooling</li>
        <li>• Team onboarding for agentic engineering</li>
        <li>• Practical LLM integration</li>
      </ul>
    </div>

    <!-- Service Card 3: Developer Tooling -->
    <div class="service-card group rounded-lg border border-border bg-background/50 p-6 transition-all hover:border-accent/50 hover:bg-background/80">
      <h3 class="mb-3 text-lg font-semibold text-accent">Developer Tooling</h3>
      <ul class="space-y-2 text-sm text-foreground/80">
        <li>• Custom automation scripts</li>
        <li>• Personal productivity tools</li>
        <li>• ComfyUI workflows</li>
        <li>• Browser automation (mcp-browser-use)</li>
      </ul>
    </div>
  </div>

  <div class="fade-up mt-8 text-center" style="animation-delay: 0.6s">
    <p class="mb-4 text-foreground/70">
      €200/hr · Book 1, 3, 5, or 10-hour packs · First hour money-back guarantee
    </p>
    <a
      href="/services"
      class="inline-flex items-center text-accent hover:underline"
    >
      View full service details →
    </a>
  </div>
</section>

<Hr />
```

**Styling Notes:**
- Service cards use existing color variables
- Hover state: border changes to accent color at 50% opacity
- Background darkens slightly on hover for depth
- Responsive: 3 columns on desktop, 1 column on mobile
- Maintains fade-up animation consistency with rest of page

---

## 2. New Services Page (`src/pages/services.astro`)

### 2.1 File Location
`/Users/igortarasenko/Projects/personal-website/src/pages/services.astro`

### 2.2 Full Page Content

```astro
---
import Layout from "@/layouts/Layout.astro";
import Header from "@/components/Header.astro";
import Footer from "@/components/Footer.astro";
import Hr from "@/components/Hr.astro";
import PickMyBrainButton from "@/components/PickMyBrainButton.astro";

const pageTitle = "Engineering Sessions - Igor Tarasenko";
const pageDesc = "Drop-in engineering sessions for iOS optimization, agentic workflows, and developer tooling. €200/hr, no retainers.";
---

<Layout title={pageTitle} description={pageDesc}>
  <Header />
  <main id="main-content" class="mx-auto max-w-4xl px-4 pb-12">

    <!-- Hero -->
    <section id="services-hero" class="py-20 text-left">
      <h1 class="fade-up mb-6 text-5xl font-bold leading-tight">
        Drop-In Engineering Sessions
      </h1>

      <p class="fade-up mb-4 text-xl text-foreground/80" style="animation-delay: 0.1s">
        Senior iOS engineer + AI agent specialist on call for focused, high-leverage
        sessions — architecture, automation, and agentic workflows that actually ship.
      </p>

      <div class="fade-up mb-8 flex items-center gap-6" style="animation-delay: 0.2s">
        <PickMyBrainButton
          variant="pushable"
          duration="60min"
          text="Book a Session"
        />
      </div>
    </section>

    <Hr />

    <!-- Who It's For -->
    <section id="who-its-for" class="py-12">
      <h2 class="mb-6 text-2xl font-semibold">Who It's For</h2>

      <p class="mb-4 text-foreground/80">
        iOS teams and technical founders who need sharp, hands-on help to:
      </p>

      <ul class="mb-6 space-y-3 text-foreground/80">
        <li>• <strong>Optimize iOS apps:</strong> modularization, build time reduction, architecture decisions</li>
        <li>• <strong>Adopt agentic engineering:</strong> set up repos for AI agents, automate workflows, onboard teams</li>
        <li>• <strong>Build developer tooling:</strong> custom scripts, automation pipelines, productivity tools</li>
        <li>• <strong>Prototype AI features:</strong> brainstorm tech stacks, integrate LLMs, ComfyUI workflows</li>
        <li>• <strong>Debug iOS configuration:</strong> build issues, dependency management, obscure errors</li>
      </ul>
    </section>

    <Hr />

    <!-- What We Do -->
    <section id="what-we-do" class="py-12">
      <h2 class="mb-6 text-2xl font-semibold">What We Do (Live, Together)</h2>

      <ul class="mb-6 space-y-4 text-foreground/80">
        <li>
          <strong class="text-foreground">Real-time pair programming & code review</strong> on your repo (recordable).
          <span class="text-sm text-muted">
            Raises quality and accelerates knowledge transfer; pair programming improves design quality and reduces defects.
          </span>
        </li>

        <li>
          <strong class="text-foreground">Targeted diagnostics</strong> (build traces, logs, repros) and annotated PRs with "do this next" steps.
        </li>

        <li>
          <strong class="text-foreground">Agentic engineering enablement:</strong> set up practical workflows (CLAUDE.md, agent commands, evaluation loops) so the team keeps moving after the session.
          <span class="text-sm text-muted">
            Productized "discovery/roadmapping" containers like this are proven on-ramps for consulting: they're specific, bounded, and ship decisions.
          </span>
        </li>

        <li>
          <strong class="text-foreground">iOS optimization:</strong> modularize monolithic apps, reduce build times, architect for maintainability.
        </li>
      </ul>
    </section>

    <Hr />

    <!-- How It Works -->
    <section id="how-it-works" class="py-12">
      <h2 class="mb-6 text-2xl font-semibold">How It Works</h2>

      <ol class="mb-6 space-y-4 text-foreground/80">
        <li>
          <strong class="text-foreground">1. Book a slot</strong> and share repo + brief (scope, stack, build/run steps).
        </li>

        <li>
          <strong class="text-foreground">2. Kickoff session (60–120 min):</strong> reproduce the issue or walk the goal; decide the smallest change that buys the most certainty.
        </li>

        <li>
          <strong class="text-foreground">3. Work sessions (book as needed):</strong> ship fixes, capture decisions, open PRs.
        </li>

        <li>
          <strong class="text-foreground">4. Wrap note:</strong> bulleted outcomes, links to PRs/commits, and next 2–3 moves.
          <span class="text-sm text-muted">No multi-week retainer theatre.</span>
        </li>
      </ol>
    </section>

    <Hr />

    <!-- Pricing -->
    <section id="pricing" class="py-12">
      <h2 class="mb-6 text-2xl font-semibold">Pricing & Capacity</h2>

      <div class="mb-6 rounded-lg border border-accent/30 bg-accent/5 p-6">
        <p class="mb-4 text-xl font-semibold text-accent">€200/hr</p>
        <p class="mb-4 text-foreground/80">
          Purchase hour blocks and schedule in 60–120 minute sessions.
        </p>

        <div class="mb-4">
          <p class="mb-2 font-semibold text-foreground">Prepaid Packs (priority scheduling):</p>
          <ul class="space-y-1 text-foreground/80">
            <li>• 3 hours: €600</li>
            <li>• 5 hours: €1,000</li>
            <li>• 10 hours: €2,000</li>
          </ul>
        </div>

        <p class="text-sm text-foreground/70">
          Payment: card or invoice. Unused time is refundable in full.
        </p>
      </div>

      <div class="rounded-lg border border-border bg-background/50 p-6">
        <p class="font-semibold text-accent">Guarantee</p>
        <p class="text-foreground/80">
          If by the end of the first hour you feel it wasn't useful, you don't pay.
        </p>
      </div>
    </section>

    <Hr />

    <!-- Typical Outcomes -->
    <section id="outcomes" class="py-12">
      <h2 class="mb-6 text-2xl font-semibold">Typical Outcomes in 1–5 Hours</h2>

      <ul class="mb-6 space-y-3 text-foreground/80">
        <li>
          • <strong>iOS build time reduction:</strong> modularize dependencies, optimize build phases, crisp "build optimization plan" with metrics
        </li>
        <li>
          • <strong>Agentic repo setup:</strong> working CLAUDE.md, custom agent commands, team onboarding doc
        </li>
        <li>
          • <strong>AI feature prototype:</strong> LLM integration stub live behind a flag (prompt, tool call, eval harness)
        </li>
        <li>
          • <strong>Developer tooling:</strong> custom automation script (ComfyUI workflow, browser automation, build pipeline)
        </li>
        <li>
          • <strong>Code quality tightening:</strong> review checklists + smaller PRs grounded in known best-practices, not vibes
        </li>
      </ul>
    </section>

    <Hr />

    <!-- FAQ -->
    <section id="faq" class="py-12">
      <h2 class="mb-6 text-2xl font-semibold">FAQ</h2>

      <div class="space-y-6">
        <div>
          <p class="mb-2 font-semibold text-foreground">What if we don't finish in one session?</p>
          <p class="text-foreground/80">
            Book another hour. Each session leaves you with working code or a clear next move.
            No obligation to continue if you've got what you need.
          </p>
        </div>

        <div>
          <p class="mb-2 font-semibold text-foreground">Do you do long projects?</p>
          <p class="text-foreground/80">
            This offer is for focused sessions only. If you need a multi-month build,
            I'll refer you to trusted partners.
          </p>
        </div>

        <div>
          <p class="mb-2 font-semibold text-foreground">Can you help with React/Next.js or other stacks?</p>
          <p class="text-foreground/80">
            My deep expertise is iOS + Agentic Engineering + Developer Tooling.
            I can help with general architecture/automation questions across stacks,
            but for production React/Next.js debugging, you want a specialist in that ecosystem.
          </p>
        </div>

        <div>
          <p class="mb-2 font-semibold text-foreground">What's your availability?</p>
          <p class="text-foreground/80">
            Check the booking calendar for current availability. Prepaid packs get priority scheduling.
          </p>
        </div>
      </div>
    </section>

    <Hr />

    <!-- Final CTA -->
    <section id="final-cta" class="py-12 text-center">
      <h2 class="mb-4 text-2xl font-semibold">Ready to Ship Faster?</h2>
      <p class="mb-8 text-foreground/80">
        Book a slot or ask a question. No sales calls, no multi-week proposals.
      </p>

      <div class="flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
        <PickMyBrainButton
          variant="pushable"
          duration="60min"
          text="Book a Session"
        />

        <a
          href="https://x.com/sa1k0s"
          target="_blank"
          class="about-button pick-my-brain-button"
        >
          Ask a Question on X
        </a>
      </div>
    </section>

  </main>
  <Footer />
</Layout>

<style>
  /* Ensure mobile responsiveness */
  @media (max-width: 640px) {
    h1 {
      font-size: 2.5rem !important;
    }
  }
</style>
```

**Styling Notes:**
- Uses existing color system (accent, foreground, background, border)
- Maintains fade-up animations for consistency
- Responsive: stacks on mobile, side-by-side on desktop
- Pricing section uses accent color highlight box for emphasis
- FAQ section uses simple Q&A format with bold questions

---

## 3. About Page Updates (`src/pages/about.astro`)

### 3.1 Current "What I've Done" Section - KEEP AS IS

### 3.2 Update "Current Focus" Section

**BEFORE:**
```astro
<h2>Current Focus</h2>
<ul>
  <li>On-device AI for iOS apps</li>
  <li>ComfyUI workflows & Agentic Engineering</li>
  <li>Stable Diffusion & LLM integration</li>
  <li>AI agents & advanced browser automation</li>
  <li>Developer productivity tools</li>
  <li>High-leverage consulting</li>
</ul>
```

**AFTER:**
```astro
<h2>What I Do</h2>

<p>
  Specialist in three areas where I have proven expertise and shipped products:
</p>

<h3>iOS Engineering (15+ years)</h3>
<ul>
  <li>Shipped millions of downloads at Uber</li>
  <li><strong>WhisperBoard:</strong> 50k+ downloads, 888★ GitHub, 4.8★ App Store</li>
  <li><strong>VibeSwitch:</strong> Privacy-first AI keyboard for iOS</li>
  <li>Expert in Swift/SwiftUI, app architecture, build optimization, modularization</li>
</ul>

<h3>Agentic Engineering</h3>
<ul>
  <li>Built <strong>mcp-browser-use</strong> (767★ GitHub) - Python server for browser automation</li>
  <li>Write comprehensive guides on AI agent integration and repository setup</li>
  <li>Help teams adopt AI-assisted workflows effectively (CLAUDE.md, agent commands, eval loops)</li>
  <li>Published: "Is Your Repo Ready for AI Agents?" and "Agentic Engineering Solo Cell"</li>
</ul>

<h3>Developer Tooling & Automation</h3>
<ul>
  <li>ComfyUI workflow expert - complete beginner guides with downloadable workflows</li>
  <li>Custom dev tools and personal automation scripts</li>
  <li>Productivity optimization for engineering teams</li>
  <li>Focus on practical, ship-today tooling vs. theoretical frameworks</li>
</ul>
```

### 3.3 Update "Let's Connect" Section

**BEFORE:**
```astro
<h2>Let's Connect</h2>
<p>
  Want to build something epic, boost your AI skills, or automate the mundane
  away? <strong>Let's chat.</strong>
</p>

<ul>
  <li>
    <a href="https://cal.com/tarasenko/30min" target="_blank" class="about-button pick-my-brain-button">
      Pick My Brain (30 min)
    </a>
  </li>
  <li>
    <a href="https://cal.com/tarasenko/60min" target="_blank" class="about-button pick-my-brain-button">
      Pick My Brain (60 min)
    </a>
  </li>
  <li>
    <a href="https://www.codementor.io/@saik0s?refer=badge">
      <img src="/book-session.svg" alt="Book a session with Igor" style="margin-inline: 0;" />
    </a>
  </li>
</ul>
```

**AFTER:**
```astro
<h2>Available For</h2>
<p>
  Focused engineering sessions on iOS optimization, agentic workflows, and developer tooling.
  <strong>€200/hr, no retainers.</strong>
</p>

<ul>
  <li>
    <a href="/services" class="about-button pick-my-brain-button">
      View Services & Pricing →
    </a>
  </li>
  <li>
    <a href="https://cal.com/tarasenko/60min" target="_blank" class="about-button pick-my-brain-button">
      Book Engineering Session (60 min)
    </a>
  </li>
</ul>

<p>
  Find me on <a href="https://github.com/Saik0s">GitHub</a> or <a href="https://x.com/sa1k0s">X</a>.
</p>
```

**Changes:**
- Remove 30min option (focus on 60min serious sessions)
- Remove Codementor badge (outdated, not primary CTA)
- Add link to new services page
- Add pricing transparency
- More action-oriented heading ("Available For" vs. "Let's Connect")

---

## 4. Navigation Update (`src/components/Header.astro`)

### 4.1 Add Services Link

**BEFORE:**
```astro
<li>
  <a href="/posts" class:list={{ "active-nav": isActive("/posts") || isActive("/articles") || isActive("/notes") }}>
    Blog
  </a>
</li>
<li>
  <a href="/projects" class:list={{ "active-nav": isActive("/projects") }}>
    Projects
  </a>
</li>
<li>
  <a href="/about" class:list={{ "active-nav": isActive("/about") }}>
    About
  </a>
</li>
```

**AFTER:**
```astro
<li>
  <a href="/posts" class:list={{ "active-nav": isActive("/posts") || isActive("/articles") || isActive("/notes") }}>
    Blog
  </a>
</li>
<li>
  <a href="/services" class:list={{ "active-nav": isActive("/services") }}>
    Services
  </a>
</li>
<li>
  <a href="/projects" class:list={{ "active-nav": isActive("/projects") }}>
    Projects
  </a>
</li>
<li>
  <a href="/about" class:list={{ "active-nav": isActive("/about") }}>
    About
  </a>
</li>
```

**Order:** Blog → Services → Projects → About → Search

---

## 5. Site Config Update (`src/config.ts`)

### 5.1 Update Description

**BEFORE:**
```ts
desc: "Technical blog about iOS development, AI/ML integration, and developer productivity",
```

**AFTER:**
```ts
desc: "iOS engineer & agentic automation specialist. Available for focused engineering sessions on iOS optimization, AI workflows, and developer tooling.",
```

**Impact:** Updates all meta tags, social sharing cards, RSS feed description

---

## 6. Optional Component: ServiceCard (Reusable)

### 6.1 File Location
`/Users/igortarasenko/Projects/personal-website/src/components/ServiceCard.astro`

### 6.2 Component Code

```astro
---
export interface Props {
  title: string;
  items: string[];
}

const { title, items } = Astro.props;
---

<div class="service-card group rounded-lg border border-border bg-background/50 p-6 transition-all hover:border-accent/50 hover:bg-background/80">
  <h3 class="mb-3 text-lg font-semibold text-accent">{title}</h3>
  <ul class="space-y-2 text-sm text-foreground/80">
    {items.map(item => (
      <li>• {item}</li>
    ))}
  </ul>
</div>
```

### 6.3 Usage Example (in index.astro)

```astro
---
import ServiceCard from "@/components/ServiceCard.astro";

const iosServices = [
  "App architecture & modularization",
  "Build time optimization",
  "Swift/SwiftUI best practices",
  "Configuration & debugging"
];

const agenticServices = [
  "Repository setup for AI agents",
  "Workflow automation & tooling",
  "Team onboarding for agentic engineering",
  "Practical LLM integration"
];

const toolingServices = [
  "Custom automation scripts",
  "Personal productivity tools",
  "ComfyUI workflows",
  "Browser automation (mcp-browser-use)"
];
---

<div class="grid gap-6 md:grid-cols-3">
  <ServiceCard title="iOS Engineering" items={iosServices} />
  <ServiceCard title="Agentic Workflows" items={agenticServices} />
  <ServiceCard title="Developer Tooling" items={toolingServices} />
</div>
```

**Note:** This is optional. Can inline the cards in index.astro if you prefer less abstraction.

---

## 7. Button Component Update

### 7.1 Option A: Update Existing PickMyBrainButton

**File:** `src/components/PickMyBrainButton.astro`

**Change default text:**
```astro
const {
  variant = "simple",
  duration = "60min",
  text = duration === "30min" ? "Book Session (30 min)" : "Book Engineering Session",
} = Astro.props;
```

### 7.2 Option B: Create New BookSessionButton

Create duplicate of PickMyBrainButton with different default text and name.

**Recommendation:** Option A (less duplication, already established component)

---

## 8. Content Tone & Voice Guidelines

### 8.1 Voice Characteristics
- **Direct:** No marketing fluff, no superlatives
- **Technical:** Use specific terms (modularization, build time, agentic workflows)
- **Transparent:** Show pricing upfront, acknowledge limitations
- **Proof-driven:** Cite GitHub stars, downloads, blog posts
- **Action-oriented:** "Book," "Ship," "Optimize" vs. "Explore," "Discover"

### 8.2 What to Avoid
- ❌ "Revolutionary," "cutting-edge," "game-changing"
- ❌ "Let's explore," "Let's chat" (use "Book a session")
- ❌ Vague "I help companies" (be specific: "iOS teams" or "technical founders")
- ❌ Over-promising ("I can help with anything" → "My expertise is iOS + Agentic Engineering")

### 8.3 Proof Points to Emphasize
- ✅ WhisperBoard: 888★ GitHub, 50k+ downloads, 4.8★ App Store
- ✅ mcp-browser-use: 767★ GitHub
- ✅ VibeSwitch: Privacy-first iOS keyboard
- ✅ Published blog posts (link to them)
- ✅ Codementor track record (mention in About, not CTA)
- ✅ 15+ years iOS experience, Uber background

---

## 9. Responsive Design Specifications

### 9.1 Breakpoints (Tailwind defaults)
- `sm:` 640px and up
- `md:` 768px and up
- `lg:` 1024px and up

### 9.2 Service Cards Grid
```astro
<!-- Mobile: single column -->
<!-- Tablet/Desktop: 3 columns -->
<div class="grid gap-6 md:grid-cols-3">
```

### 9.3 Hero Text
```astro
<!-- Mobile: 2.5rem (40px) -->
<!-- Desktop: 3rem (48px) -->
<h1 class="mb-6 text-5xl font-bold leading-tight">
```

With override in style tag:
```css
@media (max-width: 640px) {
  h1 {
    font-size: 2.5rem !important;
  }
}
```

### 9.4 CTA Button Layout
```astro
<!-- Mobile: stack vertically -->
<!-- Desktop: horizontal flex -->
<div class="flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
```

---

## 10. SEO & Metadata

### 10.1 Homepage
```ts
title: "Igor Tarasenko - iOS Engineer & Agentic Automation Specialist"
description: "Senior iOS engineer available for focused sessions on iOS optimization, agentic workflows, and developer tooling. €200/hr, no retainers."
```

### 10.2 Services Page
```ts
title: "Engineering Sessions - Igor Tarasenko"
description: "Drop-in engineering sessions for iOS optimization, agentic workflows, and developer tooling. €200/hr, no retainers."
```

### 10.3 About Page (keep existing, or update)
```ts
title: "About - Igor Tarasenko"
description: "15+ years iOS engineering, AI agent specialist, developer tooling expert. WhisperBoard, mcp-browser-use creator."
```

---

## 11. Implementation Checklist

### Phase 1: Content Updates (High Priority)
- [ ] Update homepage hero text (index.astro)
- [ ] Add "What I Help With" section to homepage (index.astro)
- [ ] Create services page (new file: services.astro)
- [ ] Update About page sections (about.astro)
- [ ] Update site config description (config.ts)

### Phase 2: Navigation & Components
- [ ] Add Services link to Header navigation (Header.astro)
- [ ] Update PickMyBrainButton default text OR create BookSessionButton
- [ ] (Optional) Create ServiceCard component if using reusable approach

### Phase 3: Testing & QA
- [ ] Test responsive design on mobile (iPhone, Android)
- [ ] Test responsive design on tablet (iPad)
- [ ] Verify all internal links work (/services, /about, etc.)
- [ ] Verify external links open in new tab (cal.com, X, GitHub)
- [ ] Test fade-up animations on all pages
- [ ] Verify service cards hover states
- [ ] Check button hover/active states
- [ ] Verify SEO meta tags in page source

### Phase 4: Content Verification
- [ ] Proofread all copy for typos
- [ ] Verify pricing consistency (€200/hr everywhere)
- [ ] Verify social proof accuracy (GitHub stars, download counts)
- [ ] Ensure no over-promises (React/Next.js removed, etc.)
- [ ] Check tone consistency across all pages

### Phase 5: Deployment
- [ ] Run `npm run build` locally to verify no errors
- [ ] Check Astro build output for warnings
- [ ] Deploy to production
- [ ] Verify live site matches local
- [ ] Test Plausible analytics tracking
- [ ] Submit updated sitemap to Google Search Console (if applicable)

---

## 12. Post-Launch Tasks

### Week 1
- [ ] Monitor analytics for /services page views
- [ ] Track booking conversion rate (sessions scheduled)
- [ ] Collect initial feedback from first 2-3 clients
- [ ] Note common questions → add to FAQ section

### Month 1
- [ ] Add first testimonial/case study if client approves
- [ ] Consider adding "Recent Work" section with redacted examples
- [ ] Review bounce rate on services page
- [ ] A/B test CTA button text if needed

### Q2 2025 (After validation)
- [ ] Add Tier 0: Free content (newsletter signup)
- [ ] Add Tier 2: Workshop offering (€3K, group format)
- [ ] Create case studies page if you have 3+ successful engagements
- [ ] Consider adding video testimonials or Loom demo clips

---

## 13. Questions to Answer Before Implementation

### Content Decisions
1. **Services page URL:** `/services` or `/consulting`?
   - **Recommendation:** `/services` (clearer, more common)

2. **Keep "Pick My Brain" branding** or switch to "Book Engineering Session"?
   - **Recommendation:** Switch to "Book Engineering Session" (more professional, clearer value)

3. **Show pricing on homepage** or only on services page?
   - **Recommendation:** Tease pricing on homepage ("€200/hr"), full details on services page

4. **Add testimonials/social proof** from Codementor or skip for V1?
   - **Recommendation:** Skip for V1, add in Week 2-4 after first clients

### Technical Decisions
5. **ServiceCard component** (reusable) or inline cards?
   - **Recommendation:** Inline for V1 (faster), extract to component later if reused

6. **Remove Projects nav link** since no projects page exists?
   - **Recommendation:** Check if /projects exists. If not, remove from nav.

7. **Update button component** or create new one?
   - **Recommendation:** Update existing PickMyBrainButton default text

---

## 14. File Changes Summary

### New Files (1)
```
src/pages/services.astro
```

### Modified Files (5)
```
src/pages/index.astro          # Hero text, add service cards section
src/pages/about.astro          # Update "What I Do" and "Available For" sections
src/components/Header.astro    # Add Services nav link
src/components/PickMyBrainButton.astro  # Update default button text
src/config.ts                  # Update site description
```

### Optional New Files (1)
```
src/components/ServiceCard.astro  # Reusable service card component
```

---

## 15. Design System Reference

### Colors (CSS Variables)
```css
--background: #2d2d2d   /* Dark gray */
--foreground: #e8e8e8   /* Light gray */
--accent: #ff6b4a       /* Coral/orange - use for CTAs, headings, links */
--muted: #808080        /* Mid gray - use for secondary text */
--border: #3d3d3d       /* Darker gray - use for card borders */
```

### Typography
```css
font-family: font-mono  /* Monospace throughout */
```

**Heading Sizes:**
- H1: `text-5xl` (3rem / 48px desktop, 2.5rem / 40px mobile)
- H2: `text-2xl` (1.5rem / 24px)
- H3: `text-lg` (1.125rem / 18px)
- Body: `text-base` (1rem / 16px)
- Small: `text-sm` (0.875rem / 14px)

### Spacing
- Section padding: `py-12` (3rem / 48px)
- Hero padding: `py-20` (5rem / 80px)
- Card padding: `p-6` (1.5rem / 24px)
- Element spacing: `mb-6`, `mb-8` (1.5rem, 2rem)

### Border Radius
- Cards: `rounded-lg` (0.5rem / 8px)
- Buttons: `rounded-lg` or custom pushable button styles

### Animations
```css
.fade-up {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeUp 0.6s ease-out forwards;
}
```

**Animation Delays (stagger):**
- First element: `style="animation-delay: 0.1s"`
- Second element: `style="animation-delay: 0.2s"`
- Third element: `style="animation-delay: 0.3s"`
- Increment by 0.1s for each subsequent element

### Button States
**Pushable Button:**
- Idle: 3D effect with shadow
- Hover: Lift up 2px, brightness 110%
- Active: Press down

**Simple Button:**
- Idle: Background rgba(255, 107, 74, 0.1), border accent color
- Hover: Background rgba(255, 107, 74, 0.2), translate up 2px, shadow

---

## 16. Copy Variations (Optional A/B Testing)

### Hero Headline Alternatives
1. **Current:** "iOS Engineer & Agentic Automation Specialist."
2. **Alt 1:** "Senior iOS Engineer. Agentic Automation Expert."
3. **Alt 2:** "iOS + AI Agents + Developer Tooling."

**Recommendation:** Use Current (most grammatically clean)

### CTA Button Text Alternatives
1. **Current:** "Book Engineering Session"
2. **Alt 1:** "Book a Session"
3. **Alt 2:** "Schedule Time"

**Recommendation:** Use Current (clearest value)

### Services Page Headline Alternatives
1. **Current:** "Drop-In Engineering Sessions"
2. **Alt 1:** "Focused Engineering Sessions"
3. **Alt 2:** "No-Retainer Engineering Sessions"

**Recommendation:** Use Current (matches offer doc, memorable)

---

## 17. Content Sources & Attribution

### Research Citations (from offer doc)
- Pair programming improves design quality (referenced but not linked)
- Discovery/roadmapping containers are proven on-ramps (referenced)
- Small PRs vs. marathons (referenced)

**Note:** These are mentioned as tooltips/footnotes in original offer doc. For website V1, keep references subtle (no footnotes needed), add links later if desired.

### Proof Points
- WhisperBoard: 888★ GitHub, 50k+ downloads, 4.8★ App Store
- mcp-browser-use: 767★ GitHub
- VibeSwitch: Privacy-first iOS keyboard
- Uber: Millions of downloads
- Codementor: Many sessions (exact count unknown, use "many" or link to profile)

---

## 18. Maintenance Plan

### Monthly
- [ ] Update GitHub stars count (WhisperBoard, mcp-browser-use)
- [ ] Update download counts if significant change
- [ ] Review booking conversion rate
- [ ] Add new blog posts to "Recent Posts"

### Quarterly
- [ ] Review service pricing (€200/hr still competitive?)
- [ ] Add case studies if client permits
- [ ] Update "Typical Outcomes" section with new examples
- [ ] Review FAQ section, add new common questions

### Annually
- [ ] Full content audit
- [ ] Check all external links still valid
- [ ] Update bio/experience (years count, new projects)
- [ ] Consider adding new service tiers

---

## 19. Success Metrics

### Week 1
- Services page views: Target 50+
- Booking clicks: Target 5+
- Actual bookings: Target 1+

### Month 1
- Services page views: Target 200+
- Booking conversion rate: Target 3-5%
- Actual clients: Target 2-3
- Testimonials collected: Target 2

### Q1 2025 (March 31)
- Total clients: Target 5-10
- Total revenue: Target €5K-€10K
- Return clients: Target 2+
- Case studies published: Target 2-3

---

## Implementation Notes

### Build Command
```bash
npm run build
```

### Dev Server
```bash
npm run dev
```

### Deployment
- Site deploys via Nixpacks (per nixpacks.toml in repo)
- Likely auto-deploys on git push to main
- Verify deployment URL: https://www.tarasenko.dev/

### Environment Variables
- `PUBLIC_GOOGLE_SITE_VERIFICATION` (optional)
- Plausible analytics configured in Layout.astro (no env var needed)

---

## Final Pre-Launch Checklist

### Content Quality
- [ ] All copy proofread (no typos)
- [ ] All links tested (internal and external)
- [ ] All images have alt text
- [ ] Pricing consistent across all pages (€200/hr)
- [ ] No over-promises (React/Next.js expertise removed)
- [ ] Social proof accurate (GitHub stars, downloads)

### Technical Quality
- [ ] Responsive on mobile (tested)
- [ ] Responsive on tablet (tested)
- [ ] Animations work smoothly
- [ ] No console errors
- [ ] No Astro build warnings
- [ ] Pagefind search still works after build
- [ ] RSS feed validates

### SEO
- [ ] Page titles descriptive and unique
- [ ] Meta descriptions under 160 characters
- [ ] OG images generated correctly
- [ ] Sitemap updated
- [ ] Canonical URLs correct

### Analytics
- [ ] Plausible tracking code present
- [ ] Test event fires (book button click)
- [ ] Page views tracking

---

## Post-Implementation: Next Steps

### Immediate (Week 1-2)
1. Share /services page on X (Igor's account)
2. Update LinkedIn profile with new positioning
3. Email existing contacts with "new service offering"
4. Post in relevant communities (iOS dev, AI engineering)

### Short-term (Month 1)
5. Publish new blog post: "Why I'm Offering Drop-In Engineering Sessions"
6. Create Loom walkthrough of services page
7. Add first testimonial from client
8. Consider adding /services to nav CTA

### Medium-term (Q1 2025)
9. Add free tier (newsletter signup) if audience grows
10. Add workshop tier (€3K) if demand exists
11. Create case studies page
12. Build email sequence for leads who don't book

---

## Appendix: Original Offer Doc Comparison

### What We Kept
- ✅ Core offer structure (Drop-In Engineering Co-Pilot)
- ✅ Pricing (€200/hr, packs, guarantee)
- ✅ 4-step process (book, kickoff, work, wrap)
- ✅ Typical outcomes framework
- ✅ Transparent, no-BS tone

### What We Changed
- ❌ Removed: WebRTC/SIP (no proof)
- ❌ Removed: Generic React/Next.js performance (not specialist)
- ❌ Removed: Auth flows (too vague)
- ✅ Added: iOS-specific outcomes
- ✅ Added: Agentic engineering emphasis
- ✅ Added: Developer tooling category
- ✅ Sharpened: "Who it's for" to match actual expertise

### What We Enhanced
- ✅ Added proof points (GitHub stars, downloads)
- ✅ Made positioning explicit (iOS + Agentic + Tooling)
- ✅ Added FAQ with honest limitations
- ✅ Created visual service cards for homepage
- ✅ Integrated with existing blog content (repo readiness, agentic engineering)

---

**END OF IMPLEMENTATION PLAN**

Total estimated implementation time: 4-6 hours
Priority: HIGH (Q1 2025 goal: land 2 enterprise AI projects)
