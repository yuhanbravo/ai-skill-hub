# workflow-bootstrap Phase 3 Runtime Pack Minimal Manifest Execution Report

## 1. Scope Restatement

This bounded execution completed `workflow-bootstrap` Phase 3: Runtime Pack Minimal Manifest.

The goal was to update `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md` so it clearly defines project-side thin runtime surface guidance, minimal candidate surfaces, canonical ownership, Git-first / non-git boundaries, and deferred future surfaces.

This work stayed within the reviewed Phase 3 task package. It did not create project-side runtime files and did not modify `chatgpt-handoff-pilot`.

## 2. Files Changed

- `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
- `skills/workflow-bootstrap/SKILL.md`
- `skills/workflow-bootstrap/role_split_and_integration.md`
- `skills/workflow-bootstrap/review_tiers.md`
- `skills/workflow-bootstrap/non_git_runtime_profile.md`
- `skills/workflow-bootstrap/examples/invocation_examples.md`
- `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_execution_report.md`

## 3. What Changed

- Reworked `runtime_pack_minimal_manifest.md` from a broad future-target overview into project-side thin runtime surface guidance.
- Clarified that runtime pack guidance is not a second rulebook, not a canonical skill copy layer, not a new execution protocol, and not CI / validator / automation.
- Added canonical ownership wording:
  - `skills/` remains canonical.
  - `workflow-bootstrap` owns workflow shell, role split, runtime profile, review tier guidance, and runtime pack manifest guidance.
  - `chatgpt-handoff-pilot` owns task package, bounded execution, and execution report protocols.
- Defined minimal candidate project-side surfaces:
  - `AGENTS.md`
  - `.github/copilot-instructions.md`
  - `.github/copilot-instructions.zh-CN.md`
  - `tasks/README.md`
  - `tasks/<task-package>.md`
  - `tasks/<execution-report>.md`
- For each candidate surface, documented Chinese positioning, main use, canonical guidance references, what it should not contain, and Git-first / non-git / low-git applicability.
- Clarified thin entry principles: discover, route, and reference without copying canonical skill bodies or creating a parallel rule set.
- Clarified that `tasks/` may be the preferred project-local evidence path for non-git / low-git work, but is not a mandatory global path.
- Marked `.github/instructions/`, `.github/agents/`, tool adapters, validators / automation / CI, Phase 4 multi-project pilot, Phase 5 tool adapter candidates, and optional local skill payloads / adapters as deferred or out of scope.
- Added only minimal supporting references and boundary wording in the authorized supporting files.

## 4. What Was Not Changed

- Did not modify `skills/chatgpt-handoff-pilot/`.
- Did not redefine task package, bounded execution, or execution report schema.
- Did not create `tool_adapters/`.
- Did not add validators, scripts, tests, CI, hooks, or automation.
- Did not enter Phase 4 multi-project pilot or Phase 5 tool adapter candidate work.
- Did not create `.github/instructions/` or `.github/agents/`.
- Did not create `AGENTS.md`, `.github/copilot-instructions.md`, `.github/copilot-instructions.zh-CN.md`, or `tasks/README.md`.
- Did not modify `README.md`, `docs/HANDOFF.md`, status surfaces, or other unauthorized files.
- Did not copy `runtime_pack_minimal_manifest.md` body into supporting files.
- Did not write tool subscription differences, model strength, or tool preference into canonical guidance.

## 5. Validation Performed

- Read the reviewed Phase 3 task package and required canonical guidance before editing.
- Checked project-side runtime file paths with `Test-Path`:
  - `AGENTS.md`: exists in the workspace, but was not created or modified by this task.
  - `.github/copilot-instructions.md`: exists in the workspace, but was not created or modified by this task.
  - `.github/copilot-instructions.zh-CN.md`: not present.
  - `tasks/README.md`: not present.
  - `.github/instructions/`: not present.
  - `.github/agents/`: not present.
  - `tool_adapters/`: not present.
- Checked `git diff --name-only`; for tracked files it returned only authorized workflow-bootstrap documentation files:
  - `skills/workflow-bootstrap/SKILL.md`
  - `skills/workflow-bootstrap/examples/invocation_examples.md`
  - `skills/workflow-bootstrap/non_git_runtime_profile.md`
  - `skills/workflow-bootstrap/review_tiers.md`
  - `skills/workflow-bootstrap/role_split_and_integration.md`
  - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
- Checked the equivalent full change list with `git status --short`; it showed the same authorized modified files plus the authorized new report:
  - `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_execution_report.md`
- Checked `git diff --name-only -- skills\chatgpt-handoff-pilot README.md docs\HANDOFF.md`; it returned no changed files.
- Checked `git diff --name-only -- .github AGENTS.md tasks\README.md tool_adapters scripts tests .github\workflows skills\chatgpt-handoff-pilot README.md docs\HANDOFF.md`; it returned no changed files.
- Checked text for boundary terms across the changed workflow-bootstrap files, including ownership, mandatory/global wording, deferred surfaces, validators, automation, Phase 4, Phase 5, and `tasks/`.
- Ran `git diff --check`; after fixing two trailing whitespace issues in `SKILL.md`, it passed with only CRLF normalization warnings for:
  - `skills/workflow-bootstrap/examples/invocation_examples.md`
  - `skills/workflow-bootstrap/non_git_runtime_profile.md`
- The CRLF normalization warnings do not affect this documentation validation; they indicate Git line-ending normalization behavior for touched files.
- `git status --short` reported only authorized modified files, the authorized new report, and a pre-existing `.pytest_cache/` permission warning while listing status. The `.pytest_cache/` warning did not affect this documentation validation.

## 6. Boundary / Out-of-Scope Check

- Actual changed files are within the Authorized Files list.
- Runtime pack guidance is written as minimal, optional, project-aware guidance, not a mandatory global rule.
- Project-side runtime surfaces are described as thin entries, thin adapters, or evidence indexes, not a parallel canonical source.
- `tasks/` is described as a preferred project-local evidence path for non-git / low-git work, not as a mandatory global path for all projects.
- `chatgpt-handoff-pilot` remains the explicit owner of task package, bounded execution, and execution report protocols.
- Supporting files contain only minimal references, a short example, or boundary clarification.
- Deferred future surfaces remain deferred and are not described as Phase 3 implementation targets.

## 7. Follow-up Recommendations

- A Final Reviewer should review the Phase 3 diff, especially the candidate-surface table and deferred future surface wording.
- Any future work on `.github/instructions/`, `.github/agents/`, tool adapters, validators, automation, CI, Phase 4, or Phase 5 should start from a new reviewed task package.

## 8. Recommended Commit Message

```text
docs(workflow-bootstrap): update runtime pack minimal manifest guidance
```
