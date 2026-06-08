# GitHub PR Bootstrap Prompt

Purpose: copyable invocation prompt for a bounded GitHub PR bootstrap after implementation is complete.

Canonical owner: `workflow-bootstrap`
Canonical orchestration: `../orchestration/github_pr_bootstrap.md`

Boundary:
- This prompt is an invocation helper only.
- It does not replace Git, GitHub CLI, project review rules, or `chatgpt-handoff-pilot` execution reports.
- All live side effects require explicit authorization flags.
- Keep repository, branch, PR, and file details as placeholders until supplied by the operator.

```text
Please run the GitHub PR bootstrap orchestration for the current bounded change.

Use `workflow-bootstrap` GitHub PR bootstrap as the thin orchestration owner.

Inputs:
- Repository root: <repo-root>
- Current branch: <current-branch>
- Base branch: <base-branch>
- Remote name: <remote-name>
- Intended PR scope: <short-scope>
- Files intended for commit:
  - <path-or-category>
- Files explicitly excluded:
  - <path-or-category-or-none>
- Commit message style: <Conventional Commits compatible | other-project-style>
- PR title: <pr-title>
- PR body file path: <pr-body-file-path>
- Review comment file path: <review-comment-file-path>
- Authorization flags:
  - commit: <yes | no>
  - push: <yes | no>
  - pr_create: <yes | no>
  - review_comment: <yes | no>

Preflight summary requested:
- Current branch and base branch
- Working tree status
- Remote / GitHub CLI readiness
- Files included and excluded
- Existing PR status, if checked

Execution boundaries:
- Do not commit, push, create PRs, or comment unless the corresponding authorization flag is `yes`.
- Do not modify SSH config, GitHub auth, hooks, repository settings, or unrelated files.
- Do not treat a suggested commit message or PR body as exempt from human review.
- Do not merge the PR.

Expected output:
- Preflight summary
- Proposed commit message and rationale
- PR title and PR body summary or file path
- Exact commands proposed or executed
- PR URL, if created
- Review comment status, if posted
- Unresolved risks and next human action

Stop conditions:
- Current branch is protected/mainline and direct work is not explicitly authorized.
- Working tree contains unexplained or unrelated changes.
- GitHub remote, base branch, or PR scope is unclear.
- `gh` is unavailable or unauthenticated when live PR actions are requested.
- Any requested command would change credentials, SSH config, hooks, repo settings, or unrelated files.
```
