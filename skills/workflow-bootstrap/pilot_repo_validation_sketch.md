# Pilot Repo Validation Sketch (Phase 3B)

Status: this is a canonical validation sketch asset for a **future project-side runtime pack**.

This document does **not** create any real consumer-repo runtime files.

## Purpose

Validate whether the Phase 2 / Phase 3A v1 entrypoint design remains stable when projected onto a single consumer-repo profile.

This validation stays in canonical layer only and does not enter implementation, rollout, distribution, or consumer-repo modification.

## Pilot Consumer Repo Profile (Validation-Only)

This phase uses one validation profile only:

- project type: Python script / analysis-oriented repository;
- repository state: already a Git repository;
- baseline structure: has `README` / `docs` / `src` / `tests`;
- future possibility: may later adopt project-side `AGENTS.md` and `.github/copilot-instructions.md`.

Boundary note: this is a validation profile, not a selected real consumer repository.

## Why This Profile Is Used

1. It is common enough to validate v1 thin-entrypoint assumptions.
2. It has enough structure (`docs`, `src`, `tests`) to stress path-expression stability.
3. It avoids overfitting Phase 3B to one special workflow pattern.
4. It supports bounded validation without entering real implementation.

## V1 Entrypoint Combination Validation

Validation question: for this single profile, is `AGENTS.md` + `.github/copilot-instructions.md` sufficient for v1?

Validation result: **yes, sufficient for v1** under current boundaries.

Reasoning:

1. `AGENTS.md` can remain the project-side master entrypoint for cross-agent dispatch.
2. `.github/copilot-instructions.md` can remain a Copilot-specific thin adapter.
3. The pair can keep canonical backreference mandatory and explicit.
4. Additional surfaces are not required to validate basic operation in this profile.

## Required / Optional / Deferred Validation (Profile-Mapped)

For this single profile, the v1 file-family decision remains:

- **Required**
  - `AGENTS.md` (future project-side master entrypoint)
  - `.github/copilot-instructions.md` (future Copilot-specific thin adapter)
- **Optional**
  - `.github/instructions/*.instructions.md` (only when one stable sub-area truly needs separate constraints)
- **Deferred / Not Recommended in V1**
  - `.github/agents/*.agent.md` (defer until base entrypoint pair is proven stable in a real implementation phase)

This is a validation classification only and does not authorize file creation in any consumer repo.

## Field and Placeholder Mapping Validation (Contained Here Intentionally)

This section keeps field/placeholder mapping in the same file to avoid premature document split and preserve readability.

### A) Future `AGENTS.md`

#### Fixed fields (canonical contract)

1. Identity: project-side master entrypoint, dispatch-oriented, reference-first, non-canonical.
2. Required canonical reading declaration with explicit file paths.
3. Conflict precedence: canonical guidance wins on conflict.
4. Anti-expansion boundary: do not become a second local rulebook.

#### Project-fill fields

1. Project/repo identity line.
2. Project-local canonical payload path (if present).
3. High-level local boundaries that are genuinely project-specific.

#### Placeholder fields

1. `<canonical-workflow-guidance-path>`
2. `<canonical-handoff-guidance-path>`
3. `<project-local-canonical-skill-path>` (if present)

Validation conclusion: this split is still workable for the profile and keeps v1 thin.

### B) Future `.github/copilot-instructions.md`

#### Fixed rules

1. Copilot-specific thin-adapter identity.
2. Explicit statement that `AGENTS.md` remains master entrypoint.
3. Bounded-execution reminder.
4. Canonical backreference reminder.
5. Non-duplication boundary (do not restate full workflow/governance content).

#### Project-specific fill scope

1. Concrete resolved path references.
2. At most a very small number of high-frequency local Copilot constraints.

#### Content that should not appear

1. Full workflow handbook text.
2. Full governance handbook text.
3. Full restatement of `AGENTS.md`.
4. Role-specific deep playbooks.

Validation conclusion: thin-adapter boundary is sufficient for this profile and remains distinct from master entrypoint responsibilities.

## Canonical Path Backreference Validation

### Stable expression pattern

Use explicit file-path references with placeholders in sketch stage:

- `<canonical-workflow-guidance-path>`
- `<canonical-handoff-guidance-path>`
- `<project-local-canonical-skill-path>`

### Fields that must be project-filled later

1. Real resolved workflow-guidance path.
2. Real resolved handoff-guidance path.
3. Real project-local canonical payload path (if present).

### Anti-brittle rules

1. Do not use directory-only references such as `skills/`.
2. Do not use host-specific absolute paths.
3. Do not assume hub and consumer repo share identical structure.
4. Keep placeholders in sketch stage; resolve to concrete relative file paths only in implementation phase.

Validation conclusion: placeholder-first with required later resolution is the most robust approach for this profile.

## Anti-Second-Rulebook Validation

### Highest-risk expansion points in project-side runtime pack

1. Expanding `AGENTS.md` into full workflow or governance manual.
2. Expanding `.github/copilot-instructions.md` into duplicated all-purpose handbook.
3. Adding optional/deferred file families too early to compensate for unclear ownership.

### Content that must stay canonical

1. Reusable cross-repo workflow rules.
2. Reusable handoff and bounded-execution protocol text.
3. Reusable governance-level guidance.

### Content allowed as local summary only (not full copy)

1. Short high-frequency reminders.
2. Thin dispatch and routing hints.
3. Minimal project-local constraints that are not reusable across repos.

Validation conclusion: the existing guardrails remain sufficient in this profile if enforced at entrypoint boundaries.

## Explicit Non-Implementation Statement

This Phase 3B asset is a canonical validation sketch only.

It does not create, modify, or claim implementation of any real consumer-repo runtime files.
