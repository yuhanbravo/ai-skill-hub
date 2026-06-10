# project-takeover Invocation Examples

## Scope

These examples show how to invoke existing `project-takeover` assets without copying reusable prompt bodies or redefining the skill protocol.

Use them as entry shapes for:

- baseline takeover
- strict phased takeover execution
- delta takeover
- dry-run rerun gate
- risk-focused takeover follow-up
- handoff redirect
- limited-scope takeover

## Existing Assets Referenced

- `prompts/reusable_prompts.md`
  - Template 1: standard takeover invocation
  - Template 2: strict phased execution template
  - Template 3: post-takeover delta update
  - Template 4: dry-run rerun necessity gate
  - Template 5: post-takeover risk focus
  - Template 6: handoff redirect

## Example 1: Baseline Takeover

### Use when

Use this when a new maintainer or AI agent is entering an unfamiliar repository and needs a first takeover packet, onboarding summary, risk list, and next actions.

### Example invocation

```text
Use project-takeover for a baseline takeover of this repository.

Project root: <project-root>
Goal: Generate the initial takeover packet and onboarding summary.
Known local rules: <AGENTS.md-or-none>
Important context paths:
- README.md
- docs/
- tasks/
- tests/

Constraints:
- Prefer project-local configuration over shared assumptions.
- Do not run install or safe-fix actions unless explicitly authorized.
- Record missing tools or scripts as soft-fail evidence.
```

### Expected entry

Reference `prompts/reusable_prompts.md` Template 1.

### Boundary

Do not use this example for bounded implementation, project status refresh, workflow bootstrap, or skill governance. If the user already has a concrete implementation task package, redirect to `chatgpt-handoff-pilot` instead of creating a broad takeover packet.

## Example 2: Strict Phased Takeover Execution

### Use when

Use this when the caller knows the takeover parameters and wants the agent to explicitly walk through `scan -> understand -> structure -> output`.

### Example invocation

```text
Use project-takeover with the strict phased execution branch.

Project root: <project-root>
Primary goal: <takeover | onboarding | handoff prep>
Config path: <path-or-none>
Report dir: <path-or-default>
Shared dir: <path-or-none>
Dry run: <yes-or-no>
Apply safe fixes: <yes-or-no>
Install: <yes-or-no>
Structure script override: <path-or-none>
Docs script override: <path-or-none>

Please report the active parameters before scanning.
```

### Expected entry

Reference `prompts/reusable_prompts.md` Template 2.

### Boundary

Do not treat missing optional paths as permission to invent repo-specific behavior. Keep `--apply-safe-fixes` and `--install` explicit opt-ins.

## Example 3: Delta Takeover

### Use when

Use this when historical takeover outputs, a handoff record, a status note, or an execution report already exists and the user needs only the changes since that prior baseline.

### Example invocation

```text
Use project-takeover for a delta takeover.

Existing baseline:
- <docs/takeover/project_takeover_report.md-or-other-prior-artifact>
- <docs/HANDOFF.md-or-status-note-if-relevant>
- <execution-report-path-if-relevant>

Current focus:
- Identify which prior conclusions still hold.
- Identify new or changed docs, task sources, environment readiness, risks, and blockers.
- Recommend whether a full takeover rerun is needed.

Constraints:
- Do not regenerate the full takeover packet unless the delta evidence says it is needed.
- Separate reused conclusions, new conclusions, and open questions.
```

### Expected entry

Reference `prompts/reusable_prompts.md` Template 3.

### Boundary

Do not use this as a handoff document refresh or execution report generator. If the requested output is a merged project handoff update, turn to `chatgpt-handoff-pilot`; if it is a status-first refresh, turn to the appropriate status update skill.

## Example 4: Dry-Run Gate

### Use when

Use this before writing takeover outputs when the user wants a read-only gate: whether takeover should run, what risks exist, and what minimal parameters should be used next.

### Example invocation

```text
Use project-takeover for a dry-run rerun necessity gate.

Project root: <project-root>
Existing takeover output: <path-or-none>
Config path: <path-or-none>
Report dir: <path-or-default>
Shared dir: <path-or-none>
Structure script override: <path-or-none>
Docs script override: <path-or-none>
Dry run: yes

Please decide:
- rerun_recommendation: yes|no
- evidence for the decision
- suggested minimal next-run parameters
```

### Expected entry

Reference `prompts/reusable_prompts.md` Template 4.

### Boundary

Do not write formal takeover documents during this gate. Do not convert dry-run findings into implementation changes; record missing tools, missing scripts, or environment problems as evidence.

## Example 5: Risk-Focused Takeover Follow-Up

### Use when

Use this when the baseline takeover already exists and the user explicitly wants project onboarding through risks, boundaries, blockers, unknowns, and next actions.

### Example invocation

```text
Use project-takeover for a risk-focused takeover follow-up.

Baseline inputs:
- <project_takeover_report.md>
- <project_onboarding_summary.md>
- <recent-status-or-execution-report-if-relevant>

Focus:
- high-priority risks
- boundaries and explicit non-goals
- blockers and unknowns
- minimum mitigation actions
- validation methods
- decision-needed items
```

### Expected entry

Reference `prompts/reusable_prompts.md` Template 5.

### Boundary

Do not rewrite the historical takeover packet by default. Do not expand this into a full project management plan or a skill-governance review.

## Example 6: Handoff Redirect

### Use when

Use this when the user starts with takeover language but the real need is a handoff refresh, bounded implementation package, status refresh, execution report, or reviewer packet.

### Example invocation

```text
The user asked for project-takeover, but first decide whether this is really a handoff/status/report task.

Current request:
- <paste-user-request-or-summary>

Existing artifacts:
- <handoff-path-if-any>
- <status-path-if-any>
- <execution-report-path-if-any>

If the request is not a takeover, recommend the correct skill entry and explain why.
Do not expand project-takeover output beyond the redirect decision.
```

### Expected entry

Reference `prompts/reusable_prompts.md` Template 6.

### Boundary

Redirect to `chatgpt-handoff-pilot` for task packages, bounded execution, execution reports, review packets, or project handoff merges. Redirect to the appropriate status or system handoff skill when the requested artifact is status-first or system-level. Do not import those skills' protocols into `project-takeover`.

## Example 7: Limited-Scope Takeover

### Use when

Use this when the user wants takeover context for only one module, directory, task package, pull request, or project phase instead of the whole repository.

### Example invocation

```text
Use project-takeover for a limited-scope takeover.

Scope target: <module | directory | task package | PR | phase>
Path or reference: <path-or-identifier>
Project root: <project-root>
Primary goal: onboarding for this limited area only

Include:
- local docs and task sources that affect this scope
- environment or script requirements for this scope
- risks, blockers, unknowns, and next actions limited to this scope

Exclude:
- full repository takeover
- unrelated skill or workflow governance
- implementation outside this scope
```

### Expected entry

Reference `prompts/reusable_prompts.md` Template 2 as a scoped invocation shape, not as a full-repository takeover requirement.

For limited-scope use, the mandatory fields are `Project root`, `Scope target`, `Path or reference`, `Primary goal`, `Dry run`, `Apply safe fixes`, and `Install`. `Config path`, `Report dir`, `Shared dir`, `Structure script override`, and `Docs script override` may be set to `none` when they are not relevant to the scoped target.

### Boundary

Keep scanning, evidence collection, risk identification, next actions, and output limited to the declared scope. The output should be a limited-scope onboarding or takeover note, not a full project takeover report, unless the user explicitly requests that expansion. If the limited target is an implementation task package rather than onboarding context, redirect to `chatgpt-handoff-pilot`.
