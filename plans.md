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
- [x] Align About page and any shared components with the new positioning.
- [x] Review analytics, SEO metadata, and sitemap for regressions after content changes.
- [x] Run verification suite (lint, tests, snapshots) and prepare release notes.

## Progress
- 100% — Copy, navigation, About, and verification complete on 2025-10-17.

## Surprises & Discoveries
- ESLint surfaced minified Plausible scripts; added ignore for `public/stats*.js` to keep the check actionable.

## Decision Log
- Pricing stays visible (€200/hr) to filter prospects before outreach.
- Sessions remain bookable in 1–10 hour blocks; no retainers to emphasize flexibility.
- Introduced a lightweight Vitest check for the services page to lock in critical copy.

## Verification
- `pnpm lint` and `pnpm test` must pass.
- Run `make snapshots` to regenerate and inspect UI previews.
- Manual pass through homepage, services, and about pages in local build before release.
- `pnpm build` before publishing; release notes recorded in `notes/2025-10-17-repositioning.md`.
