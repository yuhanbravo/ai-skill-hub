# skill-governance Invocation Examples

## Scope

These examples show how to invoke existing `skill-governance` prompt assets without copying reusable prompt bodies or redefining the skill protocol.

Use them as entry shapes for:

- read-only skill evaluation
- governance decision support
- controlled single-skill refactor
- light skill refinement
- read-only sequential batch evaluation
- skill invocation and routing recommendation

`skill-governance` remains a governance entry for skill structure, maturity, boundaries, and controlled single-skill changes. It does not take over project workflow, handoff, takeover, status, migration, or agent wrapper responsibilities.

## Existing Assets Referenced

- `prompts/reusable_prompts.md`
  - Template 1: standard governance call
  - Template 2: controlled rewrite call
- `prompts/skill-evaluator.md`
- `prompts/skill-governor.md`
- `prompts/skill-refactor.md`
- `prompts/skill-refinement.md`
- `prompts/skill-batch-evaluator.md`
- `prompts/skill-invocation.md`

No template asset is referenced here because `skill-governance/templates/` has no current template files.

## Example 1: Skill Evaluator

### Use when

Use this when the user needs a read-only assessment of one skill's structure, entrypoints, boundaries, prompt placement, template placement, example coverage, and execution clarity.

### Example invocation

```text
Use skill-governance as a skill evaluator.

Target skill: skills/<target-skill>
Mode: read-only evaluation
rewrite=false

Evaluate:
- SKILL.md structure and invocation clarity
- README support role
- prompt, template, and example placement
- boundary clarity and cross-skill risk
- evidence-backed maturity level

Do not modify files.
```

### Expected entry

Reference `prompts/skill-evaluator.md`.

### Boundary

This is evaluation only. Do not rewrite the target skill, generate new assets, or modify prompt bodies. If the user asks for project onboarding, handoff, status refresh, workflow bootstrap, or migration readiness, recommend the corresponding specialized skill instead of evaluating it through `skill-governance`.

## Example 2: Skill Governor

### Use when

Use this when the user wants governance judgment after or during evaluation: priority, rewrite level, PR split, risk boundary, and whether implementation should happen now or be deferred.

### Example invocation

```text
Use skill-governance as the skill governor.

Target skill: skills/<target-skill>
rewrite=false

Goal:
- Evaluate and diagnose the target skill.
- Decide whether it should be kept, refined, or refactored.
- Recommend PR split and priority if changes are needed.
- Identify boundaries that must not be crossed.

Return SCORECARD, DIAGNOSIS, LEVEL, next_action, and risk_priority.
Do not edit files unless rewrite=true is separately approved.
```

### Expected entry

Reference `prompts/skill-governor.md` and, through it, `prompts/skill-evaluator.md`.

### Boundary

The governor decides and scopes; it does not silently implement. Keep the decision to one target skill. Do not use this example for broad protocol redesign, cross-skill restructuring, registry/index changes, workflow changes, or `.agents` wrapper changes.

## Example 3: Skill Refactor

### Use when

Use this only after evaluation/governance findings identify a bounded, low-risk change and the user explicitly authorizes implementation.

### Example invocation

```text
Use skill-governance for a controlled skill refactor.

Target skill: skills/<target-skill>
rewrite=true
rewrite_budget=20%

Inputs:
- SCORECARD: <paste-or-reference>
- DIAGNOSIS: <paste-or-reference>
- Approved change scope: <specific files or sections>
- Target type: <pattern | project | tool | governance>

Requirements:
- Apply only the bounded findings.
- Preserve the skill's existing responsibility.
- Do not modify other skills or shared tooling.
- Report residual risks after the refactor.
```

### Expected entry

Reference `prompts/skill-refactor.md`. If the caller has not provided `SCORECARD` and `DIAGNOSIS`, first route through `prompts/skill-governor.md`.

### Boundary

Use only after evaluation/governance findings identify a bounded, low-risk change. Do not use it for broad protocol redesign or cross-skill rewrites. Do not refactor prompt bodies, templates, scripts, tests, registry/index files, or workflow configuration unless those exact files are the authorized target for the single skill.

## Example 4: Skill Refinement

### Use when

Use this when a single skill is already stable and only needs light expression-level improvement, such as clearer wording, entrypoint clarity, example coverage, README compression, or boundary statement cleanup.

### Example invocation

```text
Use skill-governance for skill refinement.

Target skill: skills/<target-skill>
Mode: refinement only
rewrite=false

Focus:
- wording clarity
- invocation examples coverage
- README or SKILL.md entry clarity
- prompt-to-SKILL alignment wording
- boundary explanation

Constraints:
- Do not change execution semantics.
- Do not rewrite the full SKILL.md.
- Do not add new prompt behavior.
- Output only the minimal changed snippets or a bounded patch plan.
```

### Expected entry

Reference `prompts/skill-refinement.md`.

### Boundary

Refinement is not a structural rewrite. If evaluation identifies missing structure, type mismatch, or major execution ambiguity, escalate to governor decision first. Do not use refinement to smuggle in protocol changes or new cross-skill orchestration.

## Example 5: Batch Evaluator

### Use when

Use this when the user needs read-only evaluation across multiple first-level skills before deciding which follow-up PRs to open.

### Example invocation

```text
Use skill-governance as the batch evaluator.

Target: skills/
Mode: read-only sequential evaluation

Evaluate each first-level skill one at a time.
For each skill, output its own RESULT before moving to the next.
Then provide a summary table and priority recommendations.

Do not modify files.
Do not call refactor.
Do not rewrite multiple skills.
```

### Expected entry

Reference `prompts/skill-batch-evaluator.md`.

### Boundary

Batch evaluator is read-only sequential evaluation across multiple skills. It must not rewrite multiple skills in one pass. Any implementation work must be split into bounded follow-up PRs.

In short: `batch evaluator = read-only sequential evaluation, not batch rewrite`.

## Example 6: Skill Invocation / Routing

### Use when

Use this when the user is unsure which skill entry should handle a task and needs a routing recommendation before execution.

### Example invocation

```text
Use skill-governance for skill invocation and routing recommendation.

User request:
<paste request>

Known candidate skills:
- skill-governance
- workflow-bootstrap
- chatgpt-handoff-pilot
- project-takeover
- system-status-update
- system-handoff
- financial-data-project-migration
- file-structure-check

Please recommend:
- the correct skill
- the entry shape
- required parameters
- whether execution should start now or wait for a bounded task package

Do not execute the task by default.
```

### Expected entry

Reference `prompts/skill-invocation.md`.

### Boundary

Use this when the user needs to identify which skill entry should handle a task. The output should recommend the correct skill and entry shape, not execute the task by default.

Redirect rather than absorb other skills' responsibilities:

- use `workflow-bootstrap` for workflow shell, role split, and project-side runtime surface mapping
- use `chatgpt-handoff-pilot` for task packages, bounded execution, execution reports, and review packets
- use `project-takeover` for repository onboarding, baseline takeover, delta takeover, and dry-run takeover gates
- use `system-status-update` for system-level status-first linked refresh
- use `system-handoff` for system handoff output boundaries
- use `financial-data-project-migration` for financial migration readiness and task-package work
- use `file-structure-check` for folder-structure audits and misplaced-file detection
