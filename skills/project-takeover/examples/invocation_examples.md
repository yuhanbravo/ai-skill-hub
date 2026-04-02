# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use project-takeover for this task.

task_description:
- Prepare a takeover packet for this unfamiliar repository.

constraints:
- Prefer project-local configuration over shared assumptions.
- Do not run install or safe-fix actions unless explicitly authorized.

expected_output:
- Takeover report
- Onboarding summary
- Risk list and next steps

context_files:
- README.md
- docs/
- tests/
```

### Output Example

```text
execution_plan:
- Scan the repository environment, docs, and task sources.
- Build a takeover understanding summary.
- Produce takeover packet outputs.

changes_made:
- Generated takeover-oriented findings and onboarding summary.
- Did not execute install or safe-fix actions.

files_touched:
- README.md
- docs/
- tests/

risks:
- Some project-local task sources may still require manual confirmation.
```
