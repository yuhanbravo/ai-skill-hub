# chatgpt-handoff-pilot Invocation Examples

## Scope

These examples show how to invoke existing `chatgpt-handoff-pilot` assets without copying reusable prompt bodies or redefining the skill protocol.

Use them as entry shapes for:

- task package handoff
- bounded execution handoff
- project handoff refresh
- execution report handoff
- review packet handoff
- continuation from an existing handoff record

## Existing Assets Referenced

- `prompts/reusable_prompts.md`
  - Template 1: generate a task package
  - Template 2: execute a task package
  - Template 3: generate or update the project handoff main document
  - Template 4: generate an execution report
- `prompts/review_packet_prompts.md`
  - Template 1: ask Codex to generate a review packet
  - Template 2: ask Copilot to generate a review packet
  - Template 3: ask ChatGPT to review from a review packet
- `templates/TASK_PACKAGE_TEMPLATE.md`
- `templates/EXECUTION_REPORT_TEMPLATE.md`
- `templates/REVIEW_PACKET_TEMPLATE.md`
- `templates/HANDOFF_CHECKLIST.md`
- `examples/example_task_package.md`
- `examples/example_execution_report.md`
- `examples/example_review_packet.md`

## Example 1: Generate a Task Package Handoff

### Use when

Use this when an upstream planner needs a bounded task package that can be handed to Codex, Copilot, or another implementer.

### Invocation shape

Reference `prompts/reusable_prompts.md` Template 1 and provide:

- background and goal
- in-scope files or directories
- explicit out-of-scope items
- acceptance criteria
- local constraints and required evidence
- expected output category, usually a task package

### Expected output

- a task package shaped like `templates/TASK_PACKAGE_TEMPLATE.md`
- explicit assumptions if the input is incomplete
- enough implementation boundary detail for another agent to execute without re-planning the task

### Boundaries

- Do not start implementation while generating the task package.
- Do not invent missing project facts.
- Do not copy the reusable prompt body into a new local protocol.
- Do not include unrelated downstream project history unless it is necessary task context.

## Example 2: Execute a Bounded Task Package

### Use when

Use this when an implementer has received a concrete task package and should perform bounded execution.

### Invocation shape

Reference `prompts/reusable_prompts.md` Template 2 and provide:

- the complete task package
- any required local rules such as `AGENTS.md`
- target files or directories
- expected validation commands or checks
- reporting requirements

The implementer should first restate the goal, scope, files likely to change, and explicit non-goals before editing.

### Expected output

- implementation limited to the task package
- changed files inside the authorized scope only
- a structured execution report after the work is complete

### Boundaries

- Do not broaden scope to adjacent cleanup.
- Do not modify files that the task package forbids.
- Do not treat extra findings as completed work; record them as risks or follow-ups.
- Do not replace project-local rules with this skill's general guidance.

## Example 3: Refresh the Project Handoff Main Document

### Use when

Use this when the requested artifact is an updated project handoff record, especially when `docs/HANDOFF.md` already exists.

### Invocation shape

Reference `prompts/reusable_prompts.md` Template 3 and provide:

- the current `docs/HANDOFF.md`, if present
- the new facts to merge
- the sections that should receive updates
- any historical handoff artifacts that should remain legacy-only
- the required execution report format

### Expected output

- section-aware updates to `docs/HANDOFF.md`
- an `Update Log` entry when appropriate
- preservation of existing human-written structure
- a short execution report describing the merge

### Boundaries

- Do not create a parallel handoff manual by default.
- Do not rewrite the whole document just to fit a template.
- Do not update historical generated handoff artifacts except to mark their legacy role when authorized.
- Do not use this example for broader status governance owned by another skill.

## Example 4: Prepare an Execution Report Handoff

### Use when

Use this after bounded execution, or when a previous implementation needs to be summarized for acceptance and continuation.

### Invocation shape

Reference `prompts/reusable_prompts.md` Template 4 and provide:

- the original task package or scope statement
- changed files summary
- validation commands and results
- known blockers, risks, assumptions, and extra findings
- any explicitly deferred work

### Expected output

- an execution report shaped like `templates/EXECUTION_REPORT_TEMPLATE.md`
- clear separation between completed work, non-changes, validation, blockers, and assumptions
- enough evidence for a reviewer or next implementer to decide whether to continue

### Boundaries

- Do not make new implementation changes while only producing a report.
- Do not overstate validation that was not run.
- Do not hide out-of-scope discoveries inside the completed-work section.
- Do not turn the report into a new task package unless that is separately requested.

## Example 5: Prepare a Review Packet

### Use when

Use this when the implementation is done and the reviewer needs a compact packet instead of a full chat transcript.

### Invocation shape

Reference `prompts/review_packet_prompts.md` Template 1 or Template 2 and provide:

- the task package
- the execution report
- changed files summary
- validation summary or relevant log snippets
- review focus requested from the upstream reviewer

### Expected output

- a review packet shaped like `templates/REVIEW_PACKET_TEMPLATE.md`
- a concise summary of the implementation delta
- explicit review focus
- clear separation from the original task package and execution report

### Boundaries

- Do not redefine the task.
- Do not replace the execution report.
- Do not paste long prompt bodies or full transcripts.
- Do not fill missing evidence with invented conclusions; mark it as missing or unverified.

## Example 6: Review from a Review Packet

### Use when

Use this when ChatGPT or an upstream reviewer receives a `review packet` and should judge readiness or request corrections.

### Invocation shape

Reference `prompts/review_packet_prompts.md` Template 3 and provide:

- the review packet
- the task package or execution report only if needed for evidence
- the intended next decision, such as accept, revise, continue, or ask for missing evidence

### Expected output

- review conclusion
- main risks or boundary issues
- missing evidence, if any
- recommended next step

### Boundaries

- Do not ask the implementer to rewrite unrelated background.
- Do not treat the review packet as a replacement for the task package or execution report.
- Do not approve scope that the packet says was not implemented.
- Do not escalate to workflow, tool, or governance changes unless the packet identifies them as blockers.

## Example 7: Continue from an Existing Handoff Record

### Use when

Use this when a new round should start from a prior task package, execution report, or review packet rather than from a fresh open-ended prompt.

### Invocation shape

Use the existing assets according to the next action:

- for a new bounded work item, reference `prompts/reusable_prompts.md` Template 1 and use the prior execution report as context
- for direct implementation of an already-approved task package, reference Template 2
- for acceptance evidence, reference Template 4
- for reviewer preparation, reference `prompts/review_packet_prompts.md` Template 1 or Template 2

Include:

- prior handoff artifact path or pasted content
- what changed since the prior round
- current scope and explicit non-goals
- acceptance criteria for this continuation only

### Expected output

- a bounded continuation artifact matching the selected existing template
- explicit carry-forward assumptions and risks
- no silent expansion beyond the new round's scope

### Boundaries

- Do not create a separate continuation protocol.
- Do not reuse stale acceptance criteria without checking current scope.
- Do not merge unrelated future work into the continuation.
- Do not make `workflow-bootstrap`, `system-handoff`, `system-status-update`, `project-takeover`, or `skill-governance` responsible for this skill's handoff protocol.
