This skill can read status signals from multiple sources.

Supported task-source types:
- `file_glob`: read checklist-style lines from local markdown or text files
- `jira_json`: parse exported Jira issue JSON
- `trello_json`: parse exported Trello card JSON
- `command`: execute a local CLI and parse either line output or JSON output

Supported sync target types:
- `local_copy`
- `command`
- `confluence_rest`
- `google_docs_rest`

Prefer `--dry-run` before enabling remote sync targets. Keep tokens in environment variables such as `CONFLUENCE_TOKEN` or `GOOGLE_DOCS_TOKEN`.
