# AGENTS.md — Tool Selection

When you need to call tools from the shell, use this rubric:

## File & Text
- Find Files: `fd`
- Find Text: `rg` (ripgrep)
- Find Code Structure: `ast-grep`
  - Common languages:
    - Python → `ast-grep --lang python -p '<pattern>'`
    - TypeScript → `ast-grep --lang ts -p '<pattern>'`
    - Bash → `ast-grep --lang bash -p '<pattern>'`
    - TSX (React) → `ast-grep --lang tsx -p '<pattern>'`
    - JavaScript → `ast-grep --lang js -p '<pattern>'`
    - Rust → `ast-grep --lang rust -p '<pattern>'`
    - JSON → `ast-grep --lang json -p '<pattern>'`
  - Prefer `ast-grep` over ripgrep/grep unless a plain-text search is explicitly requested.
- Select among matches: pipe to `fzf`

## Data
- JSON: `jq`
- YAML/XML: `yq`

When executing complex changes:
- Maintain an "exec plan" in plans.md (create/update it).
- Keep progress, decisions, and discoveries up to date.
- Do not land code until tests and reviews pass.
- Prefer small, verifiable increments.

Codex will generate and iterate the plan; you review then tell it to execute.

## Make verification cheap and continuous

Long tasks need continuous feedback; Codex thrives with strong signals.
 • Automated tests: Unit, property, and fuzz tests. Codex runs, fixes, re-runs until green.
 • Visual checks (UI): Snapshot testing so Codex can “see” results and compare against expectations.
 • Snapshot tool: run `make snapshots` to generate fresh previews from `tests/test_previews.py`.
 • Tight loop: Kick tests often; if red too long, intervene and adjust plan.

- read CLAUDE.md for more details if needed
