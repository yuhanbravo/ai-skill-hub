# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use financial-data-project-migration for this task.

task_description:
- Assess whether this financial-data Python repository is ready for structure migration.

constraints:
- Do not move files or create a src/ layout.
- Keep recommendations conservative if desktop Excel or Wind coupling is detected.

expected_output:
- Migration advisory
- Risk summary
- Minimal next-step todo

context_files:
- *.py
- *.xlsx
- README.md
```

### Output Example

```text
execution_plan:
- Scan Python scripts, Excel assets, and document entrypoints.
- Classify project type and migration stage.
- Produce a conservative migration advisory.

changes_made:
- No project files were modified.
- Produced a migration readiness assessment.

files_touched:
- README.md
- root Python scripts
- Excel asset inventory

risks:
- Wind/Desktop coupling may block any immediate package-first migration.
```
