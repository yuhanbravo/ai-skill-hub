# Orchestration Snippets（最小实例 / Minimal Instance）

> 目的：提供一层可复用的薄编排胶水，把 `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer` 串起来；不重写 `chatgpt-handoff-pilot` 协议。
>
> Active canonical policy：本文件采用“中文为主、英文术语保留”的 active canonical 形式；不维护中英文双主本以避免 drift；旧版本如需保留仅可作为 historical reference。

## 1) Boundary（Step 0: Pre-Alignment）

将下面内容作为每轮的第一条消息：

```text
Boundary lock for this run:
- This round is orchestration-layer enhancement only.
- Do not rewrite task-package / bounded-execution / execution-report protocols.
- Keep workflow-bootstrap as shell and role-boundary owner.
- Keep chatgpt-handoff-pilot as protocol owner.
- Use thin wrappers and backreferences only; do not create a second rulebook.
```

## 2) PHASE-SWITCH（同一工具多角色必填）

当同一工具在不同角色间切换时，必须显式输出：

```text
[PHASE-SWITCH]
From: <previous role>
To: <next role>
Reason: explicit boundary handoff in a same-tool multi-role run.
Boundary reminder:
- Previous role output is frozen as input.
- Next role may only perform responsibilities owned by the new role.
- Out-of-scope findings are logged, not silently fixed.
```

## 3) Drafter（起草者）Snippet（Step 1）

```text
You are the Drafter.
Produce task package v0 using existing chatgpt-handoff-pilot template fields only:
- Background
- Goal
- In Scope
- Out of Scope
- Target files/areas
- Acceptance checks
- Constraints
- Output requirements
- Assumptions

Rules:
- Keep it executable and reviewable.
- Do not include implementation work.
- Do not expand protocol definitions.
```

Expected output：`task package v0` 草案。

## 4) Reviewer（Safety Gate / 审包者）Snippet（Step 2）

```text
You are the Reviewer (Safety Gate).
Review task package v0 and return one decision:
- Pass
- Needs Fix
- Reject

Must-check items:
1) Scope clarity and boundaries
2) Authorization path and ownership boundary
3) Out-of-scope explicitness
4) Acceptance verifiability
5) Role-responsibility separation

Output format:
- Decision: <Pass | Needs Fix | Reject>
- Findings:
  - Blocking
  - Non-blocking
- Required fixes (if not Pass)
- Re-review checklist
```

### Reviewer rollback branch

当决策不是 `Pass` 时：

```text
Rollback: return to Drafter for revision.
Max re-review rounds: 2.
Round counter: <n/2>
Only blocking findings are mandatory for next revision.
```

## 5) Implementer（边界执行者）Snippet（Step 3）

仅在 Reviewer 返回 `Pass` 后使用。

```text
You are the Implementer.
Before changes, restate boundaries:
- Authorized scope
- Explicit out-of-scope
- Acceptance checks to run

Execution rules:
- Implement only authorized scope.
- Log out-of-scope issues without modifying them.
- Keep edits minimal and traceable.

Output:
1) Implementation summary
2) Validation summary (what was verified vs not verified)
```

## 6) Reporter（执行报告者）Snippet（Step 4）

```text
You are the Reporter.
Generate execution report using existing chatgpt-handoff-pilot report structure.
Must include:
- What changed
- What was not changed
- Validation performed
- Blockers
- Next steps
- Risks and assumptions

Rule:
- Evidence first; if not verified, mark as not verified.
```

## 7) Final Reviewer（Closure Gate / 终审者）Snippet（Step 5）

```text
You are the Final Reviewer (Closure Gate).
Review implementation summary + execution report.
Return one decision:
- Go
- Go with Conditions
- No-Go

Must-check items:
1) Boundary violations
2) Validation sufficiency
3) Completeness of risk/assumption disclosure
4) Consistency between implemented scope and reported scope

Output format:
- Decision: <Go | Go with Conditions | No-Go>
- Closure findings
- Conditions or required follow-ups
- Minimal backfill items (if No-Go)
- Rollback target
```

### Final Reviewer rollback branches

- 若 `No-Go` 原因是 implementation gap：回退到 `Implementer`，并给最小 backfill 列表。
- 若 `No-Go` 原因是 reporting/evidence gap：回退到 `Reporter` 补齐报告证据。

统一使用显式分支语句：

```text
[ROLLBACK]
Gate: Final Reviewer
Reason: <implementation gap | reporting gap>
Rollback to: <Implementer | Reporter>
Minimum backfill required:
- ...
```

## 8) Minimal Run Order

1. Step 0 Boundary lock
2. Drafter produces task package v0
3. Reviewer Safety Gate
4. （如需）rollback 到 Drafter，最多 2 轮
5. Implementer bounded execution
6. Reporter execution report
7. Final Reviewer Closure Gate
8. （如需）rollback 到 Implementer/Reporter，直到 closure decision 满足

## 9) Thin-Wrap Guardrails

- 本文件只做 orchestration glue。
- 协议细节仍在 `chatgpt-handoff-pilot` prompts/templates。
- workflow shell ownership 仍在 `workflow-bootstrap`。
- 不在此处复制 protocol body。

## 10) Post-Dev Dual Refresh Orchestration（开发后双刷新编排）

Template type：`orchestration snippet / invocation template`

Owner layer：`workflow-bootstrap`

Delegated skills：`update-project-status`、`chatgpt-handoff-pilot`

Purpose：在一轮开发结束后，用一个薄编排模板串起：

1. `update-project-status` status refresh
2. `chatgpt-handoff-pilot` handoff refresh
3. merged round receipt

本模板不是新 skill，不替代 delegated skills，不重写任何 delegated protocol。模板 authoring 本身不执行真实 status / handoff 写入。

### When to use

- 一轮开发完成后，需要先整理当前状态，再把状态摘要交给 handoff 闭环。
- 需要显式区分 `dry-run`、write mode、sync authorization 与 handoff write authorization。
- 需要把 status 输出整理成结构化 handoff input，但不想引入第三套 protocol。

### Non-goals / boundaries

- 不创建新 skill。
- 不复制或改写 `update-project-status` protocol。
- 不复制或改写 `chatgpt-handoff-pilot` protocol。
- 不把 YAML block 写成 schema、validator 或 third protocol。
- 不默认执行真实 status / handoff writes。
- 不默认更新 `docs/HANDOFF.md`、status docs、status log 或外部 sync 目标。
- 不安装 hooks，不提交，不推送，不同步 adapter。

### Required inputs

- repository path：`<repo-root>`
- source mode：`git | workspace | hybrid | unknown`
- refresh mode：`dry-run | write`
- status output paths：`<status files/logs, if authorized>`
- sync authorization：`yes | no`
- handoff write authorization：`yes | no`
- handoff target：`<handoff path, if separately authorized>`
- evidence pointers：`<files / commits / task artifacts>`
- assumptions：`<explicit assumptions>`

### Side-effect matrix

| Action | Side effect | Authorization |
| --- | --- | --- |
| Template authoring | no status or handoff writes | always read-only for project state |
| Status dry-run | preview only | allowed when requested |
| Status write mode | may write status snapshot/log | requires explicit `update-project-status` authorization |
| External sync | may publish/sync status output | opt-in only |
| Handoff refresh | may update handoff target | requires explicit `chatgpt-handoff-pilot` scope |
| Hook install / commit / push | not part of this template | out of scope |

### Step 0: preflight and boundary confirmation

```text
Post-dev dual refresh boundary lock:
- This is a workflow-bootstrap orchestration snippet / invocation template.
- Delegated skills:
  - update-project-status owns status refresh behavior.
  - chatgpt-handoff-pilot owns handoff refresh and execution report behavior.
- Do not create a new skill.
- Do not rewrite delegated skill protocols.
- Confirm refresh mode: <dry-run | write>.
- Confirm sync authorization: <yes | no>.
- Confirm handoff write authorization: <yes | no>.
- If authorization is unclear, stop before writes.
```

### Step 1: update-project-status invocation

```text
Use update-project-status for the post-development status refresh.

Inputs:
- repository path: <repo-root>
- source mode: <git | workspace | hybrid | unknown>
- refresh mode: <dry-run | write>
- status output paths: <paths, if write mode is authorized>
- sync authorization: <yes | no>
- evidence pointers: <files / commits / task artifacts>

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

### Step 1 -> Step 2 structured handoff input block

The block below is only a transfer payload between Step 1 and Step 2. It is not a new schema, validator, or third protocol.

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
    files:
      -
    commits:
      -
  source_mode: git | workspace | hybrid | unknown
  writes_performed:
    -
  sync_performed: yes | no
  freshness_note:
  assumptions:
    -
```

### Step 2: chatgpt-handoff-pilot invocation

```text
Use chatgpt-handoff-pilot for post-development handoff closure.

Inputs:
- task package or approved scope: <handoff refresh scope>
- handoff target: <path, if a real handoff refresh is authorized>
- handoff_input: <YAML block from Step 1>

Rules:
- Preserve chatgpt-handoff-pilot protocol ownership.
- Use section-aware handoff maintenance only when a real handoff write is explicitly authorized.
- If no handoff write is authorized, produce a dry-run handoff summary or stop with required authorization.
```

### Step 3: merged round receipt

```text
Merged round receipt:
- Status refresh result: <dry-run | written | skipped>
- Handoff refresh result: <dry-run | written | skipped>
- Sync result: <not configured | not authorized | completed | failed>
- Evidence pointers:
  - <files / commits / task artifacts>
- Remaining risks:
  - <risk / blocker>
- Recommended next action:
  - <next action owner and action>
```

### Stop conditions

- Required files or delegated skill guidance cannot be located.
- Requested writes are not explicitly authorized.
- A real status refresh or handoff refresh would exceed the approved scope.
- The handoff block starts behaving like a new protocol, schema, or validator.
- Implementation requires editing delegated skill protocols.
- Adapter changes, hook installation, commit, push, or external sync become necessary without explicit approval.
- Status output and handoff target disagree in a way that could overwrite current-state facts.

### Output requirements

- State whether the run was `dry-run` or write mode.
- List status outputs written, or state `none`.
- List handoff outputs written, or state `none`.
- State whether sync was performed.
- Include the merged round receipt.
- Record assumptions and unresolved risks.


## 11) GitHub PR Bootstrap via gh CLI

Template type：`orchestration snippet / invocation template`

Owner layer：`workflow-bootstrap`

Purpose：提供一个可复用的薄编排片段，覆盖本地改动 -> commit message suggestion -> branch push -> gh pr create -> Codex review comment 的最小路径。该片段不是新 skill，不替代 git、GitHub CLI、Codex review settings，也不替代 `chatgpt-handoff-pilot` 协议。

### When to use

- 已完成 bounded implementation，且人类操作者准备发起 GitHub PR。
- `gh` CLI 可用，且仓库 remote 指向 GitHub。
- PR scope 已明确（文档或代码均可）。

### Non-goals / boundaries

- 不在未获明确授权时自动 commit。
- 不在未获明确授权时自动 push。
- 不在未获明确授权时创建或合并 PR。
- 不自动处理 GitHub review conversations。
- 不执行 PR merge。
- 不在未单独授权时修改 SSH config、`known_hosts`、GitHub auth。
- 不在未请求时运行网络诊断。
- 不把生成的 commit message 当作免审最终版本。

### Required inputs

- repo root：`<repo-root>`
- current branch：`<current-branch>`
- base branch：`<base-branch>`
- remote name：`<remote-name>`
- intended PR scope：`<intended-scope>`
- files intended for commit：`<file-list>`
- commit message style：`Conventional Commits compatible`（default）
- PR title：`<pr-title>`
- PR body file path：`<pr_body.md>`
- Codex review comment file path：`<codex_review_comment.md>`
- authorization flags：`commit/push/pr/comment = yes|no`

### Preflight read-only checks（PowerShell examples）

```powershell
git status --short
git branch --show-current
git branch -vv
git remote -v
gh --version
gh auth status
gh pr status
# optional
git diff --name-only
# optional
git diff --check
```

### Commit message suggestion block

建议输出结构：

```text
Recommended commit message:
Alternative commit message:
Rationale:
Files included:
Files excluded / not staged:
```

Conventional-Commits-compatible examples（不强制 semantic-release 规则）：

- `docs(workflow-bootstrap): add gh PR bootstrap snippet`
- `chore(github): document gh PR creation flow`

### PR body template（PowerShell here-string example）

```powershell
@"
## Summary
-

## Scope
-

## Validation
-

## Not changed
-

## Risks / assumptions
-

## Review focus
-
"@ | Set-Content -Encoding UTF8 <pr_body.md>
```

### `gh pr create` command example

```powershell
gh pr create `
  --base <base-branch> `
  --head <current-branch> `
  --title "<PR title>" `
  --body-file <pr_body.md>
```

可选 `--fill` / `--fill-verbose` 可从 commit 派生内容，但在本 workflow 中优先使用显式 `--title` + `--body-file` 以降低歧义。

### Codex review comment template

```powershell
@"
@codex review

Please review this PR with focus on:
- scope boundaries;
- whether changed files match the stated PR purpose;
- whether stale or duplicated workflow guidance was introduced;
- whether validation evidence is sufficient;
- whether any high-risk P0/P1 issues exist.
"@ | Set-Content -Encoding UTF8 codex_review_comment.md
```

```powershell
gh pr comment <PR_NUMBER_OR_URL> --body-file codex_review_comment.md
```

### Stop conditions

- current branch 是 `main/master` 且用户未显式授权直接在主分支工作。
- working tree 含有无法解释或与本 PR 无关的改动。
- `gh` 缺失或未认证。
- remote 缺失或并非 GitHub remote。
- base branch 不明确。
- commit scope 含糊不清。
- PR 已存在且用户未请求“更新/评论已有 PR”。
- 未获得明确 live commit / push / PR / comment 授权。
- 命令将修改 SSH config、`known_hosts`、GitHub auth、hooks 或 repo settings。

### Output requirements

- preflight summary
- proposed commit message
- PR title / body path
- exact commands to run（或已执行命令）
- PR URL（若已创建）
- Codex review comment status（若已发布）
- unresolved risks 与 next human action

### Local vs cloud applicability

- 实际执行 git/gh（检查、commit、push、PR、comment）优先在本地工作树完成。
- Cloud Codex 适合编辑该文档与提供命令编排片段。
- Cloud Codex 不应声称其检查了本地未提交文件，除非这些文件真实存在于当前 workspace。
