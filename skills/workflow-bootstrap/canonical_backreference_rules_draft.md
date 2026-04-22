# Canonical Backreference Rules Draft (Phase 2)

Status: this document is a **canonical draft asset** for future project-side runtime pack design.

- Applies to: future project-side runtime pack entry files.
- Stored as: canonical draft in `ai-skill-hub` only.
- Not a fact claim: this file does **not** mean project-side runtime files already exist in this repository.

## Purpose

Provide a reusable, minimal “forced backreference” rule set so project-side entrypoints stay thin and keep canonical guidance as source-of-truth.

为避免歧义，本草案仅定义 **future project-side runtime pack** 的入口约束文案，不声明当前 hub 内已存在这些 project-side runtime files。

## Required Rule Set (Four Essentials)

### 1) Entrypoint Identity
Any project-side entrypoint must explicitly state:

- it is an entry/dispatch file;
- it is reference-first and thin;
- it is **not** canonical source-of-truth.

### 2) Required Canonical Reading List
Any project-side entrypoint must include a mandatory canonical reading list with concrete file paths (not directory-only references).

At minimum, the list should include:

- workflow bootstrap guidance;
- handoff / bounded execution guidance (`chatgpt-handoff-pilot` related);
- project-local canonical skill payload (if present).

Recommended path style (example placeholders for future project repos):

- `skills/workflow-bootstrap/SKILL.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`
- `<project-local-canonical-skill-path>`

### 3) Canonical Wins on Conflict
Any project-side entrypoint must include an explicit precedence statement:

- if project-side entry text conflicts with canonical guidance, canonical guidance wins.

### 4) No Second Rulebook
Any project-side entrypoint must explicitly prohibit local expansion into a second full rulebook.

Allowed:

- high-frequency constraints;
- dispatch hints;
- references to canonical guidance.

Not allowed:

- full workflow duplication;
- full governance duplication;
- full skill-by-skill rule duplication.

## Reusable Fixed Text Drafts

### A) Reusable text for future `AGENTS.md`

```md
## Identity
This file is the project-side runtime entrypoint. It is dispatch-oriented, reference-first, and intentionally thin. It is not the canonical source of truth.

## Required Canonical Reading
Before execution, read the required canonical guidance files listed below (use explicit file paths, not directory-only references).

## Conflict Resolution
If this file conflicts with canonical guidance, canonical guidance takes precedence.

## Boundary
Do not expand this file into a second local rulebook. Keep only high-frequency constraints and canonical backreferences.
```

### B) Reusable text for future `.github/copilot-instructions.md`

```md
## Identity
This file is a Copilot-specific thin adapter. It is not the project-side master entrypoint and does not replace AGENTS.md.

## Where Full Guidance Lives
Full workflow and governance guidance lives in AGENTS.md and canonical skill documents.

## Conflict Resolution
If this file conflicts with AGENTS.md or canonical guidance, AGENTS.md and canonical guidance take precedence.

## Boundary
Do not expand this file into a full rulebook. Keep only high-frequency Copilot constraints and backreferences.
```

## Notes for Future Runtime Pack Use

When these rules are reused in future project-side runtime packs:

- keep project-side entries small and stable;
- keep canonical updates centralized;
- reduce drift caused by duplicated rules.

## Phase 2 Compliance Checklist (Draft-Level)

- Entrypoint identity is explicit.
- Required canonical reading list exists and uses concrete file paths.
- Conflict rule explicitly says canonical guidance wins.
- “No second rulebook” boundary is explicit.
- Copilot adapter text explicitly backreferences `AGENTS.md`.
