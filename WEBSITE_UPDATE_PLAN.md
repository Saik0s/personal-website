# Website Update Plan: Capacity-Aware Productized Services (10hr/week)
## Igor Tarasenko - iOS Architecture & AI Consulting

**Model**: Architecture Audit (primary) → 4-Week Agentic Program (secondary) → Mentorship + Sessions (ongoing)
**Constraint**: 10 hours/week maximum availability
**Goal**: Lead with time-boxed Architecture Audit, convert to 4-week AI adoption program, sustain with mentorship
**SEO/GSO**: Optimize for both traditional search and AI-powered generative search

---

## Table of Contents

1. [Strategy Overview](#strategy-overview)
2. [Site Structure & Navigation](#site-structure--navigation)
3. [SEO & Generative Search Strategy](#seo--generative-search-strategy)
4. [Page-by-Page Implementation](#page-by-page-implementation)
5. [Schema Markup & Structured Data](#schema-markup--structured-data)
6. [Content Strategy & Publishing](#content-strategy--publishing)
7. [Implementation Checklist](#implementation-checklist)

---

## Strategy Overview

### The 10hr/Week Constraint

All offers redesigned to fit **10 hours/week** while maintaining high-value outcomes:

1. **Architecture Audit & Roadmap (slim)** - 3 weeks, 10hr/week → **PRIMARY WEDGE**
2. **4-Week Agentic iOS Team Program** - 4 weeks, 10hr/week → **SECONDARY CONVERSION**
3. **TCA & Modularization Mentorship** - Rolling retainer, 5-10hr/week → **BASE LOAD**
4. **Engineering Sessions** - Ad-hoc, 2-10hr/week → **IMMEDIATE NEEDS**

### Market Opportunity Navigator Scores (with 10hr/week cap)

| Offer | Score | Position |
|-------|-------|----------|
| Architecture Audit & Roadmap (slim) | 17/18 | **Primary wedge** |
| 4-Week Agentic iOS Team Program | 16/18 | Secondary conversion |
| Refactor Design Authority (oversight) | 15/18 | Follow-on |
| TCA & Modularization Mentorship | 14/18 | Base load |

**Decision**: Lead with Architecture Audit (most time-boxable, async-heavy, executive-facing). Convert to 4-Week Agentic Program. Sustain with Mentorship.

### Weekly Allocation Rule

**One primary lane (6-8h) + one secondary lane (2-4h) = 10h/week max. No overtime.**

---

## Site Structure & Navigation

### Updated Structure (Capacity-Aware Model)

```
/                  → Homepage (Audit-first, then Program, then Sessions)
/audit             → NEW: Architecture Audit & Roadmap (PRIMARY OFFER)
/program           → NEW: 4-Week Agentic iOS Team Program (SECONDARY OFFER)
/mentorship        → NEW: TCA & Modularization Mentorship (ONGOING)
/sessions          → Engineering Sessions (AD-HOC, immediate needs)
/about             → Enhanced with proof metrics
/posts             → Blog (content marketing)
/posts/[slug]      → Individual posts
/projects          → Projects showcase
/archives          → Blog archives
/tags              → Tag index
```

### Navigation Updates

**Primary Navigation** (Option 1 - Simpler):
```
Logo | Projects | Blog | About
```

**Primary Navigation** (Option 2 - With Work):
```
Logo | Work | Projects | Blog | About
```
*Where "Work" dropdown or page lists: Architecture Audits, AI Adoption Program, Mentorship, Sessions*

**CTAs**: Keep existing "Book Session" button in nav if you want, but make it subtle (not primary colored)

---

## SEO & Generative Search Strategy

### Target Keywords (Updated)

**Architecture Audit (High-Value, Executive)**:
- "iOS architecture audit"
- "iOS technical debt assessment"
- "SwiftUI architecture consultant"
- "iOS modernization roadmap"
- "iOS build time optimization"
- "TCA architecture consultant"

**Agentic Program (Team-Level, Mid-Value)**:
- "iOS AI adoption training"
- "agentic coding for iOS teams"
- "AI coding governance framework"
- "iOS team AI productivity"
- "Cursor training for iOS developers"

**Mentorship (Ongoing, Specialist)**:
- "TCA mentorship"
- "Composable Architecture consultant"
- "SwiftUI architecture mentor"
- "iOS modularization expert"

**Sessions (Immediate, Tactical)**:
- "iOS performance consultant"
- "SwiftUI consultant"
- "iOS AI integration consultant"
- "on-device AI iOS expert"

### Generative Search Optimization (GSO)

**Conversational Queries to Target**:
1. "Who can audit our iOS architecture and give us a modernization plan?"
2. "How much does an iOS architecture audit cost?"
3. "How to help our iOS team adopt AI coding tools safely?"
4. "Best consultant for The Composable Architecture adoption?"
5. "iOS consultant specializing in build time optimization"
6. "How long does an iOS architecture audit take?"
7. "Agentic coding training for mobile developers"

**GSO Content Strategy**:
- Natural language, conversational tone
- Answer "who, what, why, how, when, how much" directly
- Transparent pricing (AI models prefer concrete info)
- FAQ sections addressing common queries
- Structured headings mirroring questions
- Cited research and proof metrics

### Meta Strategy

**Homepage**:
- Title: `Igor Tarasenko - iOS Engineer & Agentic Engineer`
- Description: `16 years building iOS apps. Helping individuals and teams find AI advantages, tackle complex architectures, and improve developer experience. WhisperBoard creator. Ex-Uber.`

**/audit**:
- Title: `iOS Architecture Audit & Modernization Roadmap - 3 Week Assessment`
- Description: `Independent iOS architecture audit. Diagnose technical debt, build times, coupling. Receive phased modernization plan. €12-18k fixed fee, 3 weeks.`

**/program**:
- Title: `4-Week Agentic iOS Team Program - AI Coding Adoption Training`
- Description: `4-week program teaching iOS teams to use AI coding tools effectively. Governance, prompt patterns, measurable ROI. €8-12k, 2 live sessions/week.`

**/mentorship**:
- Title: `TCA & Modularization Mentorship - iOS Architecture Coaching`
- Description: `Rolling mentorship for iOS teams adopting TCA or modularization. Weekly office hours, async PR reviews. €2-4k/month retainer.`

**/sessions**:
- Title: `iOS Engineering Sessions - Architecture, Performance, AI Integration`
- Description: `Ad-hoc iOS consulting sessions. €200/hr, 1-10hr blocks. SwiftUI performance, TCA, LLM integration, build optimization. Remote.`

---

## Page-by-Page Implementation

### 1. Homepage (/) - Expertise-First, Subtle Services

**Approach**: Homepage is NOT a sales funnel. It's a personal site showcasing work and expertise. Services are mentioned subtly at the bottom, not pushed aggressively.

**Hero Section**:
```markdown
# Hey, I'm Igor
## iOS Engineer & Agentic Engineer

16 years building iOS apps. I help individuals and teams ship faster by finding AI advantages, tackling complex architectures, and improving developer experience.

Currently: WhisperBoard (50k+ downloads, 4.8★). Previously: Uber.

[View Recent Work](/projects) [Read Latest Posts](/posts)
```

**SEO/GSO Notes**:
- Emphasizes experience (16 years)
- Broader scope (individuals + teams)
- Natural keyword inclusion (iOS, AI, architectures, developer experience)
- Credentials upfront (WhisperBoard, Uber)

---

**What I Work On Section**:
```markdown
## What I Work On

**Building & Shipping** — Currently shipping WhisperBoard (on-device transcription, 50k+ downloads, 4.8★ App Store). I help teams navigate the full App Store release process, from architecture decisions to submission and iteration.

**Finding AI Advantages** — I work with individuals and teams to identify where AI actually helps vs where it's hype. Recent work: helped a team reduce LLM costs from €2k/month to €40/month while improving quality.

**Complex Architectures** — 16 years dealing with messy codebases. I specialize in TCA (The Composable Architecture), modularization, and making large iOS apps maintainable. Recently cut a client's build times by 35%.

**Refactoring & Modernization** — Helping teams migrate UIKit → SwiftUI, MVVM → TCA, or monoliths → modular architectures without breaking production. Strangler-fig patterns, dependency injection, incremental adoption.

**Developer Experience** — Build tooling (Tuist, SPM), CI/CD pipelines, local development speed, onboarding documentation. The stuff that makes teams productive or miserable.

[See all projects →](/projects)
```

**SEO/GSO Notes**:
- Comprehensive expertise showcase
- Specific technologies (TCA, SwiftUI, Tuist)
- Real outcomes (35% build time, 95% cost reduction)
- Covers full scope: shipping, AI, architecture, refactoring, DevXP

---

**Availability Section** (subtle services mention):
```markdown
## Available for Work (10hr/week)

I work with individuals and teams on iOS apps, AI integration, complex architectures, refactoring, and developer experience. Current availability: 10 hours/week.

**Ways to work together**:

**Architecture Audits** — 3-week deep-dive into your iOS codebase. Diagnose tech debt, build bottlenecks, coupling issues. Deliver a phased modernization roadmap with clear priorities. [Details →](/audit)

**AI Adoption Program** — 4-week program helping teams find real AI advantages and integrate tools (Cursor, Claude Code) effectively. Governance, metrics, measurable ROI. [Details →](/program)

**TCA & Modularization Mentorship** — Ongoing guidance for teams adopting The Composable Architecture or modularizing complex apps. Monthly retainer, PR reviews, office hours. [Details →](/mentorship)

**Engineering Sessions** — Ad-hoc help at €200/hr. Good for: performance triage, architecture questions, refactoring strategy, DevXP improvements, rapid prototyping. [Book →](/sessions)

*I typically work with 1-2 clients at a time. If interested, [reach out early](mailto:igor@tarasenko.dev).*
```

**SEO/GSO Notes**:
- Broader framing (individuals + teams, full scope)
- Emphasizes experience and comprehensive expertise
- Specific use cases for each offering
- Links for those interested, not hard CTAs

---

**Recent Posts Teaser**:
```markdown
## Recent Posts

[Display 3-5 most recent blog posts as cards]

Writing about iOS architecture, AI coding workflows, and on-device ML. [View all →](/posts)
```

**SEO/GSO Notes**:
- Keeps homepage fresh
- Demonstrates thought leadership
- Natural keyword signals

---

### 2. /audit (NEW PAGE) - Architecture Audit & Roadmap

**Hero**:
```markdown
# Architecture Audit & Modernization Roadmap
## Independent 3-Week Assessment for iOS Codebases

Diagnose technical debt, build bottlenecks, and coupling—then get a phased modernization plan your team can execute with confidence.

**For**: CTOs, VP Engineering, Tech Leads at product companies with 3+ year iOS apps
**Investment**: €12,000 - €18,000 fixed fee
**Timeline**: 3 weeks
**Format**: Remote, async-heavy with weekly touchpoints

[Book Discovery Call] [Download Audit Overview PDF]
```

**Meta**:
- Title: `iOS Architecture Audit & Modernization Roadmap - 3 Week Assessment`
- Description: `Independent iOS architecture audit. Diagnose technical debt, build times, coupling. Phased modernization plan. €12-18k, 3 weeks. Remote.`

---

**The Problem This Solves**:
```markdown
## Why Teams Need Architecture Audits

**You're experiencing**:
- **Build times 20+ minutes** — CI bottlenecks blocking team velocity
- **Massive view controllers** — 2000+ line files, impossible to test or refactor
- **Onboarding takes 3-6 months** — New hires struggle to understand codebase structure
- **Unclear migration path** — Team debates UIKit vs SwiftUI, MVVM vs TCA, but no clear plan
- **Hidden coupling** — Changing one module breaks three others

**The cost**:
- **Technical debt tax**: McKinsey reports 10-20% of technology budgets consumed by tech debt
- **Onboarding cost**: $15k-$28k per iOS developer in hard costs, plus 3-6 months to productivity
- **Legacy code cost**: $3.60 per line to refactor without a clear plan
- **Velocity loss**: Teams report 30-50% slower feature delivery on poorly architected codebases

**The risk**:
Without an independent assessment, teams waste months on dead-end migrations, architectural rewrites that stall halfway, or "big bang" refactors that break production.

You need a pragmatic roadmap anchored in your actual constraints.
```

**SEO/GSO**:
- Addresses "iOS architecture problems" (pain point search)
- Cites research (authority)
- Quantified costs (AI models prefer numbers)

---

**What You'll Receive (3-Week Deliverables)**:
```markdown
## Audit Deliverables

### Week 1: Discovery & Data Collection
**Your team runs the data collection kit; I analyze asynchronously**

- Codebase structure analysis (module graph, dependency visualization)
- Build time profiling (bottleneck identification, incremental build analysis)
- Coupling analysis (identify high-coupling zones, architectural hot-spots)
- Test coverage assessment (gaps, flaky tests, architecture testability)
- 60-minute kickoff call (scope, access, priorities)

**Weekly budget**: 10 hours (6h analysis, 2h interviews, 2h brief updates)

---

### Week 2: Architecture Assessment & Options
**I draft modernization options and tradeoffs**

- 2-3 architecture options (e.g., incremental modularization vs full TCA migration vs hybrid)
- Tradeoff analysis (effort, risk, ROI for each option)
- Phased roadmap draft (6-12 month timeline with milestones)
- Risk ledger (migration blockers, hidden coupling, team capacity constraints)
- 60-minute mid-audit sync (review findings, validate priorities)

**Weekly budget**: 10 hours (6h analysis, 2h interviews, 2h updates)

---

### Week 3: Final Roadmap & Executive Briefing
**Deliver actionable plan and exec presentation**

- **Final deliverables**:
  - Boundary map (recommended module structure, dependency graph)
  - Phased modernization roadmap (specific milestones, effort estimates, sequencing)
  - ROI proxy (projected build time savings, team velocity gains, onboarding improvements)
  - Risk mitigation strategies (for each phase)
  - Adoption metrics framework (how to measure success)

- **90-minute executive briefing** (stakeholder presentation, Q&A, next steps)

**Weekly budget**: 10 hours (6h final synthesis, 2h exec brief prep, 2h meeting)

---

### Post-Audit
**Optional follow-on engagements**:
- 4-Week Agentic iOS Team Program (if AI adoption is a priority)
- Refactor Design Authority (6-8 week oversight of implementation)
- TCA & Modularization Mentorship (ongoing retainer)
```

**SEO/GSO**:
- Answers "what's included in an iOS architecture audit?" (common query)
- Clear timeline and phases
- Structured format (AI models extract lists)

---

**How It Works (Process)**:
```markdown
## Audit Process

### 1. Discovery Call (30 minutes, free)
- Understand your goals (modernization, team scaling, build time optimization)
- Review codebase context (size, stack, team size, constraints)
- Confirm scope and pricing

### 2. Data Collection Kit Setup (Week 0)
- Provide automated scripts to capture:
  - Module dependency graph
  - Build time breakdown (compile times per module)
  - Test coverage and flaky test reports
  - Coupling metrics (class/module dependencies)
- Your team runs scripts, I receive anonymized data

### 3. Async Analysis (Weeks 1-2)
- I analyze codebase structure, build metrics, architectural patterns
- Weekly 60-minute sync calls to validate findings and adjust focus
- Draft options and tradeoff analysis

### 4. Final Briefing (Week 3)
- 90-minute executive presentation
- Deliver final roadmap, boundary map, ROI proxy
- Answer questions, discuss implementation approach

### 5. Handoff
- All deliverables provided in editable format (Markdown, diagrams, spreadsheets)
- Optional: schedule follow-on engagements (program, mentorship, refactor oversight)
```

**SEO/GSO**:
- Answers "how does an iOS architecture audit work?" (process query)
- Transparent methodology

---

**Pricing & Investment**:
```markdown
## Investment

**Base audit**: €12,000 - €18,000 fixed fee

**Pricing factors**:
- **Codebase size**: <100k LOC (€12k), 100k-300k LOC (€15k), >300k LOC (€18k)
- **Complexity**: Number of modules, frameworks, architectural patterns
- **Urgency**: Standard 3-week timeline vs expedited 2-week

**What's included**:
- 30 hours of expert analysis over 3 weeks (10hr/week)
- All deliverables (boundary map, roadmap, ROI proxy, risk ledger)
- 90-minute executive briefing
- Data collection kit and scripts

**Not included** (available as follow-ons):
- Implementation support (see Refactor Design Authority)
- Team training (see 4-Week Agentic Program)
- Ongoing mentorship (see TCA & Modularization Mentorship)

**Money-back guarantee**: If the plan isn't actionable or doesn't provide clear ROI justification, full refund.

[Book Discovery Call to Get Custom Quote]
```

**SEO/GSO**:
- Answers "how much does an iOS architecture audit cost?" (direct pricing query)
- Transparent pricing factors
- Clear inclusions/exclusions

---

**Who This Is For**:
```markdown
## Ideal Audit Clients

This audit is designed for:

✅ **CTOs/VP Engineering** at product companies with iOS as core product
✅ **Tech Leads** planning a major migration (UIKit → SwiftUI, monolith → modular, MVVM → TCA)
✅ **Teams with 5-15 iOS developers** experiencing build time or onboarding pain
✅ **Codebases 3+ years old** with visible technical debt and architectural drift
✅ **Leadership seeking independent validation** before committing to large refactor

❌ **Not ideal for**:
- Early-stage startups with <1 year old codebases (architecture likely fine)
- Teams with <3 iOS developers (lighter-weight session engagement may suffice)
- Teams needing immediate hands-on implementation (consider Refactor Design Authority)
```

**SEO/GSO**:
- Qualification criteria (helps AI models match intent)

---

**FAQ**:
```markdown
## Frequently Asked Questions

### How long does the audit take?
3 weeks from kickoff to final briefing. Timeline is fixed to fit 10hr/week availability.

### Do you need access to our codebase?
Read-only access preferred but not required. Teams can run data collection scripts and share anonymized metrics if repo access isn't possible.

### What if our codebase is UIKit, not SwiftUI?
No problem. Audit covers UIKit, SwiftUI, TCA, VIPER, MVVM, or hybrid architectures.

### Can you implement the roadmap for us?
The audit deliverable is the plan. If you want implementation oversight, consider the Refactor Design Authority engagement (6-8 weeks, 10hr/week). If you want hands-on pairing, book Engineering Sessions.

### What happens after the audit?
You own all deliverables and can execute the roadmap internally. Many teams choose follow-on engagements (4-Week Agentic Program, Mentorship, or Refactor oversight).

### How do you measure ROI?
The audit includes an ROI proxy: projected build time savings (minutes saved per build × builds per day × team size), velocity gains (estimated story point throughput increase), and onboarding improvements (weeks saved per new hire).

### What if we're not happy with the plan?
Money-back guarantee. If the plan isn't actionable or doesn't justify the investment, full refund.

### Can this be done on-site?
Remote is standard. On-site available for EU-based teams (travel costs additional).
```

**SEO/GSO**:
- FAQ format (AI models extract for featured snippets)
- Answers common objections

---

**CTA Section**:
```markdown
## Ready to Get a Clear Modernization Roadmap?

Book a 30-minute discovery call to discuss your codebase, goals, and constraints. Get a custom quote within 24 hours.

[Book Discovery Call] [Email igor@tarasenko.dev]

**Next steps**:
1. 30-min discovery call (free)
2. Custom proposal with pricing
3. Data collection kit setup
4. 3-week audit execution
5. Final briefing & roadmap delivery
```

---

### 3. /program (NEW PAGE) - 4-Week Agentic iOS Team Program

**Hero**:
```markdown
# 4-Week Agentic iOS Team Program
## Standardize AI Coding Adoption Across Your iOS Team

4-week program teaching your iOS team to use AI coding tools (Cursor, Claude Code, GitHub Copilot) safely and effectively on your actual codebase.

**For**: Engineering managers with 5-25 iOS developers adopting AI tools
**Investment**: €8,000 - €12,000 fixed fee
**Timeline**: 4 weeks (2 live sessions/week + async support)
**Format**: Remote, live sessions + async PR reviews

[Book Discovery Call] [Download Program Syllabus PDF]
```

**Meta**:
- Title: `4-Week Agentic iOS Team Program - AI Coding Adoption Training`
- Description: `4-week program for iOS teams adopting AI coding tools. Governance, prompt patterns, measurable ROI. €8-12k, 2 live sessions/week. Remote.`

---

**The Problem This Solves**:
```markdown
## Why AI Coding Tools Aren't Making Your Team Faster

**You've bought the licenses. Why aren't you faster?**

Research shows **90% of engineering leaders view AI as mission-critical**, yet:

- **19% slower performance**: Stanford study found AI tools make experienced developers slower without structured workflows
- **4x defect increase**: Analysis of 211M changed lines showed quality degradation with unstructured AI usage
- **Fragmented adoption**: 49% of orgs use multiple AI tools simultaneously, doubling costs and fragmenting practices
- **No training strategy**: Dominant approach is "none"—tools deployed without enablement

**The symptoms in your team**:
- Some devs use AI heavily, others ignore it — code review becomes inconsistent
- AI-generated code introduces subtle bugs or architectural drift
- No governance framework (prompts, security, review standards)
- Leadership asks "Is this worth it?" but you can't measure ROI

**The gap**: Your team has licenses. They lack a system.

This program installs the system.
```

**SEO/GSO**:
- Cites research (authority for AI search)
- Addresses "iOS AI adoption problems" (pain point)
- Quantified problems

---

**What You'll Achieve (4-Week Outcomes)**:
```markdown
## Program Outcomes

By the end of 4 weeks, your team will have:

### 1. Governance Framework
- **AI coding policy**: When to use AI, when not to, escalation procedures
- **Prompt library**: Curated prompts for common iOS tasks (SwiftUI views, TCA reducers, test generation)
- **Review checklist**: What to look for when reviewing AI-generated code
- **Security framework**: Data access policies, API key management, compliance checks

### 2. Measurable Productivity Gains
- **Baseline metrics captured**: PR cycle time, rework/rollback rates, defect counts (Week 1)
- **30-day targets**: 20-30% reduction in PR rework, 80%+ standardized adoption
- **Instrumentation dashboard**: Track AI usage impact, quality metrics, team velocity

### 3. Team-Wide Adoption
- **8 live training sessions** (2×90min/week): Prompt engineering, governance, quality gates, advanced patterns
- **Real codebase exercises**: No toy examples—practice on your actual SwiftUI/TCA/modular codebase
- **Async PR reviews throughout**: I review AI-assisted PRs and provide architectural feedback (4-6 hours/week)

### 4. Quality Gates & Safety
- **Regression test requirements**: Coverage thresholds for AI-assisted changes
- **Performance budgets**: Ensure AI-generated code doesn't degrade app performance
- **Audit trail**: Track which code was AI-assisted for future reviews
- **Rollback criteria**: When to reject AI suggestions

### 5. 30-Day Follow-Up
- **Check-in surveys** (Week 6): Measure adoption rate, satisfaction, blockers
- **Metric review**: Validate productivity targets were hit
- **Office hours** (60min): Address questions as team applies learnings
```

**SEO/GSO**:
- Answers "what's included in AI coding training?" (query)
- Structured outcomes (AI models extract)
- Specific deliverables

---

**4-Week Program Structure**:
```markdown
## How the Program Works

**Weekly commitment**: 10 hours (2×90min live sessions + 4h async PR reviews + 2h prep/support)

---

### Week 1: Foundations & Baseline
**Live sessions**:
- Session 1: Agentic coding principles, prompt engineering basics for iOS
- Session 2: Security and governance (data policies, review frameworks)

**Async work**:
- Capture baseline metrics (PR cycle time, defect rates, current AI usage)
- Team starts using standardized prompt templates
- I review 2-3 PRs with AI-assisted code, provide feedback

**Deliverable**: Baseline metrics report, governance draft

---

### Week 2: Advanced Patterns & Quality Gates
**Live sessions**:
- Session 3: Advanced prompts (TCA reducers, dependency injection, test generation)
- Session 4: Quality gates (regression tests, performance budgets, review checklist)

**Async work**:
- Team applies advanced prompts on real tasks
- I review 3-4 PRs, audit architectural consistency
- Refine governance framework based on real usage

**Deliverable**: Prompt library v1, quality gate checklist

---

### Week 3: Scaling & Team Adoption
**Live sessions**:
- Session 5: Team adoption strategies (champions program, pair programming with AI)
- Session 6: Measurement frameworks (telemetry, adoption metrics, ROI tracking)

**Async work**:
- Team standardizes AI usage across all members
- I review 3-4 PRs, track adoption rate
- Set up instrumentation dashboard

**Deliverable**: Adoption metrics dashboard, instrumentation setup

---

### Week 4: Edge Cases & Handoff
**Live sessions**:
- Session 7: Edge cases (when AI fails, escalation procedures, rollback strategies)
- Session 8: Wrap-up and handoff (Q&A, ongoing improvement process)

**Async work**:
- Final PR reviews
- Synthesize learnings into internal playbook
- 30-day follow-up plan

**Deliverable**: Final governance playbook, 30-day metric targets

---

### Week 6 (Post-Program): Follow-Up Check-In
**60-minute call**:
- Review adoption metrics vs baseline
- Address blockers or questions
- Adjust governance framework if needed
- Discuss optional ongoing mentorship
```

**SEO/GSO**:
- Answers "how does AI coding training work for iOS teams?" (process query)
- Week-by-week breakdown (transparent)

---

**Pricing & Investment**:
```markdown
## Investment

**Base program**: €8,000 - €12,000 fixed fee

**Pricing factors**:
- **Team size**: 5-10 devs (€8k), 10-20 devs (€10k), 20-25 devs (€12k)
- **Codebase complexity**: SwiftUI/TCA (standard), hybrid UIKit/SwiftUI (add €2k), legacy UIKit (add €3k)
- **Follow-up intensity**: Standard 30-day (included), extended 60-day coaching (add €2k)

**What's included**:
- 8 live training sessions (2×90min/week for 4 weeks)
- Async PR reviews throughout (4-6 hours/week)
- Governance framework (prompts, checklists, policies)
- Instrumentation dashboard setup
- 30-day follow-up check-in (Week 6)

**Not included** (available as add-ons):
- Architecture audit (see Architecture Audit page)
- Ongoing mentorship beyond 30 days (see Mentorship page)
- Implementation of governance tooling (can recommend vendors)

[Book Discovery Call to Get Custom Quote]
```

**SEO/GSO**:
- Answers "how much does AI coding training cost?" (pricing query)
- Transparent pricing factors

---

**Who This Is For**:
```markdown
## Ideal Program Participants

This program is designed for:

✅ **Engineering managers** with 5-25 iOS developers
✅ **Teams with existing AI licenses** (Cursor, GitHub Copilot, Claude Code) but unclear ROI
✅ **Brownfield codebases** (2-5 years old) with SwiftUI, UIKit, or TCA
✅ **Organizations concerned about** security, quality, or governance with AI tools
✅ **Teams where AI adoption is fragmented** (some use it, others don't)

❌ **Not ideal for**:
- Individual developers (consider Engineering Sessions instead)
- Teams with <5 iOS developers (ROI may not justify program format)
- Greenfield projects without legacy constraints (lighter approach may suffice)
- Teams without existing AI tool licenses (get licenses first, then run program)
```

**SEO/GSO**:
- Qualification criteria

---

**FAQ**:
```markdown
## Frequently Asked Questions

### Can the program be done remotely?
Yes. All sessions via Zoom/Meet with screen sharing. Async PR reviews via GitHub/GitLab.

### What if our codebase uses UIKit, not SwiftUI?
No problem. Program adapts to your stack—UIKit, SwiftUI, TCA, VIPER, MVVM, or hybrid.

### Do we need AI tools already?
Yes. Team should have active licenses for Cursor, GitHub Copilot, or Claude Code. If not, we'll help you evaluate and choose during discovery.

### What's the team size limit?
Optimal: 5-15 developers. Can accommodate up to 25 with breakout facilitators (pricing adjusts).

### How do you measure success?
Baseline metrics captured Week 1 (PR cycle time, defect rates, rework %). Week 6 follow-up compares to post-adoption numbers. Target: 20-30% improvement.

### What if we don't see results?
If adoption doesn't reach 80% of team or metrics don't improve within 30 days, I'll schedule additional coaching at no extra cost until targets are met.

### Can we get an audit first?
Yes. Many teams run Architecture Audit first to understand technical debt, then run this program to standardize AI adoption during modernization.

### What's the weekly time commitment for the team?
2×90min live sessions/week (3 hours) + applying learnings to daily work. No additional homework.
```

**SEO/GSO**:
- FAQ format (featured snippet optimization)

---

**CTA Section**:
```markdown
## Ready to Standardize Your Team's AI Workflow?

Book a 30-minute discovery call to discuss your team's needs, current AI tool usage, and goals. Get a custom quote within 24 hours.

[Book Discovery Call] [Email igor@tarasenko.dev]

**Next steps**:
1. 30-min discovery call (free)
2. Custom proposal with pricing
3. Baseline metric capture (Week 0)
4. 4-week program execution
5. 30-day follow-up check-in
```

---

### 4. /mentorship (NEW PAGE) - TCA & Modularization Mentorship

**Hero**:
```markdown
# TCA & Modularization Mentorship
## Rolling Retainer for iOS Architecture Coaching

Expert-in-your-corner for teams adopting The Composable Architecture, modularizing an existing app, or scaling SwiftUI codebases.

**For**: Senior iOS developers, tech leads, small teams (3-10 devs)
**Investment**: €2,000 - €4,000/month retainer
**Format**: Weekly office hours + async PR reviews
**Availability**: 5-10 hours/week

[Book Discovery Call] [Download Mentorship Overview PDF]
```

**Meta**:
- Title: `TCA & Modularization Mentorship - iOS Architecture Coaching`
- Description: `Rolling iOS mentorship. TCA adoption, modularization, SwiftUI architecture. €2-4k/month. Weekly office hours, async PR reviews.`

---

**The Problem This Solves**:
```markdown
## Why TCA & Modularization Are Hard to Adopt

**The Composable Architecture** has a steep learning curve:
- 100+ hours of video content (Point-Free)
- Boilerplate confusion (reducers, actions, stores, environments)
- Enum explosion (every user action is a case)
- Performance pitfalls (over-observation, excessive view updates)

**Modularization** requires careful planning:
- High abstraction and planning capabilities
- Strangler-fig pattern execution (can't "big bang" it)
- Dependency injection refactors
- Build tooling setup (SPM, Tuist, Bazel)

**Common mistakes without mentorship**:
- Massive reducers (2000+ line switch statements, Xcode can't scroll)
- Incorrect module boundaries (tight coupling across modules)
- Slow builds (didn't set up incremental compilation correctly)
- Test brittleness (mocking issues, environment setup complexity)

**The gap**: You can watch videos, but applying patterns to your real codebase requires feedback loops and expert guidance.
```

**SEO/GSO**:
- Addresses "TCA learning curve" (pain point)
- Specific problems (massive reducers, module boundaries)

---

**What You'll Get (Monthly Retainer)**:
```markdown
## Mentorship Deliverables

### Weekly Office Hours (1-2 hours/week)
- Live pairing sessions on Zoom/Meet
- Architecture design reviews (before implementing major features)
- Code review sessions (walk through PRs together)
- Q&A on TCA patterns, dependency injection, testing strategies
- Unblocking sessions (stuck on a problem? Let's fix it together)

**Scheduled flexibly**: Book slots throughout the month as needed

---

### Async PR Reviews (4-6 hours/week)
- I review your team's PRs with architectural feedback
- Focus on:
  - TCA reducer composition and action design
  - Module boundary adherence
  - Dependency injection patterns
  - Test coverage and architecture testability
  - Performance considerations (view updates, observation)

**Turnaround**: 24-48 hours on weekdays

---

### Curriculum & Templates (Ongoing)
- Starter templates for common patterns:
  - TCA feature modules (boilerplate reducers, stores, views)
  - Dependency injection setup (live, preview, test environments)
  - Module structure (SPM packages, Tuist projects)
  - Test utilities (reducer test helpers, mock dependencies)

- Curated curriculum:
  - TCA best practices (derived from Point-Free + real-world experience)
  - Modularization strategies (boundary design, dependency graphs)
  - Performance optimization (lazy observation, equatable conformance)

**Delivered**: Via private Git repo or shared Notion workspace

---

### Exemplar Repos (Optional)
- Reference implementations of your architecture patterns
- Mini-apps demonstrating TCA + modularization at scale
- CI/CD pipeline examples (build caching, test parallelization)

**Delivered**: Public or private GitHub repos
```

**SEO/GSO**:
- Answers "what's included in TCA mentorship?" (query)
- Clear deliverables

---

**How It Works**:
```markdown
## Mentorship Process

### 1. Discovery Call (30 minutes, free)
- Understand your goals (TCA adoption, modularization, both)
- Review current architecture and pain points
- Define success metrics (build time targets, team velocity, PR cycle time)

### 2. Kickoff (Week 1)
- Set up communication channels (Slack, email, or preferred)
- Schedule recurring office hours (e.g., every Tuesday 10am CET)
- Grant repo access for async PR reviews
- Deliver initial starter templates and curriculum

### 3. Ongoing Retainer (Monthly)
- Weekly office hours (scheduled flexibly)
- Async PR reviews as PRs come in
- Curriculum updates and template additions
- Optional: monthly sync to review progress and adjust focus

### 4. Flexible Commitment
- **Month-to-month**: No long-term contract, cancel anytime
- **Pause/Resume**: If team goes on break or needs less support, pause retainer
- **Scale up/down**: Adjust hours based on need (5hr/week vs 10hr/week pricing tiers)
```

**SEO/GSO**:
- Answers "how does iOS mentorship work?" (process query)
- Flexible commitment (reduces friction)

---

**Pricing & Investment**:
```markdown
## Investment

**Base retainer**: €2,000 - €4,000/month

**Pricing tiers**:
- **5hr/week tier** (€2,000/month): 1hr office hours/week + 4hr async PR reviews
- **10hr/week tier** (€4,000/month): 2hr office hours/week + 6hr async PR reviews + curriculum development

**What's included**:
- Weekly office hours (live pairing, design reviews, Q&A)
- Async PR reviews (24-48hr turnaround)
- Starter templates and curriculum
- Private Slack/email access
- Flexible scheduling (no fixed meeting times)

**Not included** (available separately):
- Architecture Audit (see /audit)
- Team-wide training (see /program)
- Hands-on implementation (consider Engineering Sessions)

**Commitment**:
- Month-to-month, cancel anytime
- Pause/resume flexible
- Scale up/down as needed

[Book Discovery Call to Get Started]
```

**SEO/GSO**:
- Answers "how much does TCA mentorship cost?" (pricing query)
- Transparent tiers

---

**Who This Is For**:
```markdown
## Ideal Mentorship Clients

This mentorship is designed for:

✅ **Senior iOS developers** learning TCA or modularization
✅ **Tech leads** guiding team through architecture migration
✅ **Small teams (3-10 devs)** adopting TCA or modularizing brownfield app
✅ **Teams post-Architecture Audit** executing modernization roadmap
✅ **Teams wanting ongoing support** beyond one-off programs

❌ **Not ideal for**:
- Complete beginners (start with Point-Free course first)
- Large teams (>15 devs) needing structured training (see 4-Week Program)
- Teams needing immediate crisis firefighting (see Engineering Sessions)
```

**SEO/GSO**:
- Qualification criteria

---

**FAQ**:
```markdown
## Frequently Asked Questions

### Do I need TCA experience already?
Basic familiarity helps (e.g., completed a few Point-Free episodes). Complete beginners should start with Point-Free's free episodes, then join mentorship.

### Can this be done async-only (no live calls)?
Yes. Some clients prefer async-only (PR reviews + Slack Q&A). Pricing adjusts slightly (more PR review hours, no live office hours).

### What if we're using VIPER or MVVM, not TCA?
Mentorship adapts to your architecture. Can guide VIPER, MVVM, or custom patterns. TCA is my specialty, but other architectures are supported.

### How do I cancel?
Email anytime before the next billing cycle. No penalties, no questions asked.

### Can I pause for a month?
Yes. Notify me before the next billing cycle and we'll pause. Resume whenever ready.

### What's the minimum commitment?
1 month. After that, month-to-month.

### Can you implement features for us?
Mentorship is guidance and code review, not hands-on implementation. For implementation, book Engineering Sessions or consider Refactor Design Authority.
```

**SEO/GSO**:
- FAQ format (featured snippets)

---

**CTA Section**:
```markdown
## Ready to Accelerate Your TCA or Modularization Journey?

Book a 30-minute discovery call to discuss your architecture goals and current challenges. Start mentorship within 1 week.

[Book Discovery Call] [Email igor@tarasenko.dev]

**Next steps**:
1. 30-min discovery call (free)
2. Choose tier (5hr/week or 10hr/week)
3. Kickoff and repo access setup
4. Start weekly office hours and PR reviews
```

---

### 5. /sessions (KEEP EXISTING, MINOR UPDATES)

**Updates to existing /sessions page**:

1. **Add positioning as tertiary option**:

```markdown
# Engineering Sessions
## Ad-Hoc iOS Consulting for Immediate Problems

Book 1-10 hour blocks at €200/hr for hands-on pairing, performance triage, or rapid prototyping.

**Best for**: Immediate, tactical problems that need solving now
**Availability**: 2-10 hours/week (flexible scheduling)

[Book a Session]

**For larger engagements**: [Architecture Audit](/audit) | [4-Week AI Program](/program) | [TCA Mentorship](/mentorship)
```

2. **Update hero to reference productized offers**:

After "Focus Areas" section, add:

```markdown
## When to Choose Sessions vs Productized Offers

**Choose Engineering Sessions when**:
- You need immediate help on a specific problem (performance bug, architecture question)
- You want to validate an idea quickly (prototype AI feature in 2-3 sessions)
- You need a second opinion before committing to larger work
- You prefer flexible, ad-hoc scheduling

**Consider productized offers when**:
- You need a comprehensive assessment → [Architecture Audit](/audit)
- Your team needs AI adoption training → [4-Week Program](/program)
- You want ongoing architectural guidance → [TCA Mentorship](/mentorship)
```

3. **Keep all existing content** (focus areas, hour packs, positioning variants, proof, FAQ)

---

### 6. /about (Enhanced with Capacity Signal)

**Add capacity constraint to existing "How to Work Together" section**:

```markdown
## How to Work Together

I operate at **10 hours/week maximum** to maintain quality while working full-time. This constraint shapes all offerings:

**Productized services** (recommended for teams):
- [Architecture Audit & Roadmap](/audit) - 3 weeks, 10hr/week
- [4-Week Agentic iOS Team Program](/program) - 4 weeks, 10hr/week
- [TCA & Modularization Mentorship](/mentorship) - Rolling retainer, 5-10hr/week

**Ad-hoc sessions** (for immediate problems):
- [Engineering Sessions](/sessions) - 1-10hr blocks at €200/hr

All engagements are remote, scoped in advance, and wrap with documented outcomes.

[Book Discovery Call]
```

---

## Schema Markup & Structured Data

### Organization Schema (Site-wide):
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Igor Tarasenko - iOS & Agentic Engineering",
  "description": "16 years iOS experience. Architecture audits, AI integration, complex refactoring, TCA mentorship, developer experience. 10hr/week availability.",
  "url": "https://www.tarasenko.dev",
  "logo": "https://www.tarasenko.dev/og-image.jpg",
  "founder": {
    "@type": "Person",
    "name": "Igor Tarasenko",
    "jobTitle": "iOS Engineer & Agentic Engineer",
    "url": "https://www.tarasenko.dev/about"
  },
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Amsterdam",
    "addressCountry": "NL"
  },
  "sameAs": [
    "https://github.com/Saik0s",
    "https://x.com/sa1k0s"
  ]
}
```

### Service Schema (/audit):
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "iOS Architecture Audit & Modernization Roadmap",
  "provider": {
    "@type": "Person",
    "name": "Igor Tarasenko"
  },
  "areaServed": "Worldwide",
  "description": "3-week independent iOS architecture audit. Diagnose technical debt, build times, coupling. Receive phased modernization plan.",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "12000-18000",
    "priceSpecification": {
      "@type": "PriceSpecification",
      "minPrice": "12000",
      "maxPrice": "18000",
      "priceCurrency": "EUR"
    }
  }
}
```

### Service Schema (/program):
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "4-Week Agentic iOS Team Program",
  "provider": {
    "@type": "Person",
    "name": "Igor Tarasenko"
  },
  "areaServed": "Worldwide",
  "description": "4-week program for iOS teams adopting AI coding tools. Governance, prompt patterns, measurable ROI.",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "8000-12000",
    "priceSpecification": {
      "@type": "PriceSpecification",
      "minPrice": "8000",
      "maxPrice": "12000",
      "priceCurrency": "EUR"
    }
  }
}
```

### Service Schema (/mentorship):
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "TCA & Modularization Mentorship",
  "provider": {
    "@type": "Person",
    "name": "Igor Tarasenko"
  },
  "areaServed": "Worldwide",
  "description": "Rolling monthly retainer for iOS architecture coaching. TCA adoption, modularization guidance, async PR reviews.",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "2000-4000",
    "priceSpecification": {
      "@type": "PriceSpecification",
      "minPrice": "2000",
      "maxPrice": "4000",
      "priceCurrency": "EUR",
      "unitText": "month"
    }
  }
}
```

### FAQ Schema (All pages with FAQs):
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How much does an iOS architecture audit cost?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "€12,000-€18,000 fixed fee for a 3-week audit. Pricing depends on codebase size and complexity."
    }
  }, {
    "@type": "Question",
    "name": "How long does an iOS architecture audit take?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "3 weeks from kickoff to final briefing. Timeline is fixed to fit 10hr/week availability."
    }
  }]
}
```

---

## Content Strategy & Publishing

### Phase 1: Core Pages (Week 1-2)
1. Update homepage (/) - Audit-first hierarchy
2. Create /audit page (Architecture Audit primary wedge)
3. Create /program page (4-Week Agentic iOS Team Program)
4. Create /mentorship page (TCA & Modularization)
5. Update /sessions page (minor positioning updates)
6. Enhance /about with capacity signal

### Phase 2: SEO Content (Weeks 3-6)
1. Publish 3 high-value blog posts:
   - "The Hidden Cost of iOS Technical Debt: A €50k/Year Tax"
   - "How to Know If Your iOS Team Needs an Architecture Audit"
   - "Why Your iOS Team's AI Tools Are Making You Slower (Stanford Research)"
2. Add FAQ sections to all service pages

### Phase 3: Ongoing (Monthly)
1. Publish 1-2 blog posts/month targeting long-tail keywords
2. Update proof metrics as projects complete
3. Collect case studies from audit/program clients
4. Refine copy based on analytics

### Blog Post Ideas (SEO-Driven, Updated for Capacity-Aware Strategy)

1. **"The Hidden Cost of iOS Technical Debt: A €50k/Year Tax"**
   - Keywords: `iOS technical debt cost`, `iOS architecture problems`, `iOS build time optimization`
   - CTA: Architecture Audit

2. **"How to Know If Your iOS Team Needs an Architecture Audit"**
   - Keywords: `iOS architecture audit`, `when to refactor iOS app`, `iOS modernization`
   - CTA: Architecture Audit discovery call

3. **"Why Your iOS Team's AI Tools Are Making You Slower (Stanford Research)"**
   - Keywords: `AI tools slow developers`, `iOS team AI adoption`, `AI coding productivity`
   - CTA: 4-Week Agentic Program

4. **"The Composable Architecture: When to Use It, When to Avoid It"**
   - Keywords: `TCA iOS`, `Composable Architecture guide`, `TCA vs MVVM`
   - CTA: TCA Mentorship

5. **"Cutting iOS Build Times by 35%: Modularization Case Study"**
   - Keywords: `reduce iOS build time`, `iOS modularization`, `Tuist tutorial`
   - CTA: Architecture Audit or Mentorship

6. **"How to Adopt AI Coding Tools Without Breaking Your iOS App"**
   - Keywords: `AI coding tools iOS`, `Cursor iOS development`, `GitHub Copilot SwiftUI`
   - CTA: 4-Week Agentic Program

---

## Implementation Checklist

### Navigation & Structure
- [ ] Update primary nav: `Audit | Program | Mentorship | Sessions | Blog | About`
- [ ] Add /audit route
- [ ] Add /program route
- [ ] Add /mentorship route
- [ ] Update /sessions (minor positioning changes)
- [ ] Update all internal links
- [ ] Add tiered CTAs throughout (Audit primary, Program secondary, Mentorship/Sessions tertiary)

### Homepage (/)
- [ ] Rewrite hero: "Ship Faster with a Clear iOS Architecture Roadmap"
- [ ] Add problem agitation (technical debt costs)
- [ ] Add four-offer preview (Audit, Program, Mentorship, Sessions hierarchy)
- [ ] Add proof metrics section (35% build time, 95% LLM cost savings)
- [ ] Update meta title/description

### Architecture Audit Page (/audit)
- [ ] Create new page with full copy from this doc
- [ ] Add discovery call CTA (Calendly/Cal.com embed)
- [ ] Add FAQ section (minimum 6 questions)
- [ ] Add Service schema markup
- [ ] Add FAQ schema markup
- [ ] Add downloadable "Audit Overview PDF" (optional)

### 4-Week Program Page (/program)
- [ ] Create new page with full copy from this doc
- [ ] Add discovery call CTA
- [ ] Add FAQ section (minimum 6 questions)
- [ ] Add week-by-week breakdown table/accordion
- [ ] Add Service schema markup
- [ ] Add FAQ schema markup
- [ ] Add downloadable "Program Syllabus PDF" (optional)

### Mentorship Page (/mentorship)
- [ ] Create new page with full copy from this doc
- [ ] Add discovery call CTA
- [ ] Add FAQ section (minimum 6 questions)
- [ ] Add pricing tier comparison table
- [ ] Add Service schema markup
- [ ] Add FAQ schema markup

### Sessions Page (/sessions)
- [ ] Update hero with positioning as tertiary option
- [ ] Add "When to Choose Sessions vs Productized Offers" section
- [ ] Keep all existing content (focus areas, hour packs, proof, FAQ)
- [ ] Update meta title/description

### About Page (/about)
- [ ] Add capacity constraint explanation (10hr/week)
- [ ] Add service hierarchy (Audit → Program → Mentorship → Sessions)
- [ ] Keep existing proof metrics
- [ ] Add Person schema markup

### Blog Strategy
- [ ] Create editorial calendar (1-2 posts/month)
- [ ] Write first 3 posts:
  - "The Hidden Cost of iOS Technical Debt: A €50k/Year Tax"
  - "How to Know If Your iOS Team Needs an Architecture Audit"
  - "Why Your iOS Team's AI Tools Are Making You Slower"
- [ ] Add FAQ section to each post
- [ ] Add CTAs to relevant services (Audit, Program, Mentorship)

### Technical SEO
- [ ] Add Organization schema (site-wide)
- [ ] Add Service schema (/audit, /program, /mentorship, /sessions)
- [ ] Add Person schema (/about)
- [ ] Add FAQ schema (all FAQ sections)
- [ ] Update sitemap.xml
- [ ] Submit to Google Search Console
- [ ] Verify page speed (<2s load time)
- [ ] Test mobile responsiveness
- [ ] Add og:image for all pages

### Analytics & Tracking
- [ ] Set up conversion goals:
  - Architecture Audit discovery calls
  - 4-Week Program discovery calls
  - Mentorship discovery calls
  - Session bookings
- [ ] Track CTA click rates
- [ ] Monitor keyword rankings
- [ ] Set up Google Search Console alerts

### Launch
- [ ] Test all CTAs (booking links work)
- [ ] Proofread all copy
- [ ] Test on mobile, tablet, desktop
- [ ] Deploy
- [ ] Announce on LinkedIn, X (focus on Audit as primary offer)
- [ ] Email existing network about Architecture Audit launch

---

## Success Metrics (90 Days Post-Launch)

**Traffic**:
- 500+ monthly organic visitors
- 100+ monthly visitors from "iOS architecture audit" related keywords
- 50+ monthly visitors from "iOS AI adoption" keywords

**Conversions**:
- 2-3 Architecture Audit discovery calls booked
- 1-2 Architecture Audits delivered
- 1-2 4-Week Program discovery calls booked
- 1 4-Week Program delivered
- 5-10 Engineering Sessions booked

**SEO**:
- Ranking page 1 for 5-7 target keywords
- Featured snippet for 2-3 queries (FAQ-based)

**Revenue**:
- €15k-30k from Architecture Audits
- €8k-12k from 4-Week Program
- €2k-8k from Mentorship
- €2k-5k from Sessions

**Total target**: €27k-€55k in 90 days

---

## Notes for Implementation Agent

1. **Copy is ready to use** — All sections above can be copied directly into page templates.
2. **CTAs need linking** — Replace `[Book Discovery Call]` with actual Calendly/Cal.com embeds.
3. **Schema markup** — Add to `<head>` or as JSON-LD scripts in layouts.
4. **Internal links** — Ensure all `/audit`, `/program`, `/mentorship`, `/sessions` links work.
5. **Pricing transparency** — All prices are visible on pages (critical for SEO/GSO).
6. **PDFs (optional)** — "Audit Overview PDF" and "Program Syllabus PDF" mentioned; can defer if not ready.
7. **Proof metrics** — Update as needed (build time %, LLM cost savings, etc.).
8. **Testimonials** — Placeholder sections added; fill with real testimonials as they come in.
9. **10hr/week constraint** — Signal throughout site (homepage, about, service pages).
10. **Service hierarchy** — Audit (primary) → Program (secondary) → Mentorship/Sessions (tertiary).

---

**End of Updated Plan**

This document reflects the **capacity-aware strategy** (10hr/week constraint) with Architecture Audit as the primary wedge, 4-Week Agentic Program as secondary conversion, and Mentorship/Sessions as ongoing/ad-hoc options.

Ready for implementation.
