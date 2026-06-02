# GitHub PR Bootstrap via gh CLI

Template type：`orchestration snippet / invocation template`

Owner layer：`workflow-bootstrap`

Purpose：提供一个可复用的薄编排片段，覆盖本地改动 -> commit message suggestion -> branch push -> gh pr create -> Codex review comment 的最小路径。该片段不是新 skill，不替代 git、GitHub CLI、Codex review settings，也不替代 `chatgpt-handoff-pilot` 协议。

## When to use

- 已完成 bounded implementation，且人类操作者准备发起 GitHub PR。
- `gh` CLI 可用，且仓库 remote 指向 GitHub。
- PR scope 已明确（文档或代码均可）。

## Non-goals / boundaries

- 不在未获明确授权时自动 commit。
- 不在未获明确授权时自动 push。
- 不在未获明确授权时创建或合并 PR。
- 不自动处理 GitHub review conversations。
- 不执行 PR merge。
- 不在未单独授权时修改 SSH config、`known_hosts`、GitHub auth。
- 不在未请求时运行网络诊断。
- 不把生成的 commit message 当作免审最终版本。

## Required inputs

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

## Preflight read-only checks（PowerShell examples）

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

## Commit message suggestion block

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

## PR body template（PowerShell here-string example）

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

## `gh pr create` command example

```powershell
gh pr create `
  --base <base-branch> `
  --head <current-branch> `
  --title "<PR title>" `
  --body-file <pr_body.md>
```

可选 `--fill` / `--fill-verbose` 可从 commit 派生内容，但在本 workflow 中优先使用显式 `--title` + `--body-file` 以降低歧义。

## Codex review comment template

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

## Stop conditions

- current branch 是 `main/master` 且用户未显式授权直接在主分支工作。
- working tree 含有无法解释或与本 PR 无关的改动。
- `gh` 缺失或未认证。
- remote 缺失或并非 GitHub remote。
- base branch 不明确。
- commit scope 含糊不清。
- PR 已存在且用户未请求“更新/评论已有 PR”。
- 未获得明确 live commit / push / PR / comment 授权。
- 命令将修改 SSH config、`known_hosts`、GitHub auth、hooks 或 repo settings。

## Output requirements

- preflight summary
- proposed commit message
- PR title / body path
- exact commands to run（或已执行命令）
- PR URL（若已创建）
- Codex review comment status（若已发布）
- unresolved risks 与 next human action

## Local vs cloud applicability

- 实际执行 git/gh（检查、commit、push、PR、comment）优先在本地工作树完成。
- Cloud Codex 适合编辑该文档与提供命令编排片段。
- Cloud Codex 不应声称其检查了本地未提交文件，除非这些文件真实存在于当前 workspace。
