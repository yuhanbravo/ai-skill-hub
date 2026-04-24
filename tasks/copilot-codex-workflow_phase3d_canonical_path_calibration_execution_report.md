# Phase 3D Execution Report: Canonical Path Calibration

## 1. Scope Restatement

This execution performed only the Phase 3D **canonical path calibration** requested by:

- `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_task_package.md`

Bounded scope used in this round:

1. decide whether `<project-local-canonical-skill-path>` should be materialized in the current pilot repo;
2. write the authorized canonical path calibration memo and option comparison sketch;
3. apply only minimal backreference wording calibration to:
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
4. produce this execution report.

This round did **not** enter multi-repo rollout, distribution, adoption, tool changes, or project-side runtime-surface expansion.

## 2. Current Phase Continuity

This round preserves prior phase conclusions and only narrows path expression:

1. Phase 2 remains the source of the `AGENTS.md` master-entrypoint and Copilot thin-adapter decision.
2. Phase 3A remains the source of fixed/project-fill/placeholder field structure.
3. Phase 3B remains the source of placeholder-first path validation before real implementation.
4. Phase 3C remains the source of the real single consumer repo implementation pilot.
5. Phase 3D adds only path calibration over the existing pilot outcome; it does not reopen entrypoint selection or authorize broader rollout.

## 3. Files Changed

Changed in this round:

1. Updated: `AGENTS.md`
2. Updated: `.github/copilot-instructions.md`
3. Added: `skills/workflow-bootstrap/project_side_canonical_path_calibration_memo.md`
4. Added: `skills/workflow-bootstrap/project_side_canonical_path_option_comparison_sketch.md`
5. Added: `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_execution_report.md`

Not added:

1. `skills/workflow-bootstrap/project_side_backreference_wording_adjustment_note.md`

Reason:

- direct minimal wording calibration plus this execution report was sufficient; a separate adjustment note was not necessary.

## 4. Current Pilot Repo Inputs Used

Read and aligned against:

1. `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_task_package.md`
2. `AGENTS.md`
3. `.github/copilot-instructions.md`
4. `tasks/copilot-codex-workflow_phase2_execution_report.md`
5. `tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`
6. `tasks/copilot-codex-workflow_phase3b_pilot_validation_sketch_execution_report.md`
7. `tasks/copilot-codex-workflow_phase3c_single_consumer_repo_implementation_pilot_execution_report.md`
8. `skills/workflow-bootstrap/README.md`
9. `skills/workflow-bootstrap/canonical_backreference_rules_draft.md`
10. `skills/workflow-bootstrap/project_side_runtime_pack_template_sketch.md`
11. `skills/workflow-bootstrap/project_side_agents_md_template_sketch.md`
12. `skills/workflow-bootstrap/project_side_copilot_instructions_template_sketch.md`
13. `skills/workflow-bootstrap/pilot_repo_validation_sketch.md`

## 5. Calibration Questions Answered

### Q1. Should `<project-local-canonical-skill-path>` be materialized now?

Answer: **no**.

Reason:

1. the current pilot repo does not define a distinct project-local canonical payload artifact;
2. materializing the placeholder now would require either inventing a path or misusing an already-listed canonical path;
3. both choices would increase drift and second-rulebook risk.

### Q2. If not materialized, how should the placeholder be expressed?

Answer: keep it as a **controlled placeholder**.

Fixed expression used in `AGENTS.md`:

- it is conditional rather than simply optional;
- it is maintainer-filled only;
- it may be filled only after a distinct repo-local canonical payload file exists;
- it may remain unresolved only while no such path exists.

### Q3. Does `AGENTS.md` need backreference calibration?

Answer: **yes, minimally**.

Applied calibration:

1. updated the active task-package path from Phase 3C to Phase 3D;
2. changed the placeholder wording from a generic unresolved placeholder to a controlled placeholder;
3. clarified who fills it and under what conditions it may remain unresolved;
4. aligned the field-mapping heading with the current Phase 3D calibration state.

### Q4. Does `.github/copilot-instructions.md` need further tightening?

Answer: **yes, minimally**.

Applied calibration:

1. updated the active task-package path from Phase 3C to Phase 3D;
2. added one thin rule stating that the adapter must not invent a project-local canonical payload path and must follow `AGENTS.md`.

### Q5. Which fields still require maintainer confirmation?

Maintainer-confirmed items remain:

1. whether this repo later introduces a distinct project-local canonical payload artifact;
2. the exact path of that artifact if it is later added;
3. whether that artifact is truly canonical payload rather than a local note;
4. whether any future path should appear only in `AGENTS.md` or also be mirrored in `.github/copilot-instructions.md`.

### Q6. What is the main drift risk now?

Main drift risks remain:

1. inventing a placeholder replacement before a real canonical payload artifact exists;
2. copying canonical guidance into local entry files;
3. letting `.github/copilot-instructions.md` define path policy separately from `AGENTS.md`;
4. later treating this single-repo calibration as if it were already a multi-repo template standard.

## 6. Path Option Comparison Summary

Options considered:

1. keep a controlled placeholder;
2. materialize immediately as a repo-local path;
3. materialize as a project-local canonical payload path;
4. remove the placeholder entirely.

Recommendation:

- keep the controlled placeholder now.

Why this option won:

1. it matches the actual current repo state;
2. it reduces ambiguity without inventing a fake canonical path;
3. it preserves the fixed/project-fill/placeholder model from prior phases;
4. it keeps the path model thin and avoids scope growth.

## 7. Decision / Recommendation

Decision for the current pilot repo:

1. do **not** materialize `<project-local-canonical-skill-path>` yet;
2. keep concrete relative paths for the already-existing canonical guidance files;
3. keep the third path slot as a controlled placeholder in `AGENTS.md`;
4. keep `.github/copilot-instructions.md` thinner than `AGENTS.md` by referencing `AGENTS.md` as the source for any future project-local canonical payload declaration.

## 8. What Was Calibrated

1. `AGENTS.md` now expresses the project-local canonical payload path as a controlled placeholder rather than a loosely described follow-up item.
2. `AGENTS.md` now points to the active Phase 3D task package.
3. `.github/copilot-instructions.md` now points to the active Phase 3D task package.
4. `.github/copilot-instructions.md` now explicitly says it must not invent a project-local canonical payload path outside `AGENTS.md`.
5. Two new canonical calibration documents now record the recommendation and option comparison for future reference.

## 9. What Was Explicitly Not Implemented

Not implemented in this round:

1. no materialization of `<project-local-canonical-skill-path>` into a concrete path;
2. no new project-local canonical payload artifact;
3. no `.github/instructions/*.instructions.md` files;
4. no `.github/agents/*.agent.md` files;
5. no rollout, distribution, adoption, or cross-repo sync actions;
6. no sync/export/import/check tooling changes;
7. no adapter, index, or discoverability layer changes;
8. no broader project-side runtime-surface expansion.

## 10. Boundary Check

Boundary result: **pass** for Phase 3D bounded execution.

Explicitly confirmed:

1. this round remained canonical path calibration only;
2. this round did not enter multi-repo rollout;
3. this round did not enter distribution;
4. this round did not add unauthorized project-side file families;
5. this round did not modify tools, indexes, adapters, or other skills’ core contracts;
6. this round did not present path calibration as rollout readiness completion.

## 11. Validation Run

Executed checks:

1. existence check:
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
   - `skills/workflow-bootstrap/project_side_canonical_path_calibration_memo.md`
   - `skills/workflow-bootstrap/project_side_canonical_path_option_comparison_sketch.md`
2. `.github/` file listing check to confirm no unauthorized `.github/instructions/*` or `.github/agents/*` files were created.
3. expression check using targeted search for:
   - `<project-local-canonical-skill-path>`
   - `project-local canonical payload`
   - `canonical guidance`
   - `AGENTS.md`
4. working-tree check with `git status --short`.

Not run:

- no extra toolchain, distribution, or rollout commands were run, because they are out of scope for this document-first calibration phase.

## 12. Risks / Assumptions

1. Assumption: the current repo still does not define a distinct project-local canonical payload artifact beyond the concrete canonical references already listed.
2. Assumption: keeping a controlled placeholder is safer than inventing a concrete path in the absence of such an artifact.
3. Risk: future editors may still materialize the placeholder too early unless they follow the maintainer-only fill rule.
4. Risk: later phases may need to re-evaluate the placeholder if the repo’s canonical payload structure changes.

## 13. Repo-Specific Assumptions

The following remain repo-specific assumptions in the current calibration:

1. `skills/workflow-bootstrap/SKILL.md` remains the correct workflow canonical guidance path for this repo.
2. `skills/chatgpt-handoff-pilot/SKILL.md` remains the correct bounded-execution guidance path for this repo.
3. no distinct project-local canonical payload path currently exists in this repo.
4. the active task-package reference should now be the Phase 3D calibration package rather than the Phase 3C implementation pilot package.

## 14. Recommended Next Step

Recommended next step:

1. keep the controlled placeholder strategy unchanged until the repo actually introduces a distinct project-local canonical payload artifact;
2. if such an artifact is later proposed, require maintainer confirmation before replacing `<project-local-canonical-skill-path>`;
3. only after that re-evaluate whether another bounded phase is warranted for rollout-readiness or distribution-readiness discussion.

This recommendation does **not** imply that rollout, distribution, or broader runtime-pack expansion should start now.
