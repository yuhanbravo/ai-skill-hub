# HANDOFF

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
- 2026-04-20: Merged the workspace-aware status refresh upgrade, the new derivative-surface drift audit, invocation-metadata extraction hardening, bridge semantic mirror refresh, and the minimum coordination note between `documentation-governance` and `update-project-status` into the handoff while preserving `Phase 3 - Controlled System` and read-only governance boundaries.
- 2026-04-20: Applied minimal wrapper-coordination hardening for `system-status-update` and `system-handoff`; refreshed status first (`docs/status/skill-hub-status.md`, Updated at `2026-04-20`), then completed handoff merge with phase consistency check (`Phase 3 - Controlled System`) and recorded this status baseline.
- 2026-04-21: Merged the completed Phase 1 `workflow-bootstrap` canonical workflow asset into the handoff after refreshing status first (`docs/status/skill-hub-status.md`, Updated at `2026-04-21`); recorded the new minimal `Copilot-led / Codex-implemented` workflow-shell expression, kept `chatgpt-handoff-pilot` as the handoff protocol layer, preserved all existing hard boundaries, and noted that project-side runtime-pack decisions remain deferred to Phase 2.
- 2026-04-22: Merged Phase 2 `workflow-bootstrap` canonical drafts into system status/handoff context after refreshing status first (`docs/status/skill-hub-status.md`, Updated at `2026-04-22`): landed only thin-entry canonical drafts (`AGENTS.md` master-entry draft, `.github/copilot-instructions.md` Copilot-specific thin-adapter draft, and canonical backreference rules draft), preserved `Phase 3 - Controlled System`, and retained hard boundaries that real project-side runtime pack files are still not implemented and rollout has not started. Phase 2 含一次 bounded re-run，用于修正 cloud snapshot 缺少 task package 时的输入不完整问题；最终以当前 draft assets 与最新 execution report 为准。
- 2026-04-23: Refreshed system status first (`docs/status/skill-hub-status.md`, Updated at `2026-04-23`) and then merged the completed Phase 3A `workflow-bootstrap` canonical template sketches into handoff context. This update records that the repository has moved from Phase 2 thin-entry drafts to Phase 3A project-side runtime pack template sketch assets, while preserving `Phase 3 - Controlled System`, keeping all runtime-pack surfaces non-implemented, and explicitly distinguishing completed canonical sketch work from the still-not-started single consumer repo pilot implementation stage.
- 2026-04-23: Refreshed system status first (`docs/status/skill-hub-status.md`, Updated at `2026-04-23`) and then merged the completed Phase 3B `workflow-bootstrap` canonical pilot-validation sketches into handoff context. This update records that the repository has moved from Phase 3A template sketches to Phase 3B validation sketches for one abstract single consumer repo profile, while preserving `Phase 3 - Controlled System`, keeping all runtime-pack surfaces non-implemented, and explicitly stating that this round does not correspond to any selected real consumer repo.
- 2026-04-24: Refreshed system status first (`docs/status/skill-hub-status.md`, Updated at `2026-04-24`) and then merged the completed Phase 3C single consumer repo implementation pilot into handoff context. This update records that `ai-skill-hub` moved from Phase 3B pilot-validation sketching to a real single consumer repo implementation pilot in the current repository, landed the minimal `AGENTS.md` plus `.github/copilot-instructions.md` entrypoint pair, validated concrete canonical backreference paths plus anti-second-rulebook behavior, and still did not start rollout, distribution, adoption, or toolchain expansion.
- 2026-04-24: Refreshed system status first (`docs/status/skill-hub-status.md`, Updated at `2026-04-24`) and then merged the completed Phase 3D canonical path calibration into handoff context. This update records that the repository kept the existing single-repo entrypoint pair but added bounded calibration assets, concluded that `<project-local-canonical-skill-path>` should remain a controlled placeholder rather than be hard-materialized in the current repo, applied only minimal backreference wording tightening to `AGENTS.md` and `.github/copilot-instructions.md`, and still did not start rollout, distribution, adoption, tooling changes, or project-side surface expansion.

## Current Status

`ai-skill-hub` is currently in `Phase 3 - Controlled System`.

The repository continues to operate as a layered AI capability system rather than a normal business-project codebase. `skills/` remains the stable canonical source, `.agents/skills/` and `.github/skills/` remain derivative discoverability surfaces, governance and tooling remain read-only / local-first, and `docs/HANDOFF.md` plus `docs/status/skill-hub-status.md` remain the active-source coordination documents for system state.

The `workflow-bootstrap` line has now advanced one bounded step further without changing system phase. Phase 1 established the canonical workflow shell for the default `Copilot 主控 / Codex 施工` chain; Phase 2 added thin-entry canonical drafts; Phase 3A added project-side runtime-pack template sketches; Phase 3B added canonical pilot-validation sketches for one abstract single consumer repo profile; Phase 3C completed a real single consumer repo implementation pilot in the current repository; and Phase 3D completed canonical path calibration over that same single-repo pilot. `chatgpt-handoff-pilot` remains the protocol layer for `task package`, `bounded execution`, and `execution report`, so `workflow-bootstrap` still clarifies workflow shape without replacing the repository's handoff contract.

The new Phase 3D work does not expand the runtime surface further; instead it closes a path-expression question that remained open after the real pilot. In the current repo, the repository now has an explicit bounded conclusion that `<project-local-canonical-skill-path>` should not be hard-materialized because no distinct project-local canonical payload artifact exists yet, and that a controlled placeholder is therefore more stable than a pseudo-real path in this repo state.

This adds path-level implementation evidence while preserving all core boundaries. The Phase 3D result shows that `AGENTS.md` and `.github/copilot-instructions.md` can be minimally tightened around a controlled-placeholder rule, that canonical guidance still wins on conflict, and that the project-side pair can remain thin without inventing a fake local canonical payload path. At the same time, this remains only a single consumer repo pilot plus calibration result: it does not authorize multi-repo rollout, distribution, adoption, toolchain retrofit, or any claim that a general template has already been finalized. The system therefore remains in `Phase 3 - Controlled System` with overall maturity still `evolving`.

## Hard Boundaries

- `skills/<skill>/` remains the only canonical source of truth inside the hub. No adapter layer may become a second authoritative source.
- `system-status-update` and `system-handoff` must remain wrapper skills. They may reuse canonical skills and add system-level output constraints, but they must not fork canonical logic.
- Workspace-aware or no-git status refresh extends evidence collection only. It must not promote workspace signals, bridge copies, readable derivatives, or other convenience surfaces into new authoritative system sources.
- `system-status-update` and `system-handoff` coordination must remain minimal: refresh status first, then merge handoff; keep a `14`-day freshness gate and phase consistency check, but do not introduce auto-trigger orchestration.
- In distributed business-project contexts, `.codex/skills/` is the runtime SSOT for local skill content. Project-local adapters must point to `.codex/skills/`, not back to hub `skills/` paths.
- `workflow-bootstrap` Phase 3D evidence is still limited to one real single consumer repo pilot plus bounded calibration. It may validate the thin `AGENTS.md` plus `.github/copilot-instructions.md` entrypoint pair, forced canonical backreferences, and controlled-placeholder path handling in one bounded repo context, but it must not be presented as multi-repo rollout, distribution readiness, or authorization to expand the project-side file family by default.
- Governance at the current stage is read-only. Consistency checks may detect drift, but they must not auto-fix, auto-delete, or silently rewrite adapters.
- Derivative-surface auditing and documentation-status coordination remain advisory/read-only. They may clarify drift, ownership, or operating order, but they must not auto-remediate, auto-sync, or redefine canonical skill contracts.
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
- Workspace-aware/no-git refresh was added inside canonical `update-project-status` because status generation needed graceful degradation when Git is unavailable, but the repository still needed one canonical status engine rather than a parallel workspace-only wrapper path.
- Project distribution keeps `.codex/skills/` as the local runtime SSOT because business projects need a stable local skill-content root without becoming a second canonical hub.
- Project-local `.agents/.github` adapters are generated around `.codex/skills/` instead of copied from the hub because copied hub adapters would carry broken references and violate project-local path correctness.
- Governance starts with read-only drift detection because the current system priority is visibility and boundary control, not automatic mutation or destructive cleanup.
- Derivative-surface auditing was introduced as a read-only tool because bridge and metadata drift need visibility before the repository decides whether any stronger enforcement or sync policy is justified.
- Selective rollout was added at the sync layer because distribution control was needed, but the default path was preserved to avoid creating a second distribution policy surface.
- Re-seed readiness was added as a separate audit tool instead of being folded into the sync path because rollout preflight needs a read-only decision surface, not a hidden execution side effect.
- Hub self-detection stays conservative because boundary protection matters more than aggressive classification; it is better to miss some hubs than to misclassify ordinary projects as system repositories.
- Documentation was split into `docs/ai`, `docs/human`, and a bridge layer because protocol, explanation, and handoff/exchange assets serve different audiences and should not compete for ownership in the same file.
- Documentation-status coordination was documented as a minimum governance note because `documentation-governance` and `update-project-status` now intersect on artifact roles, but that intersection should clarify lanes rather than introduce a pipeline or controller layer.
- Bridge-reference cleanup remains audit-first because the current explicit bridge-layer references are documentation-facing; path switches should happen deliberately and only where the active source is clearer than the bridge-facing copy.
- Repository-wide bridge auditing now distinguishes direct path dependency from bridge semantics, mirror ownership, and historical context so later cleanup can stay evidence-driven instead of trying to erase every bridge mention.
- Adapter governance remains project-local by design because the distribution contract in consumer repositories is `.codex/skills` -> `.agents/.github`, while the hub itself still uses thin wrappers that point back to canonical `skills/`.
- The system remains phase-based because capability maturity is uneven across layers; canonical definition is already stable, while governance enforcement and orchestration still need controlled progression.
- For Phase 2 runtime-pack entry planning, canonical guidance now treats `AGENTS.md` as the preferred thinnest project-side primary-entry draft and `.github/copilot-instructions.md` as a Copilot-specific thin adapter draft, with explicit canonical-backreference/no-second-rulebook constraints kept at draft level only.
- A single-profile validation sketch was added before any real implementation pilot because the repository needed one more bounded check that the thin entrypoint pair and placeholder/backreference model remain workable in a plausible consumer-repo shape without prematurely binding to a real target repository.
- Phase 3B kept field / placeholder mapping inside the main pilot validation sketch because the current design was still readable in one document; avoiding an extra split helps preserve the anti-second-rulebook goal even at sketch level.
- Repository-governance docs were split into `docs/governance/` because commit policy and similar cross-repository rules now deserve an explicit canonical home instead of remaining mixed into the human explanation layer.
- Local commit validation is installed via a versioned `.githooks/commit-msg` plus `tools/install_git_hooks.ps1` path because Git hook activation is clone-local by design; shipping the hook definition in-repo preserves consistency, while per-clone installation keeps the mechanism aligned with Git's local-hook model.
- `export_bundle.ps1` reuses the same validator as the local `commit-msg` hook because auto-commit paths should obey the same commit convention instead of creating a second commit-policy surface.

## Intentional Gaps

- No auto-fix for adapter drift.
- No CI-backed enforcement for adapter consistency yet.
- No expansion of governance into destructive sync, delete, or rewrite behavior.
- No orchestration or controller layer around `system-status-update` and `system-handoff`.
- No auto-remediation path for derivative-surface drift; the new audit remains inspect-first and read-only.
- No auto-reseed or auto-remediation path inside the re-seed audit tool.
- No aggressive hub fingerprinting beyond a conservative strong-signal guard.
- No redesign of metadata generation or adapter schema in this phase.
- No promotion of project-local adapters into upstream authoring surfaces.
- No attempt to turn heuristic routing and sequencing into a fully deterministic orchestration stack in the current phase.
- No automatic mode detection in `check_adapter_consistency.py`; hub and consumer validation are now explicitly separated, but the operator still has to choose the correct mode.
- No attempt to make routing deterministic beyond the explicit-name/system-intent fix; `system-takeover` misrouting is corrected, but the router is still intentionally heuristic rather than controller-like.
- No broader bridge-path migration plan beyond the compatibility-entry cleanup completed in this pass; any further bridge copy cleanup should still be deliberate rather than automatic.
- No repository-level mirror consistency checker yet; bridge mirrors remain manually maintained even though current repo-wide auditing shows no runtime/config dependency on them.
- No enforced runtime schema or automation layer for documentation-status coordination; the current note is guidance for operators, not a new system controller.
- No automatic hook enablement across fresh clones or worktrees; `tools/install_git_hooks.ps1` must still be run locally once per clone/worktree.
- No decision yet to tighten commit body rules beyond the current lightweight descriptive check; that boundary should continue to follow real usage feedback rather than speculative policy growth.
- No CI-backed default validation flow yet; `tools/run_local_checks.ps1` is now the default local entrypoint, but it remains a local wrapper rather than repository-level enforcement.
- No claim that the completed Phase 3C single consumer repo pilot is ready for direct multi-repo copying, template broadcast, or broad consumer-repo adoption.
- No broader project-side runtime-pack family rollout beyond the bounded `AGENTS.md` plus `.github/copilot-instructions.md` pair in one real repo; `.github/instructions/*.instructions.md` and `.github/agents/*.agent.md` remain unimplemented and out of default scope.
- No distinct project-local canonical payload artifact exists yet in the current repo; the controlled placeholder remains intentionally unresolved until a maintainer-confirmed artifact actually appears.
- No broader project-side enforced backlink contract beyond this one bounded pilot plus calibration; the concrete path-backreference and controlled-placeholder behavior is now implemented and validated in one real repo, but not yet generalized across additional repo types.
- No validation yet across multiple consumer repo types; the current implementation evidence comes from one real repo only, so layout diversity and portability remain unproven.
- No rollout-readiness, distribution-readiness, or adoption gate has been defined from the Phase 3C plus Phase 3D result; that decision remains future governance work rather than an automatic consequence of this pilot and calibration.
- No refresh of `skills_index.json` in this workflow-bootstrap pass; that deferral is intentional because the current generation chain would also rewrite `.agents/skills/*.md` flat summaries and widen the bounded-execution scope.
- No expansion of local validation and check tooling into an automated distribution, rollout, or execution framework; the repository still treats those tools as repeatable local support surfaces rather than a stronger controller layer.
- No distribution / rollout / adoption step has started for the future project-side runtime pack; Phase 3D completed only bounded single-repo follow-up calibration and intentionally stopped before broader propagation.

These gaps are intentional to keep the system legible while distribution and governance semantics are still being stabilized.

## Next Phase Direction

The next phase should still move the system from `controlled local governance` toward `controlled enforcement`, but the workflow-bootstrap track now has a narrower immediate direction than before: do not jump directly into rollout-readiness after Phase 3D calibration, and instead treat any next move as condition-triggered rather than automatic.

Directionally, this means waiting for one of two concrete triggers before reassessing the path strategy: either the current repo gains a distinct and maintainer-confirmed project-local canonical payload artifact, or the system decides to validate a second consumer repo type under bounded conditions. Only then should the repository revisit whether the controlled placeholder remains correct and whether a new bounded follow-up phase is justified.

In other words, the system should now treat `workflow-bootstrap` as canonical workflow-shell guidance plus Phase 2 thin-entry drafts plus Phase 3A template sketches plus Phase 3B validation sketches plus one completed Phase 3C implementation pilot plus Phase 3D calibration, while still preserving the hard boundary that rollout / distribution / adoption has not started. The next directional step, if any, should be another small condition-triggered follow-up rather than direct multi-repo expansion or broader proliferation across `.github/instructions/*.instructions.md` or `.github/agents/*.agent.md`.

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
