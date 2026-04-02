# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use file-structure-check for this task.

task_description:
- Validate the repository layout against the data-project profile.

constraints:
- Do not move files or create directories.
- Report suggested fixes separately from detected issues.

expected_output:
- Structure audit report
- Missing paths list
- Misplaced files list

context_files:
- skills/
- tests/
- docs/
```

### Output Example

```text
execution_plan:
- Resolve the active profile and strictness.
- Scan the repository tree.
- Report missing paths and misplaced files.

changes_made:
- No files were modified.
- Produced a structure audit summary.

files_touched:
- skills/
- tests/
- docs/

risks:
- Some directories may intentionally deviate from the default profile and need local confirmation.
```
