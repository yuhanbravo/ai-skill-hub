# Skill Hub Status

- Updated at: `2026-04-24`
- Scope: `ai-skill-hub`
- Method: `system-status-update` wrapper over `update-project-status`
- Config: `.codex/skill-config/update-project-status.json`
- Data sources: Git history, working tree, `skills/`, `.agents/`, `.github/`, `tools/`, `docs/status/`

## Layer Status

### Canonical Skill Layer (`skills/`)

- Status: `stable`
- `skills/` remains the sole canonical source, and that ownership did not change when the repository completed one bounded real-repo implementation pilot.
- The `workflow-bootstrap` line now has evidence across a bounded `Phase 1 -> Phase 2 -> Phase 3A -> Phase 3B -> Phase 3C -> Phase 3D` track: Phase 1 established the workflow shell, Phase 2 added thin-entry drafts, Phase 3A added template sketches, Phase 3B validated one abstract consumer-repo profile, Phase 3C completed a real single consumer repo implementation pilot in the current repository, and Phase 3D added canonical path calibration over that same single-repo pilot outcome.
- The Phase 3C result confirms that the v1 entrypoint pair can move from canonical sketching into minimal real-repo implementation: `AGENTS.md` can act as the thin project-side master entrypoint, `.github/copilot-instructions.md` can remain a Copilot-specific thin adapter, and concrete canonical backreference paths can be expressed without host-specific assumptions.
- The new Phase 3D calibration assets then narrow one previously open question: in the current repo, `<project-local-canonical-skill-path>` should not be hard-materialized because no distinct project-local canonical payload artifact exists yet, and a controlled placeholder is therefore more stable than a pseudo-real path.
- The same calibration pass also tightens `AGENTS.md` and `.github/copilot-instructions.md` onto that controlled-placeholder route, making the path / backreference model clearer without adding a larger local runtime surface.
- This implementation-plus-calibration evidence strengthens the canonical model without changing canonical ownership: the project-side files remain thin entrypoints, the calibration assets remain single-repo follow-up material, and none of this authorizes rollout, distribution, or multi-repo adoption.

### Distribution Layer (`.agents/` / `.github/` / bridge-facing continuity)

- Status: `evolving`
- `.agents/skills/` and `.github/skills/` continue to act as discoverability-only derivative surfaces; the Phase 3D calibration did not change their contract, did not refresh flat summaries, and did not promote them into authoring surfaces.
- One bounded project-side entrypoint pair still exists in the current repository as real implementation evidence, and the new calibration only narrows its path-expression behavior; it does not expand the distribution layer.
- `SKILLS_INDEX.md` and `skills_index.json` remain intentionally untouched in this pass, so the distribution surface did not widen just because `workflow-bootstrap` advanced from sketch validation to single-repo implementation validation.
- No `.github/instructions/*.instructions.md` or `.github/agents/*.agent.md` files were added in this pass, so the project-side surface area remains intentionally constrained to the existing entrypoint pair.
- Bridge-facing continuity for status / handoff remains maintained through active-source documents rather than by promoting mirrors into ownership surfaces.
- The distribution boundary therefore stays unchanged: canonical assets can mature, one real pilot can land locally, and that pilot can receive bounded calibration, while rollout / distribution / adoption remains outside the scope of this phase.

### Governance Layer

- Status: `evolving`
- Governance remains read-only and boundary-oriented: adapter consistency, derivative-surface drift auditing, commit-convention validation, and document-role coordination continue to provide visibility without auto-fix or auto-sync behavior.
- The new Phase 3D evidence strengthens governance clarity at the path-policy level rather than governance power. Its execution report explicitly records that the round did not materialize `<project-local-canonical-skill-path>`, chose a controlled-placeholder strategy because no distinct project-local canonical payload artifact exists, and still did not enter rollout or distribution.
- This preserves a useful governance distinction: the repository can now say not only that the thin-entrypoint / thin-adapter split works in one real repo, but also that pseudo-real path filling is not automatically preferable to a controlled unresolved slot.
- No governance scripts, sync/export/import behavior, or adapter-check contracts changed in this pass.

### Tooling Layer (`tools/`)

- Status: `evolving`
- The tooling layer still covers status refresh, routing, sequencing, metadata generation, sync/import/export, local checks, adapter consistency, re-seed audit, and derivative-surface audit; these remain the repeatable operational surfaces for the hub.
- Phase 3D did not expand tooling responsibilities. No runtime-pack generator was introduced, no controller/orchestration framework was added, and no sync/export/import/check tool logic was changed in order to support this calibration.
- `update-project-status` remains the canonical status engine, and `system-status-update` still acts only as the system-oriented framing layer over that engine.
- Tooling therefore remains strong enough to support documentation refresh and local maintenance, but it still stops short of enforced distribution, rollout readiness, or generalized runtime-pack implementation.

## Current Phase

- Current phase: `Phase 3 - Controlled System`
- Workflow-bootstrap track position: `Phase 3D` canonical path calibration over a single consumer repo pilot
- Phase judgment: the system phase remains unchanged because the latest progress narrows path expression inside the same bounded real-repo pilot rather than adding broader distribution, rollout, adoption, or toolchain maturity. The repository now has stronger evidence that the v1 entrypoint pair, forced canonical-backreference model, and controlled-placeholder path strategy hold in one real consumer repo context, but that evidence is still intentionally narrow.
- Why unchanged: recent commits added only path-calibration documents plus minimal wording calibration in the existing entrypoint pair; they did not start multi-repo rollout, distribution, adoption, or tooling/governance enforcement upgrades.
- Main direction: do not jump directly to rollout-readiness. Re-evaluate later only if the repo gains a distinct maintainer-confirmed project-local canonical payload artifact or if the system decides to validate a second consumer-repo type.

## Capabilities

- Layered capability system: canonical skills, derivative discovery surfaces, governance checks, tooling, and active-source docs remain clearly separated instead of collapsing into one mutable layer.
- Minimal canonical workflow expression: the hub still provides a stable canonical `Copilot 主控 / Codex 施工` workflow shell and keeps role-split guidance at the workflow layer rather than scattering it across adapters.
- Workflow-shell coordination: `workflow-bootstrap` continues to clarify the workflow shell while `chatgpt-handoff-pilot` remains the protocol layer for task package, bounded execution, and execution report.
- Canonical-to-runtime-pack mapping: the repository now holds a six-step progression from workflow shell to thin-entry drafts to template sketches to pilot-validation sketches to one bounded single consumer repo implementation pilot to a bounded canonical path calibration pass over that pilot.
- Thin-entry draft set (Phase 2): `AGENTS.md` as thin master entrypoint, `.github/copilot-instructions.md` as Copilot-specific thin adapter, and canonical backreference rules remain the baseline entrypoint design.
- Template sketch set (Phase 3A): `workflow-bootstrap` still carries the v1 `required / optional / not recommended` template logic, fixed-vs-project-fill split for `AGENTS.md`, and thin-adapter boundary for `.github/copilot-instructions.md`.
- Pilot validation sketch set (Phase 3B): the hub can validate one abstract single-consumer-repo profile, confirm the v1 entrypoint pair is sufficient for that profile, keep field / placeholder mapping contained without unnecessary document split, and express a future file layout without claiming implementation.
- Single consumer repo implementation pilot (Phase 3C): the hub can now demonstrate in one real repository that `AGENTS.md` can serve as the thin master entrypoint, `.github/copilot-instructions.md` can remain a thin Copilot-specific adapter, concrete canonical guidance paths can be enforced, and the fixed / project-fill / placeholder model can survive contact with an actual repo layout.
- Canonical path calibration (Phase 3D): the hub can now compare placeholder strategies against real repo state, conclude that controlled placeholder is more stable than a pseudo-real path when no distinct project-local canonical payload artifact exists, and minimally tighten backreference wording without expanding the runtime surface.
- Anti-second-rulebook execution evidence: the repository now has implementation-level evidence that forced canonical backreferences and anti-expansion constraints can remain intact in a real repo rather than only in drafts or sketches.
- Controlled-placeholder execution evidence: the repository now has implementation-level evidence that unresolved project-local path slots can be made more precise and less drift-prone through maintainer-gated wording rather than premature materialization.
- Workspace-aware status refresh: `update-project-status` still supports `git`, `workspace`, and `hybrid` evidence collection while preserving a single canonical status engine.
- Derivative-surface auditing: the system can continue to inspect bridge / metadata drift without promoting those derivative surfaces into active-source ownership.
- Invocation metadata resilience: metadata extraction and discovery surfaces remain robust to current example-file layouts and wrapper discovery needs.
- Bridge continuity: handoff/status continuity copies remain conceptually supported while active ownership stays in `docs/HANDOFF.md` and `docs/status/skill-hub-status.md`.
- Local-first validation: local scripts remain the main maintenance and validation entrypoints, even though CI-backed enforcement is still absent.
- Wrapper coordination baseline: `system-status-update` and `system-handoff` still coordinate through freshness checking, status-first ordering, and phase-consistency validation without becoming an orchestration layer.

## Stability

- Overall maturity: `evolving`
- Stable: canonical ownership, wrapper-only system skills, active-source documentation ownership, thin-entry / thin-adapter boundary discipline, and the explicit distinction between completed single-repo pilot work plus calibration and still-unstarted rollout / distribution / adoption.
- Evolving: distribution freshness, derivative-surface governance, workspace-aware status-refresh ergonomics, metadata/discovery robustness, and the question of whether any future move beyond the current controlled-placeholder strategy is warranted.
- Not yet stable: CI-backed enforcement, automatic mirror consistency, automatic governance-mode detection, deterministic orchestration, multi-repo rollout readiness, distribution readiness, adoption readiness, broader consumer-repo-type fit, a distinct project-local canonical payload model across repo types, and unvalidated project-side file families such as `.github/instructions/*.instructions.md` and `.github/agents/*.agent.md`.
- Evidence boundary: this refresh is based on the current working tree, recent Git history, `skills/workflow-bootstrap/SKILL.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `skills/workflow-bootstrap/project_side_canonical_path_calibration_memo.md`, `skills/workflow-bootstrap/project_side_canonical_path_option_comparison_sketch.md`, and `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_execution_report.md`; no adapter/index/tooling changes were observed in the same pass.
- Freshness gate: `Updated at` satisfies the `14`-day freshness gate with current age `0` days, so no `Staleness` risk is added in this refresh.

## Recommended Next Steps

- Do not move directly into rollout-readiness or distribution-readiness from Phase 3D calibration.
- Re-evaluate only if the repository later gains a distinct maintainer-confirmed project-local canonical payload artifact, or if the system decides to validate a second consumer-repo type under bounded conditions.
- If one of those triggers occurs, define narrow gates first: what repo types are in scope, what still counts as thin `AGENTS.md` plus thin `.github/copilot-instructions.md`, and what would disqualify broader rollout.
- Keep `.github/instructions/*.instructions.md` and `.github/agents/*.agent.md` outside default scope unless a later bounded phase proves they are necessary.
- Continue to preserve forced canonical backreferences, `AGENTS.md`-first entry, controlled-placeholder discipline, and anti-second-rulebook checks while rollout, distribution, and multi-repo adoption remain explicitly out of scope.
