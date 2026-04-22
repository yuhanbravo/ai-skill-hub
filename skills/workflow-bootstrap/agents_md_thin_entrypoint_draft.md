# AGENTS.md Thin Entrypoint Draft (Phase 2)

Status: this is a canonical draft asset for a **future project-side runtime pack**.

This draft does not create a real `AGENTS.md` in this repository.

## Purpose

Define the future `AGENTS.md` as the unified project-side master entrypoint.

- Positioning: dispatch-oriented, reference-first, thin-entrypoint.
- Responsibility: route users/agents to canonical guidance and enforce top-level boundaries.
- Non-goal: become canonical source-of-truth.

## Canonical Guidance

Future `AGENTS.md` should include an explicit identity statement and a required canonical reading list.

### Recommended fixed identity statement

> This file is the project-side runtime master entrypoint. It is dispatch-oriented and reference-first. It is not canonical source-of-truth.

### Required canonical reading list (example structure)

Use explicit file paths in the target project (not directory-only references). At minimum include:

1. Workflow bootstrap canonical guidance.
2. Handoff / bounded execution canonical guidance (`chatgpt-handoff-pilot` related).
3. Project-local canonical skill payload (if present).

Recommended placeholder path format:

- `skills/workflow-bootstrap/SKILL.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`
- `<project-local-canonical-skill-path>`

## High-Level Working Rules

Future `AGENTS.md` should keep only thin, high-level operating constraints:

1. Read required canonical guidance before implementation.
2. Execute in bounded scope from task package.
3. Report what was changed vs. explicitly not implemented.
4. Record assumptions when ambiguity exists.

Identity requirement (must be explicit in future file):

- it is a project-side runtime entrypoint;
- it is not canonical source-of-truth;
- it dispatches and backreferences canonical guidance first.

## Boundaries

Future `AGENTS.md` should explicitly include all of the following:

- It does not replace canonical skills in `skills/`.
- It does not replace handoff protocol ownership (`chatgpt-handoff-pilot`).
- It must not copy full workflow/governance/skill documentation.
- It must not expand into a second local rulebook.

### Recommended fixed boundary text

> Do not expand this file into a full local rulebook. Keep it thin and reference-first. Full guidance remains in canonical skill documents.

## Conflict Resolution

Future `AGENTS.md` should include an explicit precedence rule:

- if `AGENTS.md` conflicts with canonical guidance, canonical guidance wins.

### Recommended fixed conflict text

> On conflict, canonical guidance takes precedence over this entrypoint.

## Suggested Minimal Structure

A future project-side `AGENTS.md` can stay minimal with five sections:

1. Purpose
2. Canonical Guidance
3. High-Level Working Rules
4. Boundaries
5. Conflict Resolution

This keeps the entrypoint stable while preventing drift and duplicate governance text.
