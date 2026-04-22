# Phase 2 Execution Report: AGENTS.md / Copilot Thin Entrypoint Drafts (Re-run)

## Scope Restatement

This execution implemented only Phase 2 canonical draft assets for thin entrypoint design under `skills/workflow-bootstrap/`.

In-scope output was limited to:

1. `AGENTS.md` thin master-entry draft (canonical asset only).
2. `.github/copilot-instructions.md` thin adapter draft (canonical asset only).
3. Canonical backreference enforcement rules draft.
4. Minimal README navigation update (canonical documentation navigation only).
5. This execution report.

Constraint note: `tasks/copilot-codex-workflow_phase2_task_package.md` is still not present in the current Codex Cloud repository snapshot at execution time. This re-run therefore remained conservative and aligned to the existing decision memo plus previously established Phase 2 bounded scope.

## Files Changed

- Added: `skills/workflow-bootstrap/canonical_backreference_rules_draft.md`
- Added: `skills/workflow-bootstrap/agents_md_thin_entrypoint_draft.md`
- Added: `skills/workflow-bootstrap/copilot_instructions_thin_adapter_draft.md`
- Updated: `skills/workflow-bootstrap/README.md` (minimal Phase 2 draft navigation section)
- Updated: `tasks/copilot-codex-workflow_phase2_execution_report.md` (this re-run report)

## What Was Drafted

### 1) Canonical backreference rules draft

Created a reusable rule set covering the required four-part mechanism:

1. entrypoint identity,
2. required canonical reading list,
3. canonical precedence on conflict,
4. no second rulebook.

Also included reusable fixed text blocks for both future `AGENTS.md` and future `.github/copilot-instructions.md`.

Re-run enhancement: added explicit placeholder path style and a compact Phase 2 compliance checklist to reduce interpretation drift during future project-side template drafting.

### 2) `AGENTS.md` thin entrypoint draft

Drafted a future `AGENTS.md` specification as:

- unified project-side master entrypoint,
- dispatch-oriented and reference-first,
- explicitly non-canonical,
- constrained against local rulebook expansion,
- canonical-first on conflict.

Included required sections:

- Purpose,
- Canonical Guidance,
- High-Level Working Rules,
- Boundaries,
- Conflict Resolution.

Re-run enhancement: tightened the “required canonical reading list” to emphasize file-path-level references and added explicit identity requirements for dispatch-first behavior.

### 3) Copilot thin adapter draft

Drafted future `.github/copilot-instructions.md` as:

- Copilot-specific thin adapter,
- explicitly not a master entrypoint,
- mandatory backreference to `AGENTS.md`,
- high-frequency/high-constraint only,
- no full workflow/governance/skill duplication.

Included required sections:

- Purpose,
- High-Frequency Rules,
- Where Full Guidance Lives.

Re-run enhancement: added explicit “concrete file-path reference” expectation and a placeholder path format block to keep the adapter thin but operationally clear.

### 4) README minimal navigation supplement

Added a very small “Phase 2 Draft Assets (Canonical Only)” section listing the three new draft files and explicitly clarifying they are design drafts, not implemented project-side runtime files.

## What Was Explicitly Not Implemented

- No real project-side runtime files were created:
  - no repository-root `AGENTS.md`,
  - no `.github/copilot-instructions.md`,
  - no `.github/instructions/*.instructions.md`,
  - no `.github/agents/*.agent.md`.
- No runtime-pack full template system was implemented.
- No rollout/distribution/export/import/adapter/index tooling changes were made.
- No changes were made to other skills’ core contracts.

## Boundary Check

- `skills/` remained canonical source-of-truth.
- Added files are canonical draft assets only.
- Draft language explicitly avoids claiming project-side runtime files already exist.
- `chatgpt-handoff-pilot` ownership of protocol layer was not modified.
- README change was limited to minimal navigation only.

## Risks / Assumptions

1. Assumption: Missing `tasks/copilot-codex-workflow_phase2_task_package.md` in this Codex Cloud snapshot indicates sync lag, branch divergence, or filename/path mismatch.
2. Risk: Future implementation teams may still over-expand project-side entrypoints without enforcement checks.
3. Mitigation in this draft: repeated explicit “thin-entrypoint / no second rulebook / canonical wins” language in all three draft assets.

## Recommended Next Step

If Phase 3 is authorized, use these canonical drafts to produce a tightly bounded project-side runtime pack template proposal (still without rollout), and verify path-level references against a concrete target repository structure before any distribution step.

## Validation Notes (Executed)

- Performed document-boundary check by verifying no real project-side runtime files were created.
- Performed consistency check against the Phase 2 decision memo and Phase 1 layering intent.
- Performed expression check for required explicit statements:
  - `AGENTS.md` as master-entry draft,
  - Copilot file as thin adapter draft,
  - canonical precedence on conflict,
  - no-second-rulebook constraint.
