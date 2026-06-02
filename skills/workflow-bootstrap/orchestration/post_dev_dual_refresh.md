# Post-Dev Dual Refresh Orchestration（开发后双刷新编排）

Template type：`orchestration snippet / invocation template`

Owner layer：`workflow-bootstrap`

Delegated skills：`update-project-status`、`chatgpt-handoff-pilot`

Purpose：在一轮开发结束后，用一个薄编排模板串起：

1. `update-project-status` status refresh
2. `chatgpt-handoff-pilot` handoff refresh
3. merged round receipt

本模板不是新 skill，不替代 delegated skills，不重写任何 delegated protocol。模板 authoring 本身不执行真实 status / handoff 写入。

## When to use

- 一轮开发完成后，需要先整理当前状态，再把状态摘要交给 handoff 闭环。
- 需要显式区分 `dry-run`、write mode、sync authorization 与 handoff write authorization。
- 需要把 status 输出整理成结构化 handoff input，但不想引入第三套 protocol。
- 需要在 post-dev 文档刷新中保留 payload、validation、branch/head、stale wording 与 evidence pointer 的治理边界。

## Non-goals / boundaries

- 不创建新 skill。
- 不复制或改写 `update-project-status` protocol。
- 不复制或改写 `chatgpt-handoff-pilot` protocol。
- 不把 YAML block 写成 schema、validator 或 third protocol。
- 不默认执行真实 status / handoff writes。
- 不默认更新 `docs/HANDOFF.md`、status docs、status log 或外部 sync 目标。
- 不安装 hooks，不提交，不推送，不同步 adapter。
- 不把 downstream project-specific facts、raw runtime artifacts 或 broad changelog 复制进 generic template。

## Required inputs

- repository path：`<repo-root>`
- source mode：`git | workspace | hybrid | unknown`
- refresh mode：`dry-run | write`
- status output paths：`<status files/logs, if authorized>`
- sync authorization：`yes | no`
- handoff write authorization：`yes | no`
- handoff target：`<handoff path, if separately authorized>`
- evidence pointers：`<target PR / merge commit / task package / changed files / refreshed docs, when available>`
- branch/head provenance：`<mainline baseline / refresh branch HEAD / pre-write observation / post-write state>`
- validation provenance：`<PR-reported / locally rerun / refresh-level checks>`
- payload persistence decision：`<transient by default unless explicitly justified>`
- stale wording scan：`<current-state sections vs historical update-log references>`
- assumptions：`<explicit assumptions>`

## Side-effect matrix

| Action | Side effect | Authorization |
| --- | --- | --- |
| Template authoring | no status or handoff writes | always read-only for project state |
| Status dry-run | preview only | allowed when requested |
| Status write mode | may write status snapshot/log | requires explicit `update-project-status` authorization |
| External sync | may publish/sync status output | opt-in only |
| Handoff refresh | may update handoff target | requires explicit `chatgpt-handoff-pilot` scope |
| Payload persistence | may store transfer summary/evidence pointer | opt-in; default is transient |
| Hook install / commit / push | not part of this template | out of scope |

## Role separation guardrails

- `status.md` = status snapshot：current state, concise progress, active risks, next actions.
- `status_updates.log` = terse timeline：short chronological update entries; historical wording may remain if clearly historical.
- `HANDOFF.md` = operational SSOT / takeover interface：handoff-ready facts and next execution context.
- trial notes or task/execution report = mechanism evidence：dogfood findings, transfer payload rationale, and reusable pattern observations.
- 不默认把完整 transfer payload 放进 status snapshot。
- 不把 status snapshot 扩写成 project-level changelog。
- 不把 handoff document 当作 raw runtime artifact dump。

## Step 0: preflight and boundary confirmation

```text
Post-dev dual refresh boundary lock:
- This is a workflow-bootstrap orchestration snippet / invocation template.
- Delegated skills:
  - update-project-status owns status refresh behavior.
  - chatgpt-handoff-pilot owns handoff refresh and execution report behavior.
- Do not create a new skill.
- Do not rewrite delegated skill protocols.
- Do not bypass delegated skills or introduce a third handoff/status protocol.
- Confirm refresh mode: <dry-run | write>.
- Confirm sync authorization: <yes | no>.
- Confirm handoff write authorization: <yes | no>.
- Confirm payload persistence mode: <transient | status_snapshot | status_log | trial_notes | pr_body_only>.
- Confirm whether validation is PR-reported, locally rerun, refresh-level only, skipped, partial, or failed.
- If authorization is unclear, stop before writes.
```

## Step 1: update-project-status invocation

```text
Use update-project-status for the post-development status refresh.

Inputs:
- repository path: <repo-root>
- source mode: <git | workspace | hybrid | unknown>
- refresh mode: <dry-run | write>
- status output paths: <paths, if write mode is authorized>
- sync authorization: <yes | no>
- evidence pointers: <target PR / merge commit / task package / changed files / refreshed docs>

Output needed for Step 2:
- status headline
- key progress
- open risks or blockers
- recommended next steps
- evidence pointers
- source mode
- writes performed
- sync performed
- freshness note
- assumptions
```

## Step 1 -> Step 2 governed transfer block

The block below is only a transfer payload between Step 1 and Step 2. It is not a new schema, validator, or third protocol. Keep it concise and generic; use placeholders instead of downstream-specific project facts.

```yaml
handoff_input:
  status_headline:
  key_progress:
    -
  open_risks_blockers:
    -
  recommended_next_steps:
    -
  evidence_pointers:
    target_pr:
    merge_commit:
    task_package:
    changed_files:
      -
    refreshed_docs:
      -
    notes:
      -
  source_mode: git | workspace | hybrid | unknown
  writes_performed:
    -
  sync_performed: yes | no
  freshness_note:
  assumptions:
    -
  payload_persistence_decision:
    mode: transient | status_snapshot | status_log | trial_notes | pr_body_only
    reason:
  validation_provenance:
    pr_reported:
      status: present | absent
      source:
      commands:
        -
    locally_rerun:
      status: not_run | passed | failed | partial
      commands:
        -
    refresh_validation:
      status: not_run | passed | failed | partial
      commands:
        -
    note:
  stale_wording_scan:
    checked: yes | no
    current_state_sections_clean: yes | no
    historical_update_log_references:
      -
    accidental_stale_references:
      -
    action_taken:
      -
  branch_head_provenance:
    mainline_baseline_or_merge_commit:
    documentation_refresh_branch_head:
    pre_write_observation:
    post_write_branch_state:
    note:
```

Governance rules:

- Payload persistence default is `transient`; if no explicit persistence approval exists, treat the transfer payload as handoff input only.
- `status_snapshot` persistence requires an explicit reason and must not store the full transfer payload by default.
- `trial_notes` is preferred for dogfood or mechanism evidence that should not become status snapshot content.
- PR-reported validation must not be represented as locally rerun validation.
- Refresh-level checks such as `git diff --check` must stay separate from source/test validation.
- Skipped, unavailable, partial, or failed validation must be stated explicitly; failed validation remains visible in the receipt and final reviewer checklist.
- Stale wording scans should separate current-state sections from historical update-log references.
- Historical update-log entries may preserve old branch or pending wording when clearly historical.
- Current-state sections must not retain pending, branch-only, pre-merge, or pre-refresh wording after merge or refresh facts are known.
- Evidence pointers should be narrow and review-oriented: include target PR, merge commit, task package, changed files, and refreshed docs when available and appropriate.
- Evidence pointers should avoid raw runtime artifacts, local absolute paths, real data, credentials, broad unrelated file changelogs, and downstream-specific facts.

## Branch/head provenance guidance

Use branch/head wording that distinguishes observations from post-write branch state:

- project mainline baseline observed at `<merge commit>`;
- documentation refresh branch contains docs-only commit(s) on top of that baseline;
- current documentation refresh branch HEAD is `<refresh branch head>`;
- pre-write observation was `<observed state before docs refresh>`;
- post-write branch state is `<state after docs refresh commits>`.

Rules:

- Do not claim the refresh branch HEAD equals the mainline baseline after docs-only commits are added.
- If the exact baseline cannot be verified, mark it as `unknown` or `observed from available evidence` rather than inventing a commit relationship.
- Keep branch/head language generic; do not embed downstream PR numbers, commit hashes, phase names, validation counts, domain boundaries, storage scale, or allowed file lists.

## Step 2: chatgpt-handoff-pilot invocation

```text
Use chatgpt-handoff-pilot for post-development handoff closure.

Inputs:
- task package or approved scope: <handoff refresh scope>
- handoff target: <path, if a real handoff refresh is authorized>
- handoff_input: <governed transfer block from Step 1>

Rules:
- Preserve chatgpt-handoff-pilot protocol ownership.
- Use section-aware handoff maintenance only when a real handoff write is explicitly authorized.
- If no handoff write is authorized, produce a dry-run handoff summary or stop with required authorization.
- Do not copy this orchestration block into the handoff document as a raw artifact.
```

## Step 3: merged round receipt

```text
Merged round receipt:
- Status refresh result: <dry-run | written | skipped>
- Handoff refresh result: <dry-run | written | skipped>
- Sync result: <not configured | not authorized | completed | failed>
- Payload persistence: <transient | status_snapshot | status_log | trial_notes | pr_body_only> because <reason>
- Validation provenance:
  - PR-reported: <present | absent> from <source>
  - Locally rerun: <not_run | passed | failed | partial> with <commands or reason>
  - Refresh validation: <not_run | passed | failed | partial> with <commands or reason>
- Stale wording scan:
  - Current-state sections clean: <yes | no>
  - Historical references preserved: <items or none>
  - Accidental stale references fixed or remaining: <items or none>
- Branch/head provenance:
  - Mainline baseline / merged PR commit: <observed commit or unknown>
  - Documentation refresh branch HEAD: <refresh branch head or unknown>
  - Pre-write observation: <summary>
  - Post-write branch state: <summary>
- Evidence pointers:
  - Target PR: <placeholder or none>
  - Merge commit: <placeholder or none>
  - Task package: <path or none>
  - Changed files: <narrow categories or paths>
  - Refreshed docs: <paths or none>
- Remaining risks:
  - <risk / blocker>
- Recommended next action:
  - <next action owner and action>
```

## Final reviewer checklist

Use this checklist as the closure gate for the orchestration run. It is not a delegated protocol replacement.

- File scope：only approved files changed; no delegated skills, adapters, generated indexes, repository status/HANDOFF files, hooks, push, or merge unless explicitly authorized.
- Source/runtime safety：source files and runtime behavior were not changed by a docs-only orchestration update; source tests are not required unless source files changed.
- Payload persistence：default is `transient`; `status_snapshot` has explicit justification; large transfer payloads are not persisted into status by default.
- Validation provenance：PR-reported, locally rerun, skipped/unavailable, partial, failed, and refresh-level checks are not mixed.
- Stale wording scan：current-state sections were checked separately from historical update-log references.
- Branch/head wording：mainline baseline or merged PR commit is not conflated with documentation refresh branch HEAD.
- Status snapshot integrity：status remains a snapshot, not a changelog or raw transfer dump.
- HANDOFF/log role clarity：HANDOFF remains operational takeover interface; status log remains terse timeline; trial notes/task reports remain mechanism evidence.
- Generic vs project-specific separation：template uses placeholders and does not copy downstream project facts, commit hashes, validation counts, storage scale, domain boundaries, or allowed file lists.
- Evidence pointer quality：pointers are narrow, review-oriented, and avoid raw artifacts, local absolute paths, real data, credentials, or unrelated broad changelogs.

## Stop conditions

- Required files or delegated skill guidance cannot be located.
- Requested writes are not explicitly authorized.
- A real status refresh or handoff refresh would exceed the approved scope.
- The handoff block starts behaving like a new protocol, schema, or validator.
- Implementation requires editing delegated skill protocols.
- Adapter changes, hook installation, commit, push, or external sync become necessary without explicit approval.
- Status output and handoff target disagree in a way that could overwrite current-state facts.
- Validation provenance cannot distinguish PR-reported, locally rerun, refresh-level, skipped, partial, or failed checks.
- Branch/head provenance would require inventing an unverified baseline or commit relationship.
- Payload persistence would require storing full transfer payloads in status by default.
- Project-specific downstream facts would need to be copied into this generic template.

## Output requirements

- State whether the run was `dry-run` or write mode.
- List status outputs written, or state `none`.
- List handoff outputs written, or state `none`.
- State whether sync was performed.
- Include the merged round receipt.
- Record assumptions and unresolved risks.
- Confirm delegated skills were not modified and no third protocol was introduced.
