# AI Skill Adapter Layer

This directory is the primary adapter layer for AI tools that discover skills under `.agents/skills/`.

Canonical skill content is not duplicated here.

- Canonical source: `../../skills/<skill>/`
- Thin wrapper: `./<skill>/SKILL.md`
- Mirror index: `./skills_index.md`

Parsing rule:

1. Discover the wrapper under `.agents/skills/<skill>/SKILL.md`.
2. Read `metadata.canonical_path` from the wrapper.
3. Load the real skill definition from `skills/<skill>/SKILL.md`.
4. Use scripts, tests, references, templates, and examples only from the canonical directory.

Do not treat this adapter layer as the source of truth.
