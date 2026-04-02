# HANDOFF

This file is the single source of truth for project handoff.

## Update Log

- 2026-03-30: Initialized the system handoff document for `ai-skill-hub` and captured the current phase, hard boundaries, design decisions, intentional gaps, and next-phase direction.
- 2026-03-31: Merged the current system-state refresh, selective rollout control, DryRun contract hardening, and system-wrapper invocation surfaces into the handoff brief without rewriting the document.
- 2026-04-01: Merged the new re-seed preflight audit capability and conservative hub self-detection into the system handoff, while preserving the existing phase model and wrapper-only boundaries.
- 2026-04-02: Merged a `system-takeover` pass into the handoff, capturing the explicit AI/Human/Bridge documentation split, the current system capability map, the router mismatch around `system-takeover`, and the hub-vs-consumer governance boundary.
- 2026-04-02: Refreshed the system status and merged the latest bridge-reference audit into the handoff, confirming that current docs/bridge/* hits remain documentation-facing and identifying the remaining direct compatibility link in AI_USAGE.md.

## Current Status

`ai-skill-hub` is currently in `Phase 3 - Controlled System`.

The system has already moved beyond a simple skill repository and now operates as an AI capability system with six active layers:

- Canonical Skill Layer: `skills/` remains the stable canonical source for skill definitions and invocation contracts, now including system-level wrapper skills for status and handoff without forking canonical behavior.
- Invocation Layer: `docs/ai/EXECUTION_PROTOCOL.md`, `docs/ai/INVOCATION_PROTOCOL.md`, and `docs/ai/DISCOVERY_AND_INVOCATION.md` now hold the explicit AI-facing execution, invocation, and discovery contracts instead of leaving those rules implicit in mixed docs.
- Routing / Pipeline Layer: `tools/skill_router.py` and `tools/skill_pipeline.py` provide lightweight task-to-skill matching and ordered multi-skill sequencing, but they still behave as heuristic orchestration helpers rather than deterministic controllers.
- Distribution Layer: the system supports hub-side discovery surfaces and project-side runtime distribution through `.codex`, `.agents`, and `.github`, and rollout can now be scoped by target layer while preserving default behavior.
- Governance Layer: the system has a read-only adapter consistency check plus regression coverage for DryRun no-side-effect behavior, adapter reference correctness, and rollout-target audit classification.
- Documentation Layer: `docs/ai`, `docs/human`, and `docs/bridge` now split protocol, explanation, and exchange assets into explicit ownership layers while keeping `docs/HANDOFF.md` and `docs/status/skill-hub-status.md` as active sources.
- Tooling Layer: sync, metadata, routing, pipeline, local governance tooling, and a standalone re-seed preflight audit path are available as repeatable operational capabilities; system invocation also has explicit wrapper entrypoints for status and handoff.

Overall system maturity is `evolving`: the canonical and invocation layers are stable, documentation ownership is clearer, distribution and governance are increasingly controlled, routing/orchestration remain intentionally lightweight and still somewhat heuristic, and the current bridge-reference surface has now been audited as documentation-facing rather than runtime-facing.

## Hard Boundaries

- `skills/<skill>/` remains the only canonical source of truth inside the hub. No adapter layer may become a second authoritative source.
- `system-status-update` and `system-handoff` must remain wrapper skills. They may reuse canonical skills and add system-level output constraints, but they must not fork canonical logic.
- In distributed business-project contexts, `.codex/skills/` is the runtime SSOT for local skill content. Project-local adapters must point to `.codex/skills/`, not back to hub `skills/` paths.
- Governance at the current stage is read-only. Consistency checks may detect drift, but they must not auto-fix, auto-delete, or silently rewrite adapters.
- Re-seed auditing remains preflight-only. Audit tooling may classify rollout readiness and identify hub repositories, but it must not silently execute reseed, sync, delete, or project mutation.
- Adapter layers exist for discoverability, not authorship. `.agents/skills/` and `.github/skills/` must remain derivative surfaces.
- AI / Human / Bridge documentation ownership must stay explicit. `docs/ai/` owns execution-facing protocol, `docs/human/` owns explanation-oriented repository guidance, and `docs/bridge/` remains a mirror/exchange layer rather than a new active source.
- Existing docs/bridge/* references may serve navigation, mirror, or exchange semantics, but they must not become script, config, or runtime activation dependencies.
- Hub-local adapter wrappers and project-local adapters use different reference contracts. The hub may point thin wrappers back to `skills/`, while project-local governance checks must continue to validate adapters against `.codex/skills/` in distributed consumer repositories.
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
- Documentation was split into `docs/ai`, `docs/human`, and `docs/bridge` because protocol, explanation, and handoff/exchange assets serve different audiences and should not compete for ownership in the same file.
- Bridge-reference cleanup remains audit-first because the current explicit docs/bridge/* hits are documentation-facing; path switches should happen deliberately and only where the active source is clearer than the bridge-facing copy.
- Adapter governance remains project-local by design because the distribution contract in consumer repositories is `.codex/skills` -> `.agents/.github`, while the hub itself still uses thin wrappers that point back to canonical `skills/`.
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
- No hub-aware mode in `check_adapter_consistency.py`; running it at the hub root still produces consumer-project mismatch findings by design rather than a hub-health report.
- No explicit router bias that guarantees `system-takeover` wins over generic `project-takeover` when the task wording mixes system intent with broad takeover language.
- No completed path-switch plan for the remaining direct bridge-facing compatibility link in AI_USAGE.md; that reference still needs a deliberate decision before any bridge copy cleanup.

These gaps are intentional to keep the system legible while distribution and governance semantics are still being stabilized.

## Next Phase Direction

The next phase should move the system from `controlled local governance` toward `controlled enforcement`, while preserving the current single-source layering model, the thin-wrapper system invocation model, the explicit documentation ownership split, and the new preflight-before-rollout boundary.

Directionally, this means strengthening confidence in cross-layer consistency, separating hub-health validation from consumer-project adapter validation, making orchestration behavior less heuristic, and increasing repeatability without giving up the current hard boundaries around canonical ownership, read-only governance transitions, preflight-only audit semantics, bridge-as-mirror documentation semantics, navigation-only bridge references, and wrapper-only system invocation surfaces.

The objective is not to add more surfaces or a controller framework, but to make the existing layers more trustworthy, more enforceable, and easier for future maintainers or AI agents to operate without ambiguity.

## System Takeover Snapshot (2026-04-02)

### System Structure

- Canonical source: `skills/` remains the only authoritative layer for skill content and execution contracts.
- Invocation protocol: `docs/ai/` now explicitly owns execution, invocation, and discovery rules for AI agents.
- Discovery adapters: `.agents/skills/` and `.github/skills/` expose thin entrypoints back to canonical skills for multi-AI discoverability.
- Orchestration helpers: `tools/skill_router.py` and `tools/skill_pipeline.py` provide lightweight routing and sequencing based on metadata, aliases, and heuristic follow-up rules.
- Distribution and maintenance tools: sync, bundle, metadata, governance check, and re-seed audit tools sit in `tools/`.
- Governance and regression evidence: repository tests cover structure, routing, sync DryRun semantics, adapter consistency smoke, and re-seed audit behavior.
- Human/bridge surfaces: `docs/human/` explains the repository to maintainers, while `docs/bridge/` mirrors key exchange assets without taking ownership from the active sources.

### Capability Map

- `template`: `chatgpt-handoff-pilot`
- `audit`: `documentation-governance`, `file-structure-check`
- `project`: `financial-data-project-migration`, `project-takeover`, `update-project-status`
- `governance`: `skill-governance`
- `system`: `system-handoff`, `system-status-update`, `system-takeover`

The current map is strong on takeover, status, documentation, structure, and distribution-governance workflows. It is still comparatively thin on deterministic orchestration, CI-backed enforcement, and hub-specific governance diagnostics.

### Maturity Assessment

- Capability Map: `stable-to-evolving`. The hub has ten named skills with clear categories and system wrappers, and the canonical/adaptor split is deliberate.
- Invocation Readiness: `stable`. Explicit AI-facing protocol docs and thin wrapper entrypoints make invocation rules legible and reusable.
- Routing Layer: `evolving`. A direct runtime check on `请使用system-takeover接管该项目` still selected `project-takeover`, which shows system-intent matching is not yet robust enough.
- Pipeline Layer: `evolving`. Sequencing exists and can attach follow-up skills, but it remains a lightweight ordered helper rather than a dependency-aware orchestration engine.
- Adapter Layer: `stable` for discoverability, `context-sensitive` for governance. Hub wrappers correctly point to canonical `skills/`, while consumer-project governance expects `.codex/skills` references.
- Tooling / Governance: `evolving`. The toolchain is broad and repeatable, but governance remains local and read-only rather than CI-enforced or hub-aware by default.
- Documentation / Handoff: `stable-to-evolving`. Ownership is much clearer after the AI/Human/Bridge split, but bridge continuity still depends on disciplined manual upkeep.

### Top Bottlenecks

- System-skill routing is underweighted. Explicit `system-takeover` intent can still collapse into generic `project-takeover`.
- Governance tooling is split by context but not yet explicit in interface. The same repository can look healthy as a hub and unhealthy under consumer-project adapter rules unless the operator already knows the difference.
- Validation is still mostly local. `pytest` was not available in the current interpreter, and the system still relies heavily on local scripts and human context rather than enforced repository-level checks.
- Direct bridge-facing compatibility links still exist. The clearest current example is AI_USAGE.md -> docs/bridge/SKILLS_INDEX.md, which is navigation-only today but would need a coordinated update before any bridge copy cleanup.

### Evolution Plan

- Add a hub-aware governance mode or a separate hub-health checker so hub-local wrappers and project-local adapters are not assessed through the same reference contract.
- Strengthen router aliases, trigger weighting, or explicit-name matching so system wrappers win when the task explicitly names them.
- Switch or preserve remaining direct bridge-facing compatibility links intentionally instead of treating bridge copy cleanup as a blind documentation move.
- Promote the most important routing, governance, and documentation ownership checks into a standard repeatable validation path, ideally without turning the system into an auto-mutating controller.

