# AI_USAGE

This document explains how this repository exposes skills to multiple AI tools while keeping `skills/` as the single source of truth.

## Naming

- Canonical repository name: `ai-skill-hub`
- Consumer-facing compatibility directories such as `.codex/`, `.codex/skills/`, and `.codex/skill-config/` remain valid and are not renamed by this repository refactor.

## Discovery Paths

- Primary canonical source: `skills/<skill>/`
- Primary adapter layer: `.agents/skills/<skill>/SKILL.md`
- Copilot fallback layer: `.github/skills/<skill>.md`
- Human-readable fallback index: `SKILLS_INDEX.md`

## How To Use In AI Tools That Scan `.agents/skills`

1. Discover the skill under `.agents/skills/<skill>/SKILL.md`.
2. Read the wrapper frontmatter to get `name`, `description`, and `metadata`.
3. Use `metadata.triggers`, `metadata.side_effects`, and `metadata.canonical_path` as the adapter metadata.
4. Load the canonical definition from `skills/<skill>/SKILL.md`.
5. Read additional assets only from the canonical directory, such as `scripts/`, `tests/`, `references/`, `examples/`, or `templates/`.

## How To Use In GitHub Copilot

1. Discover the compatibility entry under `.github/skills/<skill>.md`.
2. Read the canonical path from that entry.
3. Continue with `skills/<skill>/SKILL.md` as the authoritative definition.
4. If Copilot cannot infer the correct skill from the compatibility entry alone, consult `SKILLS_INDEX.md`.

## Why The Repository Does Not Duplicate Skill Content

- `skills/` is the only source of real skill content.
- Adapter files are intentionally thin and only exist to improve discoverability.
- Scripts, tests, references, prompts, templates, and examples remain under canonical skill directories.
- This avoids metadata drift across multiple full copies of the same skill.

## How To Add A New Skill

1. Create the canonical directory under `skills/<new-skill>/`.
2. Start from `skills/SKILL_TEMPLATE.md` and create `skills/<new-skill>/SKILL.md`.
3. Fill in `name`, `description`, and `metadata.triggers` plus `metadata.side_effects`.
4. Add any canonical assets under the same directory, such as `README.md`, `scripts/`, `tests/`, `references/`, `templates/`, or `examples/`.
5. Create a thin wrapper at `.agents/skills/<new-skill>/SKILL.md` pointing back to the canonical path.
6. Create a Copilot compatibility entry at `.github/skills/<new-skill>.md`.
7. Add the new skill to `SKILLS_INDEX.md`.

## Authoring Rules

- Change behavior only in `skills/<skill>/`.
- Keep adapter files short and path-oriented.
- Do not place scripts, tests, or references under `.agents/skills/` or `.github/skills/`.
- If an AI tool supports only one discovery location, direct it to the canonical path instead of creating a second full skill copy.

## SkillHub Projects And Status Templates

A `skill-hub project` is a repository whose main maintained assets are skills, adapters, invocation contracts, indexes, governance docs, tests, and automation scripts.

When `update-project-status` is used on a skill-hub project, prefer a config with `template_type` set to `skillhub`.

Example:

```json
{
  "template_type": "skillhub",
  "status_dimensions": [
    "skill_coverage",
    "invocation_readiness",
    "governance_readiness",
    "automation_readiness"
  ]
}
```

This keeps the `update-project-status` core logic unchanged while switching the output structure from a general project view to a skill-hub-oriented status view.
