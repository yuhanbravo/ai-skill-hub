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

### Readiness Class Example

```text
Use financial-data-project-migration for a readiness-class migration advisory.

Project root: <project-root>
Readiness class candidate: <inventory_only | wrapper_first | module_extract_ready | src_package_ready>
Constraints: <runtime-coupling-summary>
Allowed output: advisory only

Expected output:
- selected readiness class
- rationale and evidence pointers
- conservative next safe step
- explicitly deferred migration paths
```

### Target Profile Example

```text
Use financial-data-project-migration to choose a target planning profile.

Project root: <project-root>
Target profile candidate: <script_wrapper_profile | batch_pipeline_profile | data_service_profile | analytics_report_profile>
Current constraints: <Excel/Wind/network/CWD/scheduler/database/report-output constraints>
No file moves authorized: <yes | no>

Expected output:
- primary target planning profile
- fallback profile, if useful
- why the profile is planning-only
- first safe step and risk boundary
```

### First Executable Migration Task Package Example

```text
Use financial-data-project-migration to generate the first executable bounded migration task package.
Prompt asset: skills/financial-data-project-migration/prompts/first_executable_migration_task_package_prompt.md
Template asset: skills/financial-data-project-migration/templates/FIRST_EXECUTABLE_MIGRATION_TASK_PACKAGE_TEMPLATE.md

Required inputs:
- Repository / project path: <project-root>
- Migration target profile: <target-profile>
- Migration readiness class: <readiness-class>
- Current constraints: <constraints>
- Allowed files: <allowed-paths>
- Forbidden files: <forbidden-paths>
- Validation commands: <commands>
- Stop conditions: <stop-conditions>

Expected output:
- one bounded migration task package
- assumptions and missing operator inputs
- validation and rollback placeholders
```
