# HANDOFF

> Status: semantic mirror of active source [../HANDOFF.md](../HANDOFF.md)
>
> Ownership: active updates continue in `docs/HANDOFF.md`
>
> Purpose: bridge-facing handoff continuity for AI and human maintainers without changing the active handoff path

> Bridge mirror notice:
> This file is a non-canonical bridge/mirror reference for compatibility or exchange workflows.
> Canonical source: `docs/HANDOFF.md`
> If this bridge copy conflicts with the canonical source, the canonical source wins.
> Do not treat this bridge copy as the current-state SSOT.

This file is the single source of truth for project handoff.

## Update Log

- 2026-03-30: Initialized the system handoff document for `ai-skill-hub` and captured the current phase, hard boundaries, design decisions, intentional gaps, and next-phase direction.
- 2026-03-31: Merged the current system-state refresh, selective rollout control, DryRun contract hardening, and system-wrapper invocation surfaces into the handoff brief without rewriting the document.
- 2026-04-01: Merged the new re-seed preflight audit capability and conservative hub self-detection into the system handoff, while preserving the existing phase model and wrapper-only boundaries.
- 2026-04-02: Merged a `system-takeover` pass into the handoff, capturing the explicit AI/Human/Bridge documentation split, the current system capability map, the router mismatch around `system-takeover`, and the hub-vs-consumer governance boundary.
- 2026-04-02: Refreshed the system status and merged the latest bridge-reference audit into the handoff, confirming that current bridge-layer references remained documentation-facing and identifying the direct compatibility link in AI_USAGE.md before this cleanup.
- 2026-04-02: Merged the repository-wide bridge audit result into the handoff, confirming that direct bridge-path dependency has now been cleared from active docs and that remaining bridge references are semantic, historical, or bridge-layer self-description rather than runtime dependency.
- 2026-04-03: Merged the landed commit-governance capability into the handoff, capturing `docs/governance/` as the repository-governance documentation home, the moved commit convention, the `skill-governance` validator asset, the versioned `.githooks/commit-msg` plus `tools/install_git_hooks.ps1` local activation path, the `export_bundle.ps1` auto-commit reuse of the same validator, and the current choice to observe real usage before tightening body rules further.
- 2026-04-07: Merged the explicit `system-takeover` routing fix, the new `hub|consumer` adapter-governance mode split, and the default local validation entrypoint `tools/run_local_checks.ps1` into the handoff without changing phase or hard boundaries.
- 2026-04-07: Merged the new human-oriented quick commands docs for `system-takeover` plus the lightweight cross-link from `SYSTEM_SKILL_QUICK_COMMANDS.md`, treating them as maintainer-facing documentation-surface additions rather than protocol, governance, or boundary changes.

## Current Status

`ai-skill-hub` is currently in `Phase 3 - Controlled System`.

The system has already moved beyond a simple skill repository and now operates as an AI capability system with six active layers:

- Canonical Skill Layer: `skills/` remains the stable canonical source for skill definitions and invocation contracts, now including system-level wrapper skills for status and handoff without forking canonical behavior.
- Invocation Layer: `docs/ai/EXECUTION_PROTOCOL.md`, `docs/ai/INVOCATION_PROTOCOL.md`, and `docs/ai/DISCOVERY_AND_INVOCATION.md` now hold the explicit AI-facing execution, invocation, and discovery contracts instead of leaving those rules implicit in mixed docs.
- Routing / Pipeline Layer: `tools/skill_router.py` and `tools/skill_pipeline.py` provide lightweight task-to-skill matching and ordered multi-skill sequencing, but they still behave as heuristic orchestration helpers rather than deterministic controllers.
- Distribution Layer: the system supports hub-side discovery surfaces and project-side runtime distribution through `.codex`, `.agents`, and `.github`, and rollout can now be scoped by target layer while preserving default behavior.
- Governance Layer: the system has a read-only adapter consistency check, a landed commit-message convention validator under `skill-governance`, and regression coverage for DryRun no-side-effect behavior, adapter reference correctness, rollout-target audit classification, and commit-message validation behavior.
- Documentation Layer: `docs/ai`, `docs/human`, `docs/governance`, and the bridge documentation layer now split protocol, explanation, repository-governance, and exchange assets into explicit ownership layers while keeping `docs/HANDOFF.md` and `docs/status/skill-hub-status.md` as active sources; `docs/governance/` is now the canonical home for repository-governance docs, `docs/governance/COMMIT_CONVENTION.md` has replaced the old human-layer path as the active commit-policy source, direct bridge-path dependency has been removed from active documentation, bridge semantics remain explicit for navigation and continuity, and `docs/human/` now also carries lightweight quick-command references for maintainers, including a standalone `SYSTEM_TAKEOVER_QUICK_COMMANDS.md` page plus a small cross-link from `SYSTEM_SKILL_QUICK_COMMANDS.md` without changing protocol ownership or system boundaries.
- Tooling Layer: sync, metadata, routing, pipeline, local governance tooling, a standalone re-seed preflight audit path, and a versioned local commit-hook installation path are available as repeatable operational capabilities; system invocation also has explicit wrapper entrypoints for status and handoff, and `export_bundle.ps1` now reuses the same commit-message validator as the local `commit-msg` hook.

Overall system maturity is `evolving`: the canonical and invocation layers are stable, documentation ownership is clearer, distribution and governance are increasingly controlled, routing/orchestration remain intentionally lightweight and still somewhat heuristic, and the current bridge-reference surface has now been audited as documentation-facing rather than runtime-facing. This round improves system trust without changing phase: explicit `system-takeover` requests now route correctly, adapter validation now distinguishes hub and consumer contracts explicitly, and local repository validation now has a default entrypoint through `tools/run_local_checks.ps1`.

## Hard Boundaries

- `skills/<skill>/` remains the only canonical source of truth inside the hub. No adapter layer may become a second authoritative source.
- `system-status-update` and `system-handoff` must remain wrapper skills. They may reuse canonical skills and add system-level output constraints, but they must not fork canonical logic.
- In distributed business-project contexts, `.codex/skills/` is the runtime SSOT for local skill content. Project-local adapters must point to `.codex/skills/`, not back to hub `skills/` paths.
- Governance at the current stage is read-only. Consistency checks may detect drift, but they must not auto-fix, auto-delete, or silently rewrite adapters.
- Re-seed auditing remains preflight-only. Audit tooling may classify rollout readiness and identify hub repositories, but it must not silently execute reseed, sync, delete, or project mutation.
- Adapter layers exist for discoverability, not authorship. `.agents/skills/` and `.github/skills/` must remain derivative surfaces.
- AI / Human / Bridge documentation ownership must stay explicit. `docs/ai/` owns execution-facing protocol, `docs/human/` owns explanation-oriented repository guidance, and the bridge layer remains a mirror/exchange layer rather than a new active source.
- Existing bridge-layer references may serve navigation, mirror, or exchange semantics, but they must not become script, config, or runtime activation dependencies.
- Hub-local adapter wrappers and project-local adapters use different reference contracts. The hub may point thin wrappers back to `skills/`, while project-local governance checks must continue to validate adapters against `.codex/skills/` in distributed consumer repositories.
- Sync-back semantics stay constrained to canonical content recovery. Project-local adapters are not treated as editable upstream sources.
- Selective rollout control may narrow where distribution lands, but it must not redefine canonical ownership or promote adapter layers into authoring surfaces.
- `ai-skill-hub` itself is not a normal clean re-seed target. Hub self-detection is allowed as a protective boundary so the system repository is not misclassified as a consumer project.
- System evolution must preserve layer clarity: canonical definition, distribution surfaces, governance checks, and orchestration tooling cannot be collapsed into a single mutable layer.
- Repository-governance docs now belong under `docs/governance/`; compatibility or historical paths must not be treated as the active commit-policy source.
- Local commit governance is versioned through `.githooks/` plus `tools/install_git_hooks.ps1`, not through checked-in `.git/hooks/` content; each clone or worktree must opt in locally once.

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
- Documentation was split into `docs/ai`, `docs/human`, and a bridge layer because protocol, explanation, and handoff/exchange assets serve different audiences and should not compete for ownership in the same file.
- Bridge-reference cleanup remains audit-first because the current explicit bridge-layer references are documentation-facing; path switches should happen deliberately and only where the active source is clearer than the bridge-facing copy.
- Repository-wide bridge auditing now distinguishes direct path dependency from bridge semantics, mirror ownership, and historical context so later cleanup can stay evidence-driven instead of trying to erase every bridge mention.
- Adapter governance remains project-local by design because the distribution contract in consumer repositories is `.codex/skills` -> `.agents/.github`, while the hub itself still uses thin wrappers that point back to canonical `skills/`.
- The system remains phase-based because capability maturity is uneven across layers; canonical definition is already stable, while governance enforcement and orchestration still need controlled progression.
- Repository-governance docs were split into `docs/governance/` because commit policy and similar cross-repository rules now deserve an explicit canonical home instead of remaining mixed into the human explanation layer.
- Local commit validation is installed via a versioned `.githooks/commit-msg` plus `tools/install_git_hooks.ps1` path because Git hook activation is clone-local by design; shipping the hook definition in-repo preserves consistency, while per-clone installation keeps the mechanism aligned with Git's local-hook model.
- `export_bundle.ps1` reuses the same validator as the local `commit-msg` hook because auto-commit paths should obey the same commit convention instead of creating a second commit-policy surface.

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
- No automatic mode detection in `check_adapter_consistency.py`; hub and consumer validation are now explicitly separated, but the operator still has to choose the correct mode.
- No attempt to make routing deterministic beyond the explicit-name/system-intent fix; `system-takeover` misrouting is corrected, but the router is still intentionally heuristic rather than controller-like.
- No broader bridge-path migration plan beyond the compatibility-entry cleanup completed in this pass; any further bridge copy cleanup should still be deliberate rather than automatic.
- No repository-level mirror consistency checker yet; bridge mirrors remain manually maintained even though current repo-wide auditing shows no runtime/config dependency on them.
- No automatic hook enablement across fresh clones or worktrees; `tools/install_git_hooks.ps1` must still be run locally once per clone/worktree.
- No decision yet to tighten commit body rules beyond the current lightweight descriptive check; that boundary should continue to follow real usage feedback rather than speculative policy growth.
- No CI-backed default validation flow yet; `tools/run_local_checks.ps1` is now the default local entrypoint, but it remains a local wrapper rather than repository-level enforcement.

These gaps are intentional to keep the system legible while distribution and governance semantics are still being stabilized.

## Next Phase Direction

The next phase should move the system from `controlled local governance` toward `controlled enforcement`, while preserving the current single-source layering model, the thin-wrapper system invocation model, the explicit documentation ownership split, and the new preflight-before-rollout boundary.

Directionally, this means strengthening confidence in cross-layer consistency, continuing to keep hub-health validation separate from consumer-project adapter validation, making orchestration behavior less heuristic without turning it into a controller framework, and increasing repeatability around the new default local validation entrypoint without giving up the current hard boundaries around canonical ownership, read-only governance transitions, preflight-only audit semantics, bridge-as-mirror documentation semantics, navigation-only bridge references, wrapper-only system invocation surfaces, and the current evidence that remaining bridge mentions are semantic rather than runtime-coupled.

The objective is not to add more surfaces or a controller framework, but to make the existing layers more trustworthy, more enforceable, and easier for future maintainers or AI agents to operate without ambiguity. In practical terms, the current direction is to keep the explicit routing fix, the dual governance contract, and the local validation entrypoint stable and well-understood before attempting any stronger enforcement layer.

## System Takeover Snapshot (2026-04-02)

### System Structure

- Canonical source: `skills/` remains the only authoritative layer for skill content and execution contracts.
- Invocation protocol: `docs/ai/` now explicitly owns execution, invocation, and discovery rules for AI agents.
- Discovery adapters: `.agents/skills/` and `.github/skills/` expose thin entrypoints back to canonical skills for multi-AI discoverability.
- Orchestration helpers: `tools/skill_router.py` and `tools/skill_pipeline.py` provide lightweight routing and sequencing based on metadata, aliases, and heuristic follow-up rules.
- Distribution and maintenance tools: sync, bundle, metadata, governance check, and re-seed audit tools sit in `tools/`.
- Governance and regression evidence: repository tests cover structure, routing, sync DryRun semantics, adapter consistency smoke, and re-seed audit behavior.
- Human/bridge surfaces: `docs/human/` explains the repository to maintainers, while the bridge layer mirrors key exchange assets without taking ownership from the active sources.

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
- Documentation / Handoff: `stable-to-evolving`. Ownership is much clearer after the AI/Human/Bridge split, and repo-wide auditing shows active docs no longer depend on bridge paths directly, but bridge continuity still depends on disciplined manual upkeep.

### Top Bottlenecks

- System-skill routing is underweighted. Explicit `system-takeover` intent can still collapse into generic `project-takeover`.
- Governance tooling is split by context but not yet explicit in interface. The same repository can look healthy as a hub and unhealthy under consumer-project adapter rules unless the operator already knows the difference.
- Validation is still mostly local. `pytest` was not available in the current interpreter, and the system still relies heavily on local scripts and human context rather than enforced repository-level checks.
- The compatibility entry in `AI_USAGE.md` now points to root `SKILLS_INDEX.md`, reducing bridge-path coupling while preserving the same navigation outcome.
- Remaining bridge references are mostly semantic or historical. That is lower risk than direct path dependency, but it also means future mirror shrink should happen through deliberate refreshes instead of cleanup-only rewrites.

### Evolution Plan

- Add a hub-aware governance mode or a separate hub-health checker so hub-local wrappers and project-local adapters are not assessed through the same reference contract.
- Strengthen router aliases, trigger weighting, or explicit-name matching so system wrappers win when the task explicitly names them.
- Continue to switch or preserve bridge-facing compatibility links intentionally instead of treating bridge copy cleanup as a blind documentation move.
- Promote the most important routing, governance, and documentation ownership checks into a standard repeatable validation path, ideally without turning the system into an auto-mutating controller.
