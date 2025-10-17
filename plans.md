# plans.md

## Objective
- Reposition tarasenko.dev as an iOS engineering and agentic automation specialist funnel with clear service booking flow.

## Big Picture
- Refresh homepage copy, structure, and CTA to highlight focused services.
- Introduce `/services` content that explains engagements, pricing, and proof.
- Update navigation and supporting pages so the positioning feels consistent end to end.
- Validate visuals and copy with automated checks before publishing.

## Tasks
- [x] Finalize messaging updates for hero, CTA, and new “What I Help With” section.
- [x] Implement services page and wire navigation + footer links.
- [ ] Align About page and any shared components with the new positioning.
- [ ] Review analytics, SEO metadata, and sitemap for regressions after content changes.
- [ ] Run verification suite (lint, tests, snapshots) and prepare release notes.

## Progress
- 50% — Homepage hero updated and services page plus navigation wired on 2025-10-17.

## Surprises & Discoveries
- None yet.

## Decision Log
- Pricing stays visible (€200/hr) to filter prospects before outreach.
- Sessions remain bookable in 1–10 hour blocks; no retainers to emphasize flexibility.

## Verification
- `pnpm lint` and `pnpm test` must pass.
- Run `make snapshots` to regenerate and inspect UI previews.
- Manual pass through homepage, services, and about pages in local build before release.
