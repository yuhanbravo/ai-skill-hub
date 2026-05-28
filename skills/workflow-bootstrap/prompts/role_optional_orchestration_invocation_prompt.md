# Role-Optional Orchestration Invocation Prompt

## Purpose

本提示词用于显式调用 `workflow-bootstrap` 的 role chain，并允许只运行本轮真正需要的角色段。它适合完整运行 `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer`，也适合在 task package 已充分讨论、已审阅、已实施或已报告后，只进入下一段角色。

> Active canonical policy：本文件采用“中文为主、英文术语保留”的 active canonical 形式；不维护中英文双主本以避免 drift。

## When to use

- 需要 copy-ready 的 `workflow-bootstrap` 调用入口。
- 需要显式选择 `roles_to_run`，而不是默认串行执行五个角色。
- 需要同一工具跨角色执行，并保留 `[PHASE-SWITCH]` 边界。
- 需要保持 `workflow-bootstrap` 只负责 workflow shell / role boundary，并把 task package、bounded execution、execution report 协议继续交给 `chatgpt-handoff-pilot`。

## Copy-ready prompt

```text
Use workflow-bootstrap for this role-optional orchestration run.

Read:
- skills/workflow-bootstrap/SKILL.md
- skills/workflow-bootstrap/orchestration_snippets.md
- skills/chatgpt-handoff-pilot/SKILL.md only for protocol ownership boundaries

task_description:
- <what this run needs to accomplish>

current_state:
- <what has already been discussed, drafted, reviewed, implemented, or reported>

roles_to_run:
- <Drafter | Reviewer | Implementer | Reporter | Final Reviewer>
- <use one role, a contiguous role segment, or the full chain>

roles_already_completed:
- <role>: <accepted | not accepted | not applicable> - <evidence or source>

accepted_inputs:
- <task package, reviewed scope, implementation summary, execution report, or other accepted input>

constraints:
- Keep workflow-bootstrap as workflow shell and role-boundary owner.
- Keep chatgpt-handoff-pilot as task package / bounded execution / execution report protocol owner.
- Do not rerun any role marked accepted unless the user explicitly asks for re-review or revision.
- If a selected role lacks its required input, stop and request the missing input before continuing.
- Do not create a second local rulebook or expand beyond the reviewed boundary.

expected_output:
- <decision, task package, implementation summary, execution report, closure review, or other output>

context_files:
- <paths relevant to this run>

stop_conditions:
- Required canonical guidance cannot be located.
- roles_to_run is not clear enough to determine the next role boundary.
- A selected role lacks required accepted input.
- The run would rewrite chatgpt-handoff-pilot protocol text instead of referencing it.
- The run would perform implementation before Reviewer has passed the task package or reviewed scope.

Execution rules:
1. Confirm the selected role segment and the frozen accepted inputs.
2. Apply the relevant snippets from skills/workflow-bootstrap/orchestration_snippets.md.
3. Use explicit [PHASE-SWITCH] statements whenever the same tool continues across roles.
4. Log out-of-scope findings without silently fixing them.
5. Return only the output owned by the selected role segment.
```

## Role selection guide

| Situation | roles_to_run |
| --- | --- |
| Nothing has been drafted yet | `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer` |
| Task package was discussed but not gate-reviewed | `Reviewer` |
| Task package or reviewed scope already passed | `Implementer -> Reporter` |
| Implementation summary exists but report is missing | `Reporter` |
| Implementation and report are ready for closure | `Final Reviewer` |
| Closure review returns No-Go for implementation gap | `Implementer -> Reporter -> Final Reviewer` |
| Closure review returns No-Go for evidence/reporting gap | `Reporter -> Final Reviewer` |

## Examples

### Full chain from zero

```text
Use workflow-bootstrap for this role-optional orchestration run.

task_description:
- Prepare and execute a bounded documentation update for <topic>.

current_state:
- No task package has been drafted.

roles_to_run:
- Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer

roles_already_completed:
- none

accepted_inputs:
- none

constraints:
- Keep workflow-bootstrap as workflow shell and role-boundary owner.
- Keep chatgpt-handoff-pilot as protocol owner.
- Do not expand beyond <authorized paths>.

expected_output:
- task package, Reviewer decision, implementation summary, execution report, and closure decision

context_files:
- <paths>

stop_conditions:
- Stop before implementation if Reviewer does not return Pass.
```

### Reviewer only after discussion

```text
Use workflow-bootstrap for this role-optional orchestration run.

task_description:
- Review the discussed task package before bounded execution.

current_state:
- The task package was discussed with the maintainer and is ready for Safety Gate review.

roles_to_run:
- Reviewer

roles_already_completed:
- Drafter: accepted - task package text in this thread

accepted_inputs:
- <paste or reference the accepted task package>

constraints:
- Do not rewrite the task package unless the decision is Needs Fix.
- Do not implement.

expected_output:
- Reviewer decision: Pass, Needs Fix, or Reject

context_files:
- <paths>

stop_conditions:
- Stop if task package scope or acceptance checks are missing.
```

### Implementer plus Reporter after review pass

```text
Use workflow-bootstrap for this role-optional orchestration run.

task_description:
- Implement the reviewed scope and report the result.

current_state:
- Reviewer returned Pass for the accepted task package.

roles_to_run:
- Implementer -> Reporter

roles_already_completed:
- Drafter: accepted - <source>
- Reviewer: accepted - Pass decision at <source>

accepted_inputs:
- <reviewed task package or reviewed scope>
- <Reviewer Pass decision>

constraints:
- Implement only the reviewed scope.
- Log out-of-scope issues without modifying them.

expected_output:
- implementation summary and execution report

context_files:
- <paths>

stop_conditions:
- Stop if reviewed scope and Reviewer Pass evidence are not available.
```

### Final Reviewer only

```text
Use workflow-bootstrap for this role-optional orchestration run.

task_description:
- Perform closure review for the completed bounded execution.

current_state:
- Implementation summary and execution report are available.

roles_to_run:
- Final Reviewer

roles_already_completed:
- Drafter: accepted - <source>
- Reviewer: accepted - <source>
- Implementer: accepted - <source>
- Reporter: accepted - <source>

accepted_inputs:
- <implementation summary>
- <execution report>
- <reviewed task package or reviewed scope>

constraints:
- Do not perform new implementation.
- Return Go, Go with Conditions, or No-Go.

expected_output:
- closure decision, findings, conditions or minimum backfill

context_files:
- <paths>

stop_conditions:
- Stop if implementation summary or execution report is missing.
```

## Notes

- `roles_to_run` should normally be one role or a contiguous role segment.
- Non-contiguous role jumps are allowed only when all skipped roles are listed under `roles_already_completed` with accepted evidence.
- Tool names such as Copilot, Codex, ChatGPT, Cline, and DeepSeek are adapter examples only; they are not canonical role requirements.
- This prompt is an invocation wrapper. The role snippets remain in `orchestration_snippets.md`; handoff protocol details remain owned by `chatgpt-handoff-pilot`.
