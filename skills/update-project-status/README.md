# Update Project Status Skill

## Purpose

`update-project-status` builds a status document from recent Git commits plus optional external task sources. It can also publish that status through configurable sync targets.

## Running The Script

```powershell
python .codex/skills/update-project-status/scripts/update_project_status.py --root <project-root>
```

```powershell
python .codex/skills/update-project-status/scripts/update_project_status.py --root <project-root> --dry-run
```

Optional flags:
- `--config <path>`
- `--status-file <path>`
- `--log-file <path>`
- `--shared-doc <path>`
- `--limit <n>`
- `--dry-run`

Hook installation:

```powershell
python .codex/skills/update-project-status/scripts/install_post_commit_hook.py --root <project-root>
```

```powershell
python .codex/skills/update-project-status/scripts/install_post_commit_hook.py --root <project-root> --dry-run
```

## Task Sources

`task_sources` entries can be:
- `file_glob`
- `jira_json`
- `trello_json`
- `command`

This lets the status report combine Git history with exported or CLI-fetched work items from Jira, Trello, or other tooling.

## Sync Targets

`sync_targets` entries can be:
- `local_copy`
- `command`
- `confluence_rest`
- `google_docs_rest`

Remote targets require authentication through environment variables referenced in the config.

## Side Effects

Without `--dry-run`, the script writes:
- the configured status file
- the configured status log
- any configured sync targets

The hook installer writes `.git/hooks/post-commit`.

## Cross-Project Notes

- The hook script now embeds the resolved Python executable and status-script path instead of assuming a fixed repository layout.
- Use `command` task sources or sync targets when your team already has a preferred CLI or wrapper for Jira, Trello, Confluence, or Google Workspace.
