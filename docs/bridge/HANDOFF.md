# HANDOFF

> Status: semantic mirror of active source [../HANDOFF.md](../HANDOFF.md)
>
> Ownership: active updates continue in `docs/HANDOFF.md`
>
> Purpose: bridge-facing handoff continuity for AI and human maintainers without changing the active handoff path

This file is the single source of truth for project handoff.

## Update Log

- 2026-03-30: Initialized the system handoff document for `ai-skill-hub` and captured the current phase, hard boundaries, design decisions, intentional gaps, and next-phase direction.
- 2026-03-31: Merged the current system-state refresh, selective rollout control, DryRun contract hardening, and system-wrapper invocation surfaces into the handoff brief without rewriting the document.
- 2026-04-01: Merged the new re-seed preflight audit capability and conservative hub self-detection into the system handoff, while preserving the existing phase model and wrapper-only boundaries.

## Current Status

`ai-skill-hub` is currently in `Phase 3 - Controlled System`.

The system has already moved beyond a simple skill repository and now operates as an AI capability system with four active layers:

- Canonical Skill Layer: `skills/` remains the stable canonical source for skill definitions and invocation contracts, now including system-level wrapper skills for status and handoff without forking canonical behavior.
- Distribution Layer: the system supports hub-side discovery surfaces and project-side runtime distribution through `.codex`, `.agents`, and `.github`, and rollout can now be scoped by target layer while preserving default behavior.
- Governance Layer: the system has a read-only adapter consistency check plus regression coverage for DryRun no-side-effect behavior, adapter reference correctness, and rollout-target audit classification.
- Tooling Layer: sync, metadata, routing, pipeline, local governance tooling, and a standalone re-seed preflight audit path are available as repeatable operational capabilities; system invocation also has explicit wrapper entrypoints for status and handoff.

Overall system maturity is `evolving`: the canonical layer is stable, distribution and governance are increasingly controlled, and system-level invocation surfaces are now explicit but still intentionally thin.

## Hard Boundaries

- `skills/<skill>/` remains the only canonical source of truth inside the hub. No adapter layer may become a second authoritative source.
- `system-status-update` and `system-handoff` must remain wrapper skills. They may reuse canonical skills and add system-level output constraints, but they must not fork canonical logic.
- In distributed business-project contexts, `.codex/skills/` is the runtime SSOT for local skill content. Project-local adapters must point to `.codex/skills/`, not back to hub `skills/` paths.
- Governance at the current stage is read-only. Consistency checks may detect drift, but they must not auto-fix, auto-delete, or silently rewrite adapters.
- Re-seed auditing remains preflight-only. Audit tooling may classify rollout readiness and identify hub repositories, but it must not silently execute reseed, sync, delete, or project mutation.
- Adapter layers exist for discoverability, not authorship. `.agents/skills/` and `.github/skills/` must remain derivative surfaces.
- Sync-back semantics stay constrained to canonical content recovery. Project-local adapters are not treated as editable upstream sources.
- Selective rollout control may narrow where distribution lands, but it must not redefine canonical ownership or promote adapter layers into authoring surfaces.
- `ai-skill-hub` itself is not a normal clean re-seed target. Hub self-detection is allowed as a protective boundary so the system repository is not misclassified as a consumer project.
- System evolution must preserve layer clarity: canonical definition, distribution surfaces, governance checks, and orchestration tooling cannot be collapsed into a single mutable layer.

## Key Design Decisions

- The hub keeps `skills/` as the sole canonical layer because duplicated skill content across adapters would create metadata drift and blur ownership.
- The system uses thin adapter surfaces instead of full adapter copies because discoverability is needed across AI entrypoints, but content duplication would weaken governance.
- System-level status and handoff are implemented as wrapper skills over canonical capabilities because the system needs standardized invocation semantics without introducing a second status engine or handoff framework.
- Project distribution keeps `.codex/skills/` as the local runtime SSOT because business projects need a stable local skill-content root without becoming a second canonical hub.
- Project-local `.agents/.github` adapters are generated around `.codex/skills/` instead of copied from the hub because copied hub adapters would carry broken references and violate project-local path correctness.
- Governance starts with read-only drift detection because the current system priority is visibility and boundary control, not automatic mutation or destructive cleanup.
- Selective rollout was added at the sync layer because distribution control was needed, but the default path was preserved to avoid creating a second distribution policy surface.
- Re-seed readiness was added as a separate audit tool instead of being folded into the sync path because rollout preflight needs a read-only decision surface, not a hidden execution side effect.
- Hub self-detection stays conservative because boundary protection matters more than aggressive classification; it is better to miss some hubs than to misclassify ordinary projects as system repositories.
- The system remains phase-based because capability maturity is uneven across layers; canonical definition is already stable, while governance enforcement and orchestration still need controlled progression.

## Intentional Gaps

- No auto-fix for adapter drift.
- No CI-backed enforcement for adapter consistency yet.
- No expansion of governance into destructive sync, delete, or rewrite behavior.
- No orchestration or controller layer around `system-status-update` and `system-handoff`.
- No auto-reseed or auto-remediation path inside the re-seed audit tool.
- No aggressive hub fingerprinting beyond a conservative strong-signal guard.
- No redesign of metadata generation or adapter schema in this phase.
- No promotion of project-local adapters into upstream authoring surfaces.
- No attempt to turn heuristic routing and sequencing into a fully deterministic orchestration stack in the current phase.

These gaps are intentional to keep the system legible while distribution and governance semantics are still being stabilized.

## Next Phase Direction

The next phase should move the system from `controlled local governance` toward `controlled enforcement`, while preserving the current single-source layering model, the thin-wrapper system invocation model, and the new preflight-before-rollout boundary.

Directionally, this means strengthening confidence in cross-layer consistency, making orchestration behavior less heuristic, and increasing repeatability without giving up the current hard boundaries around canonical ownership, read-only governance transitions, preflight-only audit semantics, and wrapper-only system invocation surfaces.

The objective is not to add more surfaces or a controller framework, but to make the existing layers more trustworthy, more enforceable, and easier for future maintainers or AI agents to operate without ambiguity.
