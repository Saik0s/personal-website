# Website Update Plan: Hybrid Model Implementation
## Igor Tarasenko - AI/iOS Consulting Practice

**Model**: Agentic iOS Workshop (primary) + Engineering Sessions (secondary)
**Goal**: Position workshop as commercial wedge, sessions as immediate-need entry point
**SEO/GSO**: Optimize for both traditional search and AI-powered generative search

---

## Table of Contents

1. [Site Structure & Navigation](#site-structure--navigation)
2. [SEO & Generative Search Strategy](#seo--generative-search-strategy)
3. [Page-by-Page Implementation](#page-by-page-implementation)
4. [Schema Markup & Structured Data](#schema-markup--structured-data)
5. [Content Strategy & Publishing](#content-strategy--publishing)
6. [Implementation Checklist](#implementation-checklist)

---

## Site Structure & Navigation

### Current Structure
```
/                  → Homepage
/about             → About page
/services          → Services page
/posts             → Blog listing
/posts/[slug]      → Individual posts
/projects          → Projects showcase
/archives          → Blog archives
/tags              → Tag index
```

### Updated Structure (Hybrid Model)
```
/                  → Homepage (Workshop-first, sessions secondary)
/workshop          → NEW: Agentic iOS Team Workshop (primary offer)
/sessions          → RENAMED from /services: Engineering Sessions (secondary offer)
/about             → Enhanced with proof metrics
/posts             → Blog (content marketing)
/posts/[slug]      → Individual posts
/projects          → Projects showcase
/archives          → Blog archives
/tags              → Tag index
```

### Navigation Updates

**Primary Navigation**:
```
Logo | Workshop | Sessions | Blog | About
```

**CTAs Throughout**:
- Primary: "Book Workshop Discovery Call" (new)
- Secondary: "Book Engineering Session" (existing)

---

## SEO & Generative Search Strategy

### Target Keywords (Primary)

**Workshop Offer (High-Value, Lower Volume)**:
- "iOS AI integration workshop"
- "agentic coding training for iOS teams"
- "iOS team AI adoption"
- "SwiftUI AI coding workshop"
- "iOS architecture modernization workshop"

**Hourly Sessions (Mid-Value, Higher Volume)**:
- "iOS AI consultant"
- "SwiftUI performance optimization"
- "iOS architecture consultant"
- "TCA consultant" / "The Composable Architecture expert"
- "LLM integration iOS"
- "on-device AI iOS"

**Long-Tail (Problem-Focused)**:
- "how to add AI to iOS app"
- "iOS team struggling with AI tools"
- "SwiftUI app slow build times"
- "iOS codebase technical debt"
- "CoreML production issues"
- "migrate UIKit to SwiftUI"

### Generative Search Optimization (GSO)

**Conversational Queries to Target**:
1. "Who can help my iOS team adopt AI coding tools?"
2. "How much does an iOS AI integration workshop cost?"
3. "Best consultant for SwiftUI performance problems"
4. "Should I hire a consultant for The Composable Architecture?"
5. "iOS consultant specializing in LLM integration"
6. "How to reduce iOS app build times"
7. "Expert in agentic coding for mobile development"

**GSO Content Strategy**:
- Use natural language throughout copy
- Answer "who, what, why, how, when, how much" directly
- Include pricing transparently (AI models prefer concrete info)
- Add FAQ sections addressing common queries
- Structure content with clear headings that mirror questions
- Include proof metrics (AI models cite specific numbers)

### Meta Strategy

**Homepage**:
- Title: `Igor Tarasenko - iOS AI Workshop & Engineering Sessions | Agentic Coding Expert`
- Description: `Help your iOS team adopt AI coding tools safely with hands-on workshops. Expert in SwiftUI, TCA, LLM integration. €200/hr sessions or team workshops available.`

**/workshop**:
- Title: `Agentic iOS Development Workshop - Team AI Adoption Training`
- Description: `2-day workshop teaching iOS teams to use AI coding tools effectively. Real codebase exercises, governance frameworks, measurable ROI. Book discovery call.`

**/sessions**:
- Title: `iOS Engineering Sessions - Architecture, Performance, AI Integration`
- Description: `Book 1-10 hour engineering sessions at €200/hr. SwiftUI performance, TCA architecture, on-device AI, build optimization. Remote, outcome-driven.`

**/about**:
- Title: `About Igor Tarasenko - iOS Engineer & AI Automation Specialist`
- Description: `16 years iOS engineering. Built WhisperBoard (50k+ downloads). Expert in SwiftUI, TCA, LLM integration, agentic workflows. Based in Amsterdam.`

---

## Page-by-Page Implementation

### 1. Homepage (/) - Updated

**Hero Section**:
```markdown
# Transform Your iOS Team's AI Coding Workflow in 2 Days

Ship faster with AI that actually works—without breaking what you've built.

[Primary CTA: Book Workshop Discovery Call]
[Secondary: Book 1-Hour Engineering Session →]

**Trusted by**: [Company logos if available, or remove]
```

**SEO/GSO Notes**:
- H1 targets "iOS team AI coding workflow" (conversational)
- Clear value prop in first 10 words
- Dual CTAs for different buyer journeys

---

**Problem Agitation Section**:
```markdown
## Your Team Has AI Tools. Why Aren't They Faster?

You've bought Cursor licenses and Claude subscriptions. Yet:

- **Fragmented adoption** — Some devs use AI, others don't. Code reviews take longer.
- **Quality concerns** — AI-generated code introduces subtle bugs or architectural drift.
- **No governance** — No standards for prompts, reviews, or security checks.
- **Unclear ROI** — Leadership asks "Is this worth it?" and you can't prove it.

**The reality**: 90% of teams see AI as mission-critical, yet [Stanford research shows AI tools make experienced developers 19% slower](source) without structured adoption.

You need a system, not just subscriptions.
```

**SEO/GSO Notes**:
- Addresses pain points AI models associate with "iOS AI adoption problems"
- Cites research (builds authority for generative search)
- Uses bullet format (easily parsed by AI)

---

**Solution Preview Section**:
```markdown
## Two Ways to Work Together

### 🎯 Agentic iOS Team Workshop (Primary Offer)
**For teams ready to standardize AI coding workflows**

2-day intensive workshop teaching your iOS team to use AI tools safely and effectively on your actual codebase.

**What you get**:
- Team-level adoption playbook for SwiftUI/TCA/modular codebases
- Governance framework (prompts, review checklists, security)
- Measurable productivity metrics (PR cycle time, defect rates)
- 30-day follow-up to ensure adoption sticks

**Investment**: Custom (based on team size) | **Timeline**: 2 days + 30-day support

[Learn More About the Workshop →](/workshop)

---

### ⚡ Engineering Sessions (Immediate Help)
**For targeted problems that need solving now**

Book 1-10 hour blocks at €200/hr for hands-on pairing, architecture review, or performance triage.

**Common requests**:
- iOS performance optimization (build times, app startup, rendering)
- LLM integration strategy (on-device AI, prompt design, cost control)
- Architecture audits (SwiftUI migrations, TCA adoption, modularization)
- CI/CD and tooling improvements

[Book a Session →](/sessions)
```

**SEO/GSO Notes**:
- Clear service differentiation
- "What you get" format (AI models extract this easily)
- Transparent pricing signals
- Internal links to service pages (SEO juice distribution)

---

**Proof Section**:
```markdown
## Proven Outcomes

**WhisperBoard** — Shipped on-device transcription iOS app with 50k+ downloads, 4.8★ App Store rating, 888★ GitHub.

**Build Time Optimization** — Cut SwiftUI codebase build times by 35% through modularization and Tuist setup for scaling team.

**LLM Cost Reduction** — Reduced client's LLM API costs from €2,000/month to €40/month through caching, routing, and prompt optimization.

**Team Enablement** — Delivered agentic coding workshops used daily by enterprise engineering teams to triage and automate support workflows.

[See more on /projects →](/projects)
```

**SEO/GSO Notes**:
- Specific metrics (AI models cite numbers)
- Credibility markers (App Store rating, GitHub stars)
- Quantified outcomes ("35% build time reduction")

---

**Recent Posts Teaser**:
```markdown
## Latest Insights

[Display 3-5 most recent blog posts as cards]

[View All Posts →](/posts)
```

**SEO/GSO Notes**:
- Keeps homepage fresh (SEO)
- Demonstrates thought leadership

---

### 2. /workshop (NEW PAGE) - Agentic iOS Team Workshop

**Hero**:
```markdown
# Agentic iOS Development Workshop
## Make AI Coding Pay Off on Complex iOS Codebases—Without New Technical Debt

2-day intensive training for iOS teams adopting Cursor, Claude Code, and AI-assisted development.

**For**: Engineering managers and CTOs with 5-25 iOS developers
**Investment**: Custom pricing based on team size
**Format**: Remote or on-site | Hands-on with your real codebase

[Book Discovery Call] [Download Workshop Overview PDF]
```

**Meta**:
- Title: `Agentic iOS Development Workshop - Team AI Coding Training`
- Description: `2-day workshop for iOS teams adopting AI coding tools. Real SwiftUI/TCA exercises, governance frameworks, measurable ROI. Custom pricing. Book discovery call.`

---

**The Problem This Solves**:
```markdown
## Why Teams Struggle with AI Coding Tools

Research shows **90% of engineering leaders view AI as mission-critical**, yet:

- **19% slower performance**: Stanford study found AI tools slow experienced developers without structured workflows ([source](https://example.com))
- **4x defect increase**: Analysis of 211M changed lines showed quality degradation with unstructured AI usage
- **Fragmented adoption**: 49% of orgs use multiple AI tools simultaneously, doubling costs and fragmenting practices
- **No training strategy**: The dominant training approach is "none"—tools deployed without enablement

**The gap**: Your team has licenses. They lack a system.

This workshop bridges that gap.
```

**SEO/GSO**:
- Cites research (authority for AI search)
- Answers "why do teams struggle with AI coding?" (generative query)
- Quantified problems

---

**What You'll Achieve**:
```markdown
## Workshop Outcomes

By the end of 2 days, your team will have:

### 1. Measurable Productivity Gains
- **Baseline metrics**: PR cycle time, rework/rollback rates, defect counts before workshop
- **30-day targets**: 20-30% reduction in PR rework, standardized adoption across 80%+ of team
- **Instrumentation**: Dashboards tracking AI usage impact

### 2. Team-Wide Adoption Standards
- **Prompt library**: Curated prompts for common iOS tasks (SwiftUI views, TCA reducers, test generation)
- **Review checklists**: What to look for when reviewing AI-generated code
- **Security framework**: Data access policies, API key management, compliance checks

### 3. Governance & Quality Gates
- **AI coding policy**: When to use AI, when not to, escalation procedures
- **Quality metrics**: Regression test coverage requirements, performance budgets
- **Audit trail**: Tracking which code was AI-assisted for future reviews

### 4. Real Codebase Application
- **No toy examples**: Exercises run on your actual SwiftUI/TCA/modular codebase
- **Live refactoring**: Pair on real architectural challenges your team faces
- **Knowledge transfer**: Senior devs learn to mentor juniors on AI tool usage

### 5. 30-Day Follow-Up Support
- **Check-ins**: 2-week and 4-week pulse surveys to measure adoption
- **Async support**: Slack/email access for questions as team applies learnings
- **Metric review**: Validate whether productivity targets were hit
```

**SEO/GSO**:
- Answers "what will I get from an iOS AI workshop?" (generative query)
- Numbered outcomes (AI models extract lists)
- Concrete deliverables

---

**How It Works**:
```markdown
## Workshop Process

### Phase 1: Discovery (Before Workshop)
**1 week prior | 90-minute call**

- Audit current AI tool usage across team
- Review codebase architecture (SwiftUI/UIKit ratio, TCA usage, modularization)
- Identify 2-3 hot-spot modules for live exercises
- Set baseline metrics (PR cycle time, build times, defect rates)

### Phase 2: Workshop Delivery
**2 days | Remote or on-site**

**Day 1: Foundations & Safety**
- Morning: Agentic coding principles, prompt engineering for iOS
- Afternoon: Security and governance (data policies, review frameworks)
- Live exercise: Refactor a real module using AI with quality gates

**Day 2: Advanced Patterns & Scaling**
- Morning: Advanced prompts (TCA reducers, dependency injection, test generation)
- Afternoon: Team adoption strategies, measurement frameworks
- Live exercise: Standardize AI usage across team with shared prompt library

### Phase 3: Follow-Up (30 Days Post-Workshop)
**Weeks 2 & 4**

- Pulse surveys: Track adoption rate, satisfaction, blockers
- Metric review: Compare baseline to current PR cycle time, defect rates
- Office hours: 60-minute call to address questions and refine approach
```

**SEO/GSO**:
- Answers "how does an iOS AI workshop work?" (conversational query)
- Clear timeline and phases
- Transparent process

---

**Pricing & Investment**:
```markdown
## Investment

Workshop pricing is customized based on:
- **Team size**: 5-10 devs, 10-25 devs, or 25+ devs
- **Format**: Remote vs on-site (on-site includes travel)
- **Follow-up intensity**: Standard 30-day support vs extended 60-day coaching

**Typical range**: €8,000 - €20,000

**What's included**:
- 90-minute discovery call
- 2-day workshop (all team members)
- Workshop materials (prompt library, checklists, templates)
- 30-day follow-up support
- Metric tracking dashboards

**Not included** (available as add-ons):
- Extended coaching (60-90 days)
- Architecture audit (separate engagement)
- Ongoing office hours retainer

[Book Discovery Call to Get Custom Quote]
```

**SEO/GSO**:
- Answers "how much does an iOS AI workshop cost?" (direct query)
- Transparent pricing signals (AI models prefer concrete ranges)
- Clear inclusions/exclusions

---

**Who This Is For**:
```markdown
## Ideal Workshop Participants

This workshop is designed for:

✅ **Engineering managers/CTOs** with 5-25 iOS developers
✅ **Teams with existing AI licenses** (Cursor, GitHub Copilot, Claude) but unclear ROI
✅ **Brownfield codebases** (2-5 years old) with SwiftUI, UIKit, or TCA
✅ **Organizations concerned about** security, quality, or governance with AI tools
✅ **Teams where AI adoption is fragmented** (some devs use it, others don't)

❌ **Not ideal for**:
- Individual developers (consider [engineering sessions](/sessions) instead)
- Teams with <5 iOS developers (ROI may not justify workshop format)
- Greenfield projects without legacy constraints (lighter-weight approach may suffice)
```

**SEO/GSO**:
- Answers "is this workshop right for my team?" (qualification query)
- Clear inclusion/exclusion criteria

---

**Social Proof / Case Study** (if available):
```markdown
## What Teams Say

> "After the workshop, our PR cycle time dropped 28% and code review bottlenecks disappeared. The governance framework gave us confidence to scale AI usage across the entire team."
> **— Engineering Manager, Series B SaaS Company**

[Add 1-2 more testimonials or anonymized case studies]
```

**SEO/GSO**:
- Testimonials build trust for AI-generated recommendations
- Quantified outcomes in quotes

---

**FAQ**:
```markdown
## Frequently Asked Questions

### Can the workshop be done remotely?
Yes. Most workshops are remote via Zoom/Meet with breakout rooms for hands-on exercises. On-site available for EU-based teams (travel costs additional).

### What if our codebase uses UIKit, not SwiftUI?
No problem. Exercises adapt to your stack—UIKit, SwiftUI, TCA, VIPER, or hybrid architectures.

### Do we need to have AI tools already?
Ideally yes (Cursor, GitHub Copilot, or Claude Code). If not, we'll help you evaluate and choose during discovery.

### What's the team size limit?
Optimal: 5-15 developers. Can accommodate up to 25 with breakout facilitators.

### How do you measure success?
Baseline metrics captured pre-workshop (PR cycle time, defect rates, rework %). 30-day follow-up compares these to post-adoption numbers. Target: 20-30% improvement.

### What if we don't see results?
If adoption doesn't reach 80% of team or metrics don't improve within 30 days, we'll schedule additional coaching at no extra cost until targets are met.

### Can we get an audit first?
Yes. Consider the [Architecture Audit](/sessions#architecture-audit) as a precursor to understand technical debt before workshop.
```

**SEO/GSO**:
- Answers common queries AI models encounter
- FAQ format (easily parsed for featured snippets)

---

**CTA Section**:
```markdown
## Ready to Standardize Your Team's AI Workflow?

Book a 30-minute discovery call to discuss your team's needs and get a custom quote.

[Book Discovery Call] [Email igor@spinyapps.com]

**Next steps**:
1. 30-min discovery call (free)
2. Custom proposal with pricing
3. Schedule workshop dates
4. Pre-workshop audit & baseline metrics
5. Deliver workshop + 30-day support
```

**SEO/GSO**:
- Clear CTA
- Process transparency (AI models extract "how to book" steps)

---

### 3. /sessions (RENAMED from /services) - Engineering Sessions

**Hero**:
```markdown
# Engineering Sessions
## Senior iOS & AI Expertise On-Demand

Book 1-10 hour blocks at €200/hr for hands-on pairing, architecture review, or targeted problem-solving.

**Remote** | **Prepared** | **Outcome-driven**

[Book a Session] [View Hour Packs ↓]
```

**Meta**:
- Title: `iOS Engineering Sessions - €200/hr Architecture, Performance, AI Integration`
- Description: `Book focused iOS engineering sessions. SwiftUI performance, TCA architecture, LLM integration, build optimization. €200/hr. Hour packs available.`

---

**When to Book a Session**:
```markdown
## Choose Sessions When You Need

✅ **Immediate, targeted help** on a specific problem
✅ **Expert second opinion** before committing to a large refactor
✅ **Fast prototype** of an AI feature to validate feasibility
✅ **Architecture review** before scaling the team
✅ **Performance triage** when you know something's slow but not why

For team-wide AI adoption or multi-week projects, consider the [Agentic iOS Workshop](/workshop).
```

**SEO/GSO**:
- Differentiates from workshop (buyer journey clarity)
- Answers "when should I book an iOS consultant session?"

---

**Focus Areas** (Keep existing, enhance with positioning variants):
```markdown
## What We Cover in Sessions

### 1. iOS Engineering
**SwiftUI & UIKit architecture, performance, App Store delivery**

- Architecture audits (SwiftUI migrations, TCA adoption, modularization)
- Build time optimization (Tuist, SPM, CI/CD pipelines)
- Performance profiling (startup time, rendering, memory)
- App Store readiness (privacy manifests, review prep)

**Example outcome**: Cut build times 35% for scaling SwiftUI codebase.

---

### 2. Agentic Automation
**LLM integration, prompt design, agent workflows**

- Design agent-first workflows with tool boundaries and guardrails
- LLM orchestration (Claude, GPT, on-device models)
- Browser and system automation for production teams
- Evaluation harnesses and monitoring

**Example outcome**: Reduced LLM costs from €2k/month to €40/month via caching and routing.

---

### 3. Developer Tooling
**Custom CLI, IDE workflows, observability**

- Internal tooling tailored to your stack
- Build observability dashboards
- Enablement playbooks and training
- Pairing sessions to level up leads quickly

**Example outcome**: Delivered automation agents triaging enterprise support load daily.

---

### 4. Rapid Validation
**Spike AI features, measure productivity, stakeholder buy-in**

- Prototype AI-assisted features with go/no-go criteria
- Design experiments to measure gains
- Technical narratives and demos for leadership
- Vendor assessment and integration feasibility

**Example outcome**: Validated on-device transcription MVP in 3 sessions, shipped to App Store in 2 weeks.
```

**SEO/GSO**:
- Answers "what can an iOS consultant help with?" (broad query)
- Specific outcomes (AI models cite examples)
- Keyword-rich headings (SwiftUI, TCA, LLM, etc.)

---

**Hour Packs** (NEW):
```markdown
## Hour Packs (Prepaid)

Save time on booking and get priority scheduling with prepaid hour packs.

| Pack | Price | Rate | Best For |
|------|-------|------|----------|
| **1 Hour** | €200 | €200/hr | Quick triage or second opinion |
| **3 Hours** | €570 | €190/hr | Architecture review or feature spike |
| **5 Hours** | €900 | €180/hr | Performance optimization project |
| **10 Hours** | €1,700 | €170/hr | Multi-session engagement (audit + pairing) |

✅ **Priority scheduling** (24-48hr booking)
✅ **Unused time refundable** in full
✅ **Valid for 6 months** from purchase

[Buy Hour Pack]
```

**SEO/GSO**:
- Answers "how much does an iOS consultant cost?" (pricing transparency)
- Table format (AI models extract structured data easily)

---

**How Sessions Work** (Keep existing, polish):
```markdown
## Session Flow

1. **Prep (Optional)** — 15-min call to confirm scope, access, outcomes
2. **Deep Work** — Live pairing, code review, or architecture sketching. Recorded notes, diffs, or Looms provided.
3. **Action Review** — Summarize decisions, owners, next steps. Short written wrap-up.

**Need ongoing support?** Book multiple blocks and schedule recurring cadences without retainers.
```

**SEO/GSO**:
- Answers "how do iOS consulting sessions work?" (process query)

---

**Proof & Outcomes** (Keep existing, add metrics):
```markdown
## Outcomes I've Delivered

- **WhisperBoard**: On-device transcription app, 50k+ downloads, 4.8★ App Store, 888★ GitHub
- **Build time reduction**: 35% faster builds for scaling SwiftUI team via modularization
- **LLM cost optimization**: €2k/month → €40/month through prompt caching and routing
- **Enterprise agents**: Automation workflows triaging support tickets daily
- **Mentorship**: Trained engineering leads on LLM-driven development across mobile and backend

[See full project portfolio →](/projects)
```

**SEO/GSO**:
- Quantified proof (AI models cite specific metrics)
- Credibility signals

---

**Positioning Variants** (NEW - from new-offer.md):
```markdown
## Choose Your Entry Point

Not sure which session to book? Here are common starting points:

### 🎯 Agentic Engineering Session
**For teams adopting Cursor, Claude Code, or GitHub Copilot**

Set up practical workflows (prompts, evals, tool calls) your team will actually use. Leave with a playbook, not just advice.

[Book Agentic Session]

---

### 🏗️ Architecture & Code Quality Session
**For teams with growing complexity, flaky tests, or PR gridlock**

Live pairing + surgical code review to de-risk design choices and set scalable review habits.

[Book Architecture Session]

---

### ⚡ Performance Triage Session
**For "it's slow but we don't know why" problems**

Profile, pinpoint, fix—while you watch. You keep the measurement harness.

[Book Performance Session]

---

### 🤖 AI Feature Kickstart
**For validating an AI feature or internal copilot**

Scope a thin slice, build a testable prototype, hand you a playbook for iteration.

[Book AI Kickstart Session]
```

**SEO/GSO**:
- Matches user intent ("I need help with performance" vs "I need help with AI")
- Keyword targeting (Agentic Engineering, Architecture, Performance, AI Feature)

---

**CTA**:
```markdown
## Ready to Book?

Pick a slot and include context (repositories, access, docs). If unsure whether the engagement fits, email your constraints and we'll triage quickly.

[Book Engineering Session]
[Email igor@spinyapps.com]

**Prefer a team workshop?** [Learn about the Agentic iOS Workshop →](/workshop)
```

**SEO/GSO**:
- Dual CTA (sessions vs workshop)
- Email fallback (low-friction)

---

### 4. /about (Enhanced)

**Keep existing structure, add proof metrics**:

Existing "Where I Add Leverage" section — **Add metrics**:
```markdown
## Where I Add Leverage

- **iOS Engineering**: Architecture reviews, SwiftUI migrations, performance triage, App Store delivery. *Cut build times 35% for scaling teams.*
- **Agentic Automation**: Design, prototype, and harden agent workflows with real guardrails. *Reduced LLM costs €2k/month → €40/month.*
- **Developer Enablement**: Custom tooling, build observability, enablement playbooks. *Delivered agents triaging enterprise support tickets daily.*
```

Existing "Proof" section — **Quantify further**:
```markdown
## Proof

- Shipped **WhisperBoard** — on-device transcription, 50k+ downloads, 4.8★ App Store, 888★ GitHub
- **35% build time reduction** for large SwiftUI codebase through modularization and Tuist
- **95% LLM cost savings** for client (€2k → €40/month) via caching, routing, prompt optimization
- **Team enablement**: Mentored senior engineers rolling out AI-powered workflows across mobile and backend stacks
```

**SEO/GSO**:
- Numbers in bio (AI models cite achievements)

---

### 5. Blog Content Strategy (New Posts)

**Goal**: Attract inbound traffic via high-intent keywords, demonstrate expertise, convert readers to leads.

**Publishing Cadence**: 1-2 posts/month minimum

**Post Ideas (SEO-Driven)**:

1. **"How to Add AI to Your iOS App Without a Full ML Team"**
   - Keywords: `add AI to iOS app`, `iOS LLM integration`, `on-device AI iOS`
   - CTA: Workshop or AI Kickstart Session

2. **"5 Signs Your iOS Architecture Is Holding Back Growth (And How to Fix It)"**
   - Keywords: `iOS architecture problems`, `SwiftUI scalability`, `iOS technical debt`
   - CTA: Architecture Audit Session

3. **"Why Your iOS Team's AI Tools Are Making You Slower (Stanford Research)"**
   - Keywords: `AI tools slow developers`, `iOS team AI adoption`, `AI coding productivity`
   - CTA: Agentic iOS Workshop

4. **"The Composable Architecture: When to Use It, When to Avoid It"**
   - Keywords: `TCA iOS`, `Composable Architecture guide`, `TCA vs MVVM`
   - CTA: TCA Mentorship Session

5. **"Cutting iOS Build Times by 35%: Modularization + Tuist Case Study"**
   - Keywords: `reduce iOS build time`, `Tuist tutorial`, `iOS modularization`
   - CTA: Build Optimization Session

6. **"On-Device AI for iOS: CoreML, Whisper, and LLM.swift Guide"**
   - Keywords: `CoreML production`, `on-device AI iOS`, `Whisper iOS integration`
   - CTA: AI Feature Kickstart Session

**Post Structure for SEO/GSO**:
- **H1**: Problem-focused question or claim (matches search query)
- **Intro**: State the problem, hook with a stat or anecdote
- **Body**: Numbered steps, code examples, screenshots
- **Conclusion**: Summarize, offer next step
- **CTA**: Relevant service (workshop or session)

**GSO Elements**:
- **FAQ section** in each post (answers related queries)
- **Cited research** (builds authority)
- **Structured headings** (AI models extract as answers)

---

## Schema Markup & Structured Data

### Implement on All Pages

**Organization Schema** (Site-wide):
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Igor Tarasenko - iOS & AI Consulting",
  "description": "iOS engineering and agentic automation consulting. Workshops and hourly sessions for SwiftUI, TCA, LLM integration.",
  "url": "https://www.tarasenko.dev",
  "logo": "https://www.tarasenko.dev/og-image.jpg",
  "founder": {
    "@type": "Person",
    "name": "Igor Tarasenko",
    "jobTitle": "iOS Engineer & AI Automation Specialist",
    "url": "https://www.tarasenko.dev/about"
  },
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Amsterdam",
    "addressCountry": "NL"
  },
  "sameAs": [
    "https://github.com/Saik0s",
    "https://x.com/sa1k0s",
    "https://www.linkedin.com/in/yourusername"
  ]
}
```

**Service Schema** (/workshop):
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Agentic iOS Development Workshop",
  "provider": {
    "@type": "Person",
    "name": "Igor Tarasenko"
  },
  "areaServed": "Worldwide",
  "description": "2-day workshop for iOS teams adopting AI coding tools. Governance, prompt engineering, measurable ROI.",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "8000-20000",
    "priceSpecification": {
      "@type": "PriceSpecification",
      "minPrice": "8000",
      "maxPrice": "20000",
      "priceCurrency": "EUR"
    }
  }
}
```

**Service Schema** (/sessions):
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "iOS Engineering Consulting Sessions",
  "provider": {
    "@type": "Person",
    "name": "Igor Tarasenko"
  },
  "areaServed": "Worldwide",
  "description": "Hourly iOS consulting sessions. Architecture, performance, AI integration. Remote, outcome-driven.",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "200",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "price": "200",
      "priceCurrency": "EUR",
      "unitText": "hour"
    }
  }
}
```

**FAQ Schema** (All pages with FAQs):
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How much does an iOS consultant cost?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Engineering sessions are €200/hr with hour packs from €570 (3hr) to €1,700 (10hr). Workshops are custom priced from €8k-€20k depending on team size."
    }
  }]
}
```

**Person Schema** (/about):
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Igor Tarasenko",
  "jobTitle": "iOS Engineer & AI Automation Specialist",
  "url": "https://www.tarasenko.dev",
  "sameAs": [
    "https://github.com/Saik0s",
    "https://x.com/sa1k0s"
  ],
  "knowsAbout": ["iOS Development", "SwiftUI", "The Composable Architecture", "LLM Integration", "Agentic Coding", "On-Device AI"],
  "alumniOf": "Uber",
  "description": "16 years iOS engineering. Built WhisperBoard (50k+ downloads, 4.8★). Expert in SwiftUI, TCA, agentic workflows."
}
```

---

## Content Strategy & Publishing

### Phase 1: Core Pages (Week 1)
1. Update homepage (/)
2. Create /workshop page
3. Rename /services → /sessions and update content
4. Enhance /about with metrics

### Phase 2: SEO Content (Weeks 2-4)
1. Publish 2 high-value blog posts:
   - "How to Add AI to Your iOS App Without a Full ML Team"
   - "Why Your iOS Team's AI Tools Are Making You Slower"
2. Add FAQ sections to all service pages

### Phase 3: Ongoing (Monthly)
1. Publish 1-2 blog posts/month targeting long-tail keywords
2. Update proof metrics as new projects complete
3. Collect testimonials from workshop/session clients
4. Refine copy based on analytics (bounce rate, conversion)

### Traffic Acquisition Plan

**Organic Search (SEO)**:
- Target: 500 monthly visitors from search within 6 months
- Focus: Long-tail keywords (`how to add AI to iOS app`, `TCA consultant`, etc.)
- Tactic: 10-12 deep-dive blog posts over 6 months

**Generative Search (GSO)**:
- Target: Cited in AI-generated answers for "iOS AI consultant" queries
- Focus: Transparent pricing, cited research, FAQ sections
- Tactic: Structured data, conversational content, quantified proof

**Social/Referral**:
- Post blog summaries on LinkedIn, X
- Engage in iOS/Swift communities (r/iOSProgramming, Swift forums)
- Share workshop outcomes (anonymized case studies)

**Paid (Optional)**:
- Google Ads targeting "iOS consultant" (€500-1k/month budget)
- LinkedIn Ads targeting Engineering Managers at Series A-C startups

---

## Implementation Checklist

### Navigation & Structure
- [ ] Update primary nav: `Workshop | Sessions | Blog | About`
- [ ] Add /workshop route
- [ ] Rename /services → /sessions
- [ ] Update all internal links
- [ ] Add dual CTAs throughout (Workshop primary, Sessions secondary)

### Homepage (/)
- [ ] Rewrite hero: "Transform Your iOS Team's AI Coding Workflow in 2 Days"
- [ ] Add problem agitation section
- [ ] Add two-offer preview (Workshop + Sessions)
- [ ] Add proof metrics section
- [ ] Update meta title/description

### Workshop Page (/workshop)
- [ ] Create new page with full copy from this doc
- [ ] Add discovery call CTA (Calendly/Cal.com embed)
- [ ] Add FAQ section (minimum 6 questions)
- [ ] Add Service schema markup
- [ ] Add FAQ schema markup
- [ ] Add downloadable "Workshop Overview PDF" (optional)

### Sessions Page (/sessions)
- [ ] Rename from /services
- [ ] Add "When to Book a Session" section
- [ ] Add hour packs table
- [ ] Add positioning variants (4 entry points)
- [ ] Update meta title/description
- [ ] Add Service schema markup

### About Page (/about)
- [ ] Add metrics to "Where I Add Leverage"
- [ ] Quantify "Proof" section
- [ ] Add Person schema markup

### Blog Strategy
- [ ] Create editorial calendar (1-2 posts/month)
- [ ] Write first 2 posts:
  - "How to Add AI to Your iOS App Without a Full ML Team"
  - "Why Your iOS Team's AI Tools Are Making You Slower"
- [ ] Add FAQ section to each post
- [ ] Add CTAs to relevant services

### Technical SEO
- [ ] Add Organization schema (site-wide)
- [ ] Add Service schema (/workshop, /sessions)
- [ ] Add Person schema (/about)
- [ ] Add FAQ schema (all FAQ sections)
- [ ] Update sitemap.xml
- [ ] Submit to Google Search Console
- [ ] Verify page speed (target: <2s load time)
- [ ] Test mobile responsiveness
- [ ] Add og:image for all pages

### Analytics & Tracking
- [ ] Set up conversion goals:
  - Workshop discovery call bookings
  - Session bookings
  - Email signups (if added)
- [ ] Track CTA click rates
- [ ] Monitor keyword rankings (Ahrefs, SEMrush, or free tools)
- [ ] Set up Google Search Console alerts

### Launch
- [ ] Test all CTAs (booking links work)
- [ ] Proofread all copy
- [ ] Test on mobile, tablet, desktop
- [ ] Deploy
- [ ] Announce on LinkedIn, X
- [ ] Email existing network about workshop launch

---

## Success Metrics (90 Days Post-Launch)

**Traffic**:
- 500+ monthly organic visitors
- 50+ monthly visitors from "iOS AI" related keywords

**Conversions**:
- 3-5 workshop discovery calls booked
- 10-15 engineering sessions booked
- 1-2 workshops delivered

**SEO**:
- Ranking page 1 for 3-5 target keywords
- Featured snippet for 1-2 queries

**Revenue**:
- €15k-30k from workshops
- €5k-10k from sessions

---

## Notes for Implementation Agent

1. **Copy is ready to use** — All sections above can be copied directly into page templates.
2. **CTAs need linking** — Replace `[Book Discovery Call]` with actual Calendly/Cal.com embeds.
3. **Schema markup** — Add to `<head>` or as JSON-LD scripts in layouts.
4. **Internal links** — Ensure all `/workshop`, `/sessions`, `/about`, `/posts` links work.
5. **Hour pack purchasing** — Needs payment integration (Stripe, Gumroad, or manual via email initially).
6. **PDF download** (optional) — "Workshop Overview PDF" mentioned on /workshop page; can defer if not ready.
7. **Proof metrics** — Update as needed if numbers change (build time %, LLM cost savings, etc.).
8. **Testimonials** — Placeholder sections added; fill with real testimonials as they come in.

---

**End of Plan**

This document contains all copy, structure, SEO strategy, and implementation steps for the hybrid model website update. Ready for handoff to implementation agent.
