# Workflow Bootstrap Non-Git Project-Side Pilot Review

## 1. Executive Summary

The Derivative_Data pilot validates the main workflow-bootstrap assumptions for a non-git / low-git project-side trial.

- It validated the `Copilot planner / Codex bounded implementer` mode: task packages framed scope and acceptance, while Codex executed narrowly and returned execution reports.
- It validated `tasks/` as the primary non-git per-task trace path. Later rounds used paired task package and execution report artifacts under `tasks/`, and `tasks/README.md` now acts as a lightweight navigation index.
- It validated the execution report as the primary per-task evidence trail when Git history, branches, PRs, or diffs are not reliable evidence sources.
- It validated minimal closure for handoff/status surfaces: `docs/HANDOFF.md` and status-like surfaces did not become per-task trace logs.
- It validated a project-side split where `AGENTS.md` is the master thin entry and `.github/copilot-instructions.md` is a Copilot-specific thin adapter. The zh-CN adapter was later synchronized as a translated mirror, not promoted into a separate rule source.
- It is suitable for conservative backport review into workflow-bootstrap, but only as generalized workflow-shell and runtime-profile guidance. Derivative_Data project facts must remain local.

Target hub observation: in `ai-skill-hub`, `skills/workflow-bootstrap/non_git_runtime_profile.md` and `skills/workflow-bootstrap/examples/invocation_examples.md` were missing at review time. This memo records them as possible future absorption targets only; it does not create or modify canonical skill files.

## 2. Original Pilot Goal

The original goal was a second non-git workflow trial, not a larger or harder implementation task.

The intended focus was to tighten the landing relationship among task package, execution report, handoff, and status. The pilot was meant to test whether Copilot could prepare a bounded task package, whether Codex could execute only that package, and whether the execution report could carry the local evidence that Git would normally provide.

The pilot also tested whether cross-round project docs could stay lightweight: task-level detail belongs in `tasks/`, while handoff/status surfaces receive only the smallest useful closure facts.

## 3. Actual Execution Chain

- Workflow-bootstrap P0 repair: added a project-local non-git / low-git runtime profile to the pilot copy of workflow-bootstrap, clarified protocol ownership, and reinforced that chatgpt-handoff-pilot owns task package, bounded execution, and execution report protocol.
- Non-git runtime profile: defined task package and execution report pairing under `tasks/`, execution report as primary evidence, minimal handoff/status closure, and archive as inactive history.
- Invocation examples: added examples for reviewing project-side runtime packs, preparing non-git runtime conventions, and framing a non-git handoff to chatgpt-handoff-pilot.
- Workflow artifact navigation: updated `docs/README.md` with short navigation guidance pointing to `tasks/`, `docs/HANDOFF.md`, optional status, and archive boundaries.
- Step 5 review: confirmed the repaired workflow-bootstrap supported small non-git bounded tasks and recommended a read-only readiness review before project-side thin-entry migration.
- Project-side thin-entry readiness review: inventoried `AGENTS.md`, `.github/copilot-instructions.md`, absent `.github/instructions/`, absent `.github/agents/`, and confirmed readiness for a narrow first cut.
- `AGENTS.md` master thin entry first cut: made `AGENTS.md` the project-side master entry, with required backreferences, conflict precedence, no-second-rulebook wording, and non-git evidence convention.
- `.github/copilot-instructions.md` thin adapter first cut: reduced the Copilot file to a Copilot-specific adapter that points first to `AGENTS.md`, keeps high-frequency runtime constraints, and preserves runtime-pack boundaries.
- `.github/copilot-instructions.zh-CN.md` translated mirror sync: aligned the Chinese copy to the English thin adapter without making it a second source of truth.
- `tasks/README.md` index: added a lightweight task artifact index and recorded missing or non-exact historical pairs honestly instead of backfilling them.

## 4. What Worked

- `tasks/` worked as the primary per-task trace path.
- Task package / execution report pairing made bounded work easier to audit in a non-git workspace.
- Execution reports successfully replaced part of the evidence role normally served by commits, PRs, or diffs.
- Handoff/status surfaces did not steal the main evidence line.
- Archive remained historical or inactive, not the active workflow line.
- `AGENTS.md` worked as a project-side master entry when kept thin and backreference-oriented.
- Copilot instructions worked better as a thin adapter than as a duplicate repository rulebook.
- The zh-CN adapter worked as a translated mirror with the same semantic boundary as the English adapter.
- `tasks/README.md` provided a useful lightweight index without replacing task packages, execution reports, canonical skills, or project docs.

## 5. What Expanded Beyond the Initial Goal

The pilot expanded slightly from a pure non-git workflow-path trial into a project-side runtime-entry pilot.

That expansion was reasonable because the non-git evidence convention needed a clear place to be discovered by agents. Once task/report pairing, minimal handoff closure, and archive boundaries were working, the next natural question was whether a project-side `AGENTS.md` and Copilot adapter could expose those rules without copying the full canonical workflow or handoff protocol.

The expansion stayed bounded because it proceeded through read-only review, then one file at a time, with execution reports after each step. It did not create `.github/instructions/`, `.github/agents/`, validators, automation, CI, hooks, or broader runtime-pack machinery.

Those deferred surfaces should remain deferred. The pilot does not prove that every project needs topic-specific GitHub instructions, role-specific agent files, validators, automation, or CI enforcement.

## 6. Candidate Backport Items for ai-skill-hub

### Strong candidates

- Non-git / low-git runtime profile as a workflow-bootstrap supporting asset.
- `tasks/` primary trace convention for projects without reliable Git evidence.
- Task package / execution report pairing with shared date and task-name prefix.
- Execution report as the primary per-task evidence trail in non-git / low-git contexts.
- Handoff/status minimal closure guidance.
- Archive as optional historical or inactive material, not the active workflow line.
- Project-side master entry vs Copilot thin adapter split.
- Explicit boundary that workflow-bootstrap frames the workflow shell while chatgpt-handoff-pilot owns task package, bounded execution, and execution report protocol.

### Review candidates

- Translated adapter mirror guidance for multilingual projects, kept as optional guidance rather than a universal requirement.
- `tasks/README.md` or task registry as an optional navigation layer once task artifacts accumulate.
- Invocation examples for framing workflow-bootstrap work before handing actual task-package protocol to chatgpt-handoff-pilot.
- Read-only readiness review before changing project-side runtime entries.
- Guidance for recording missing or non-exact historical task/report pairs without backfilling them.

### Project-local only

- Any Derivative_Data environment, interpreter, CLI, probe, directory, module, production-data, workbook, Wind, Outlook, Excel, or business-process detail.
- The exact Derivative_Data `AGENTS.md` protected-module list and architecture migration boundaries.
- The exact Copilot command examples and test probes from Derivative_Data.
- The specific decision that Derivative_Data does not need a separate `docs/status.md` because its current status surface already exists elsewhere.

## 7. Project-local Facts That Must Not Become Canonical

The following facts are useful evidence from the pilot but must not become universal workflow-bootstrap rules:

- `prod-core-py312`.
- `D:\miniforge3\envs\prod-core-py312\python.exe`.
- Derivative_Data CLI command set and root wrapper command examples.
- Wind / Outlook / Excel lock details.
- Chinese operational directories and their exact layout.
- Derivative_Data protected modules.
- Generated workbook and production data constraints.
- The specific quarterly probe.
- Any Derivative_Data business workflow detail, including derivatives reporting, broker formats, valuation ETL, daily/monthly/quarterly pipelines, and project migration specifics.

## 8. Risks If Backported Too Aggressively

- Project facts could pollute canonical workflow guidance.
- workflow-bootstrap and chatgpt-handoff-pilot boundaries could blur again if task-package schema or report format details are copied into workflow-bootstrap.
- An `AGENTS.md` template could become too heavy and recreate the second-rulebook problem.
- A Copilot adapter could be mistaken for a second authoritative repository manual.
- The non-git profile could be misused as a mandatory rule for all projects, including normal Git-first repositories.
- Validators, automation, hooks, or CI could be introduced before the manual convention has enough cross-project evidence.
- Optional translated-adapter behavior could be overgeneralized into a requirement for every project.

## 9. Recommended ai-skill-hub Next Step

Review this memo first, then open a separate bounded task to absorb only the strongest generalized candidates.

The next step should not copy Derivative_Data project files into ai-skill-hub. It should not directly modify chatgpt-handoff-pilot. It should not immediately create a universal project-side runtime pack. It should not introduce validators, automation, CI, hooks, or rollout tooling.

A conservative absorption pass can update workflow-bootstrap supporting assets to describe the non-git runtime profile and invocation examples in generic terms, while preserving the rule that project-specific environment, command, directory, and production constraints stay project-local.

## 10. Suggested Bounded Follow-up Task

Suggested task name: `review_and_absorb_non_git_runtime_profile_candidates`

Suggested scope:

- Update `skills/workflow-bootstrap/non_git_runtime_profile.md`; if it does not exist, add it as a generic supporting asset.
- Update `skills/workflow-bootstrap/examples/invocation_examples.md`; if it already exists in a future run, perform a section-aware merge.
- Update `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md` to include a minimal checklist item for non-git task/report pairing and minimal handoff/status closure.
- Keep all Derivative_Data environment, command, directory, module, production-data, and business-process details out of canonical files.
- Do not modify `skills/chatgpt-handoff-pilot/*` or its schema.
- Do not add validators, automation, CI, hooks, rollout tooling, `.github/instructions/`, or `.github/agents/`.
- Validate by confirming that only authorized workflow-bootstrap files changed and that project-local facts remain excluded from canonical guidance.
