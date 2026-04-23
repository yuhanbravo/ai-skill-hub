# Project-Side AGENTS.md Template Sketch (Phase 3A)

Status: this is a canonical sketch asset for a **future project-side runtime pack**.

This document does **not** create a real `AGENTS.md` in this repository.

## Purpose

Refine the Phase 2 thin-entrypoint draft into a v1 template sketch for a future project-side `AGENTS.md`.

The future file remains:

- the unified project-side master entrypoint;
- dispatch-oriented and reference-first;
- intentionally thin;
- non-canonical.

## Fixed vs Project-Fill Fields

### Fixed Fields

The following parts should stay fixed across future project-side uses because they express the canonical contract:

1. Identity statement:
   - `AGENTS.md` is the project-side master entrypoint.
   - It is dispatch-oriented and reference-first.
   - It is not canonical source-of-truth.
2. Required canonical reading requirement:
   - the file must list explicit canonical file-path references.
3. Conflict rule:
   - canonical guidance wins on conflict.
4. Anti-expansion boundary:
   - do not expand the file into a second local rulebook.
5. Execution orientation:
   - read canonical guidance first;
   - execute in bounded scope from task package;
   - report what changed vs. what was not implemented.

### Project-Fill Fields

The following parts should stay project-supplied:

1. Project name or repository identity.
2. Concrete project-local canonical skill path, if the repo has one.
3. Project-specific local boundaries that are not reusable across repos.
4. Optional local working constraints that are truly high-level and do not duplicate canonical guidance.

## Suggested Minimal Structure

A future project-side `AGENTS.md` should stay minimal with five sections:

1. Purpose
2. Canonical Guidance
3. High-Level Working Rules
4. Boundaries
5. Conflict Resolution

## Template Sketch

```md
# AGENTS.md

## Purpose
This file is the project-side runtime master entrypoint. It is dispatch-oriented and reference-first. It is not canonical source-of-truth.

Project: `<project-name>`

## Canonical Guidance
Read the required canonical guidance before implementation:

- `<canonical-workflow-guidance-path>`
- `<canonical-handoff-guidance-path>`
- `<project-local-canonical-skill-path>` (if present)

## High-Level Working Rules
1. Read required canonical guidance before implementation.
2. Execute in bounded scope from the active task package.
3. Record assumptions when project-local ambiguity exists.
4. Report what was changed and what was explicitly not implemented.

## Boundaries
- Keep this file thin and reference-first.
- Do not copy full workflow, governance, or skill guidance here.
- Keep project-specific local notes high-level only.
- If a reusable rule is missing, add it to canonical guidance rather than expanding this file.

## Conflict Resolution
If this file conflicts with canonical guidance, canonical guidance takes precedence.
```

## Field Notes

### Purpose

Fixed:

- the identity statement;
- the non-canonical declaration.

Project-fill:

- optional one-line project descriptor.

### Canonical Guidance

Fixed:

- explicit requirement to read canonical guidance first;
- explicit file-path-based reading list shape.

Project-fill:

- concrete resolved file paths;
- optional project-local canonical payload path.

### High-Level Working Rules

Fixed:

- bounded execution orientation;
- assumption logging;
- changed vs. not-implemented reporting.

Project-fill:

- at most a few local high-level constraints that do not duplicate canonical guidance.

### Boundaries

Fixed:

- no full workflow duplication;
- no governance duplication;
- no second rulebook.

Project-fill:

- small project-local constraints about scope or repo shape, if truly necessary.

### Conflict Resolution

Fixed:

- canonical guidance wins.

Project-fill:

- none required.

## Anti-Bloat Guardrail

The future `AGENTS.md` should be reviewed for drift if any of the following happens:

1. It starts adding topic-by-topic rules that belong in canonical skills.
2. It becomes longer than a thin entrypoint needs to be.
3. It repeats content already present in `.github/copilot-instructions.md`.
4. It carries detailed role-specific playbooks.

When that happens, the reusable content should move back to canonical guidance instead of staying only in the project-side file.
