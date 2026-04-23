# Phase 3A Execution Report: Project-Side Runtime Pack Template Sketch

## Scope Restatement

This execution implemented only the Phase 3A canonical template-sketch assets authorized by `tasks/copilot-codex-workflow_phase3a_template_sketch_task_package.md`.

In-scope output was limited to:

1. a runtime-pack inclusion decision sketch for future project-side v1;
2. an `AGENTS.md` template sketch;
3. a `.github/copilot-instructions.md` template sketch;
4. a minimal `workflow-bootstrap` README navigation update;
5. this execution report.

This round produced canonical sketch assets only. It did not implement a real project-side runtime pack, and it did not enter rollout, distribution, or adoption.

## Files Changed

- Added: `skills/workflow-bootstrap/project_side_runtime_pack_template_sketch.md`
- Added: `skills/workflow-bootstrap/project_side_agents_md_template_sketch.md`
- Added: `skills/workflow-bootstrap/project_side_copilot_instructions_template_sketch.md`
- Updated: `skills/workflow-bootstrap/README.md` (minimal Phase 3A sketch navigation only)
- Added: `tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`

## What Was Sketched

### 1) Runtime pack inclusion decision sketch

Created a canonical v1 inclusion matrix that explicitly classifies:

- `AGENTS.md` as required;
- `.github/copilot-instructions.md` as required;
- `.github/instructions/*.instructions.md` as optional;
- `.github/agents/*.agent.md` as not recommended in v1.

The sketch also explains why the v1 pack should stay centered on the entrypoint pair first, rather than adding more surfaces immediately.

### 2) `AGENTS.md` template sketch

Created a future project-side `AGENTS.md` template sketch that:

- preserves Phase 2's master-entrypoint conclusion;
- separates fixed fields from project-fill fields;
- keeps the file dispatch-oriented, reference-first, and non-canonical;
- retains canonical precedence and no-second-rulebook boundaries.

### 3) Copilot thin-adapter template sketch

Created a future project-side `.github/copilot-instructions.md` template sketch that:

- preserves Phase 2's thin-adapter conclusion;
- keeps the file limited to high-frequency, high-constraint guidance;
- backreferences `AGENTS.md` explicitly;
- lists what must stay out to avoid duplication.

### 4) Path backreference and anti-expansion guidance

Placed the path-expression sketch and anti-second-rulebook constraints in the runtime-pack template sketch so that the Phase 3A output stays within the task package's authorized file set.

This includes:

- placeholder-based path expression guidance;
- project-filled vs fixed path responsibilities;
- change-routing guidance for deciding what belongs back in canonical guidance.

## What Was Explicitly Not Implemented

- No real project-side runtime surfaces were added or modified for this phase:
  - no new or changed repository-root `AGENTS.md`;
  - no new or changed real `.github/copilot-instructions.md`;
  - no new real `.github/instructions/*.instructions.md`;
  - no new real `.github/agents/*.agent.md`.
- No rollout, distribution, adoption, or consumer-repo writes were performed.
- No sync/export/import/check/index tooling changes were made.
- No discoverability, adapter, or index files were changed.
- No core contract changes were made to `chatgpt-handoff-pilot` or any other existing skill.
- No separate Phase 3A sketch files were added for `.github/instructions/*.instructions.md` or `.github/agents/*.agent.md`, because the task package fixed the authorized deliverables to the three canonical sketch files above and v1 does not require dedicated sketches for those deferred surfaces.

## Boundary Check

- `skills/` remained the canonical source-of-truth.
- All new content was added as canonical sketch assets only.
- New documents explicitly state that they do not create real project-side runtime files in this repository.
- `AGENTS.md` remains a future project-side master-entrypoint sketch object only.
- `.github/copilot-instructions.md` remains a future Copilot-specific thin-adapter sketch object only.
- README changes were limited to a small Phase 3A sketch navigation section.

## Validation Notes

Executed checks:

1. Document-boundary check by confirming no real project-side runtime surfaces were added or modified by this phase.
2. Consistency check against:
   - `tasks/copilot-codex-workflow_phase2_entrypoint_decision_memo.md`
   - `tasks/copilot-codex-workflow_phase2_execution_report.md`
   - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
3. Expression check confirming the new sketches preserve:
   - `AGENTS.md` as the thinnest master entrypoint;
   - `.github/copilot-instructions.md` as the Copilot-specific thin adapter;
   - canonical precedence on conflict;
   - no-second-rulebook constraints;
   - explicit v1 required / optional / not-recommended classification.

Not run:

- No extra repository validation scripts were run, because this round only changed canonical sketch documents and a minimal README navigation section. Running tooling would have widened scope without adding direct validation value for these document-only changes.

## Risks / Assumptions

1. Assumption: the Phase 3A task package's fixed execution-report path takes precedence over the shorter filename requested in the operator message, so this execution used `tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`.
2. Assumption: path backreference examples should remain placeholder-based until a real consumer-repo structure is in scope.
3. Risk: future implementation teams may still try to introduce `.github/instructions/*.instructions.md` too early unless v1 discipline is enforced during rollout planning.
4. Risk: future consumer repos may package canonical guidance differently, requiring careful resolution of placeholder paths during implementation.

## Deferred Questions

1. When a real consumer repo is selected, what exact local paths should replace the placeholder canonical references?
2. What concrete threshold should trigger optional `.github/instructions/*.instructions.md` in a project-side v1.1 or later?
3. Under what later phase, if any, should `.github/agents/*.agent.md` be reconsidered?

These questions were intentionally deferred because Phase 3A is sketch-only and does not authorize real consumer-side implementation.

## Recommended Next Step

If a later phase is authorized, use these Phase 3A sketch assets to prepare a bounded implementation task package for a single consumer-repo trial, with concrete path resolution and continued enforcement that the project-side runtime pack remains thin and non-canonical.
