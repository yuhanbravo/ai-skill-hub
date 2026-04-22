# Copilot Instructions Thin Adapter Draft (Phase 2)

Status: this is a canonical draft asset for a **future project-side runtime pack**.

This draft does not create a real `.github/copilot-instructions.md` in this repository.

## Purpose

Define the future `.github/copilot-instructions.md` as a Copilot-specific thin adapter.

- It is not the project-side master entrypoint.
- It must backreference `AGENTS.md`.
- It keeps only high-frequency, high-constraint Copilot guidance.

### Required explicit identity statement

> This file is a Copilot-specific thin adapter. It does not replace AGENTS.md as the project-side master entrypoint.

## High-Frequency Rules

Future `.github/copilot-instructions.md` should retain only concise, high-frequency constraints, such as:

1. Follow `AGENTS.md` first for repo-wide workflow entry.
2. Stay within bounded scope from task package.
3. Prefer canonical references over duplicated local rule text.
4. Escalate ambiguity to canonical guidance, not local expansion.
5. Keep references concrete (file paths), not broad directory-only hints.

### Recommended fixed boundary text

> Keep this file short. Do not turn it into a full workflow/governance/skill rulebook.

## Where Full Guidance Lives

Future `.github/copilot-instructions.md` should explicitly point to:

1. `AGENTS.md` as project-side master entrypoint.
2. Canonical skill guidance for full workflow and governance rules.
3. Project-local canonical skill payload (if present).

Recommended placeholder path format:

- `AGENTS.md`
- `skills/workflow-bootstrap/SKILL.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`
- `<project-local-canonical-skill-path>`

### Required explicit non-replacement statement

> This file does not replace AGENTS.md and does not duplicate full workflow, governance, or skill documentation.

## Suggested Minimal Structure

A future project-side `.github/copilot-instructions.md` can remain minimal with three sections:

1. Purpose
2. High-Frequency Rules
3. Where Full Guidance Lives

This structure preserves adapter value without creating a second rule library.
