---
name: update-project-status
description: Generate and maintain a project status document from recent Git history plus optional task sources such as markdown task boards, Jira exports, Trello exports, or custom commands, then sync the result to configurable targets. Use when Codex needs to summarize recent work, create a status report, update docs/status.md, prepare handoff status notes, or respond to requests like "update project status", "summarize recent changes", or "publish a status report".
---

# Update Project Status

Use this skill to turn Git activity and external task sources into a portable status report, with optional sync targets for local copies, commands, Confluence, or Google Docs.

## Trigger Keywords

- update project status
- status report
- summarize recent changes
- publish status
- jira status sync
- trello status sync
- project update log

## Side Effects

- Default mode writes the configured status markdown file and log file.
- Sync targets can copy or publish the generated content after the write step.
- `install_post_commit_hook.py` writes a Git hook file.
- `--dry-run` previews output and sync activity without writing files.

## Workflow

1. Load config and inspect recent Git history when available.
2. Collect extra tasks from configured file globs, Jira exports, Trello exports, or command sources.
3. Build the status document and append a status log entry.
4. Optionally sync the generated content to configured targets.
5. If needed, install a post-commit hook that points at the actual script path and Python executable.

## Commands

```powershell
python .codex/skills/update-project-status/scripts/update_project_status.py --root <project-root>
```

```powershell
python .codex/skills/update-project-status/scripts/update_project_status.py --root <project-root> --dry-run
```

```powershell
python .codex/skills/update-project-status/scripts/install_post_commit_hook.py --root <project-root>
```

Useful flags:

- `--config <path>`
- `--status-file <path>`
- `--log-file <path>`
- `--shared-doc <path>` for legacy local-copy sync
- `--limit <n>`
- `--dry-run`

## Prompt Template

Use or adapt this request when invoking the skill:

```text
Use the `update-project-status` skill for this repository and refresh the status report.

Project root: <project-root>
Primary goal: <status refresh | recent change summary | publish status>

Please:
- inspect recent Git history
- pull in configured task sources when available
- update the status markdown and status log
- note key progress, open risks, and pending work

Options:
- config path: <path-or-none>
- status file override: <path-or-none>
- log file override: <path-or-none>
- shared doc override: <path-or-none>
- commit limit: <n-or-default>
- dry run: <yes-or-no>
- install post-commit hook: <yes-or-no>
```

## Config Notes

- Default config lives in `references/default_status_config.json`.
- Projects can override it with `.codex/skill-config/update-project-status.json` or `--config`.
- `task_sources` supports `file_glob`, `jira_json`, `trello_json`, and `command` sources.
- `sync_targets` supports `local_copy`, `command`, `confluence_rest`, and `google_docs_rest`.
- Confluence and Google Docs sync rely on bearer or basic auth tokens supplied through environment variables.

## Safety Rules

- Use `--dry-run` before enabling network sync targets.
- Treat commit classification as heuristic and review the generated status text before publishing.
- Keep authentication material in environment variables or project secrets, not in the committed config file.
