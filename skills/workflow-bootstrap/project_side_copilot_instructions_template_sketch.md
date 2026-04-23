# Project-Side Copilot Instructions Template Sketch (Phase 3A)

Status: this is a canonical sketch asset for a **future project-side runtime pack**.

This document does **not** create a real `.github/copilot-instructions.md` in this repository.

## Purpose

Refine the Phase 2 thin-adapter draft into a v1 template sketch for a future project-side `.github/copilot-instructions.md`.

The future file remains:

- a Copilot-specific thin adapter;
- not the project-side master entrypoint;
- mandatory backreference to `AGENTS.md`;
- limited to high-frequency, high-constraint guidance only.

## What This File Should Keep

Future `.github/copilot-instructions.md` should keep only:

1. A short identity statement saying it is a thin adapter and does not replace `AGENTS.md`.
2. A short instruction to follow `AGENTS.md` first for repo-wide workflow entry.
3. A very small set of high-frequency constraints that are especially useful for Copilot.
4. Concrete backreferences to `AGENTS.md` and canonical guidance.

## What Must Stay Out

Future `.github/copilot-instructions.md` should **not** contain:

1. Full workflow guidance.
2. Full governance guidance.
3. Full project handbook content.
4. A restated copy of `AGENTS.md`.
5. Detailed role-specific playbooks.
6. Long local rule lists that belong in canonical guidance or project-local canonical payload.

## Suggested Minimal Structure

A future project-side `.github/copilot-instructions.md` should stay minimal with three sections:

1. Purpose
2. High-Frequency Rules
3. Where Full Guidance Lives

## Template Sketch

```md
# Copilot Instructions

## Purpose
This file is a Copilot-specific thin adapter. It does not replace AGENTS.md as the project-side master entrypoint.

## High-Frequency Rules
1. Follow `AGENTS.md` first for repo-wide workflow entry.
2. Stay within bounded scope from the active task package.
3. Prefer canonical references over duplicated local rule text.
4. Escalate ambiguity to `AGENTS.md` or canonical guidance instead of expanding this file.
5. Keep references concrete and file-path-based.

## Where Full Guidance Lives
- `AGENTS.md`
- `<canonical-workflow-guidance-path>`
- `<canonical-handoff-guidance-path>`
- `<project-local-canonical-skill-path>` (if present)
```

## Non-Repetition Rule

The future Copilot adapter should only summarize what is needed to route Copilot quickly.

Keep in `AGENTS.md`, not here:

- master-entry identity;
- full project-side working boundaries;
- detailed conflict and governance explanations;
- cross-agent workflow framing.

Keep here, not expanded further:

- short Copilot-facing reminder to use `AGENTS.md`;
- short bounded-execution reminder;
- short canonical-backreference reminder.

## Fixed vs Project-Fill Fields

### Fixed Fields

1. The thin-adapter identity statement.
2. The statement that `AGENTS.md` remains the master entrypoint.
3. The high-frequency reminder set.
4. The requirement to use explicit file paths.
5. The non-duplication boundary.

### Project-Fill Fields

1. Concrete resolved canonical paths.
2. Optional project-local canonical payload path.
3. At most a very small number of Copilot-specific local constraints if they are truly high-frequency and not duplicated elsewhere.

## Anti-Bloat Guardrail

Review the future file if any of the following starts to happen:

1. It grows into a multi-section local handbook.
2. It repeats most of `AGENTS.md`.
3. It starts carrying rules that are not specifically high-frequency for Copilot.
4. It becomes the de facto place where reusable workflow rules are edited first.

If any of these occurs, reduce the adapter and move reusable material back into canonical guidance or the project-side master entrypoint.
