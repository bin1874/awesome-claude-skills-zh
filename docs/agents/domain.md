# Domain Docs

This repo uses a **single-context** layout for domain documentation.

## Location

- **Domain context**: `CONTEXT.md` at repo root
- **Architectural decisions**: `docs/adr/` directory

## Consumer Rules

Skills that read domain docs follow these rules:

1. **Read `CONTEXT.md` first** — contains the project's domain language, key concepts, and terminology
2. **Check `docs/adr/` for decisions** — Architectural Decision Records (ADRs) document past decisions and their rationale
3. **Respect existing terminology** — use the language defined in CONTEXT.md when discussing the domain

## ADR Format

ADRs in `docs/adr/` should follow this naming convention:

- `NNNN-title-with-dashes.md` (e.g., `0001-use-jekyll-for-docs.md`)
- Include: Status, Context, Decision, Consequences

## Note

This is a documentation/translation project rather than a traditional codebase. CONTEXT.md should describe the domain of Claude Skills (workflow patterns, skill structure, translation conventions) rather than business logic.
