# Project-Level Post-Dev Dual Refresh Prompt

Purpose: copyable invocation prompt for a project-level post-development status + handoff refresh.

Canonical owner: `workflow-bootstrap`
Canonical orchestration: `../orchestration/post_dev_dual_refresh.md`
Delegated skills:
- `update-project-status` owns project status refresh behavior.
- `chatgpt-handoff-pilot` owns project handoff refresh and execution report behavior.

Boundary:
- This prompt is an invocation helper only.
- This is project-level, not system-level.
- Do not use `system-status-update` or `system-handoff` for this run.
- Do not copy delegated protocols or create a third handoff/status protocol.
- Keep all project-specific facts in placeholders until supplied by the operator.

```text
Please run a project-level post-dev dual-refresh for the target project.

Use `workflow-bootstrap` post-dev dual-refresh orchestration as the thin owner.

Delegated skills:
1. Use `update-project-status` for the project status refresh.
2. Use `chatgpt-handoff-pilot` for the project handoff refresh.

Inputs:
- Repository path: <project-root>
- Source mode: <git | workspace | hybrid | unknown>
- Refresh mode: <dry-run | write>
- Status output paths, if write mode is authorized:
  - <status-file-path>
  - <status-log-path>
- Sync authorization: <yes | no>
- Handoff write authorization: <yes | no>
- Handoff target, if authorized: <handoff-path>
- Evidence pointers:
  - Task package / issue / PR: <pointer-or-none>
  - Changed files: <narrow-file-list-or-categories>
  - Refreshed docs: <paths-or-none>
- Validation provenance:
  - PR-reported: <present | absent> from <source-or-none>
  - Locally rerun: <not_run | passed | failed | partial> with <commands-or-reason>
  - Refresh-level checks: <not_run | passed | failed | partial> with <commands-or-reason>
- Payload persistence decision: <transient | status_snapshot | status_log | trial_notes | pr_body_only>
- Stale wording scan target: <current-state sections and update-log references>
- Assumptions: <explicit assumptions>

Execution boundaries:
- First refresh status, then pass only a concise governed transfer summary into handoff.
- Do not paste the full transfer block into the status snapshot or handoff document.
- Do not perform external sync unless explicitly authorized.
- Do not install hooks, commit, push, or merge as part of this refresh.
- Keep status snapshot, status log, and handoff roles separate.

Expected output:
- Status refresh result: <dry-run | written | skipped>
- Handoff refresh result: <dry-run | written | skipped>
- Sync result: <not configured | not authorized | completed | failed>
- Merged round receipt with validation provenance, stale wording scan, evidence pointers, risks, assumptions, and recommended next action.

Stop conditions:
- Requested writes are not explicitly authorized.
- The refresh would require system-level skills instead of project-level skills.
- The handoff/status transfer starts behaving like a new protocol or schema.
- Required target files, delegated skill guidance, or project scope cannot be located.
- Evidence would require raw runtime artifacts, credentials, real data, unrelated changelogs, or unverified project facts.
```
