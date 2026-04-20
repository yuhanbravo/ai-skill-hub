# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use update-project-status for this task.

task_description:
- Refresh the project status report from Git-first signals plus current workspace/task sources.

constraints:
- Do not install hooks unless explicitly requested.
- Treat external sync as opt-in.

expected_output:
- Updated status summary
- Source mode and signal-source breakdown (Git / workspace / task / inferred)
- Risk and next-step summary
- Optional sync decision

context_files:
- .git/
- README.md
- status config files
- docs/**/*
```

### Output Example

```text
execution_plan:
- Detect source_mode (git/workspace/hybrid) and load available signals.
- Build the status summary and log entry.
- Decide whether any sync action is authorized.

changes_made:
- Generated a refreshed status summary.
- Did not install post-commit hook.

files_touched:
- .git/
- status markdown output
- status log output

risks:
- Missing external task sources may reduce summary completeness.
```
