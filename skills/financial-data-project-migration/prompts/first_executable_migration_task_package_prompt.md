# First Executable Migration Task Package Prompt

Purpose: copyable invocation prompt for generating the first bounded migration task package after a financial-data migration assessment.

Canonical owner: `financial-data-project-migration`
Generated artifact structure: `../templates/FIRST_EXECUTABLE_MIGRATION_TASK_PACKAGE_TEMPLATE.md`

Boundary:
- This prompt requests a task package only; it does not execute migration work.
- Keep assessment and execution separate.
- Do not invent a new migration framework or change readiness class semantics.
- Keep all downstream project facts as placeholders unless supplied by the operator.

```text
Please use `financial-data-project-migration` to generate the first executable bounded migration task package.

Use the template at:
- skills/financial-data-project-migration/templates/FIRST_EXECUTABLE_MIGRATION_TASK_PACKAGE_TEMPLATE.md

Required inputs:
- Repository / project path: <project-root>
- Migration target profile: <script_wrapper_profile | batch_pipeline_profile | data_service_profile | analytics_report_profile>
- Migration readiness class: <inventory_only | wrapper_first | module_extract_ready | src_package_ready>
- Current constraints:
  - Runtime constraints: <Excel / Wind / network drive / CWD / scheduler / database / report-output constraints>
  - Data constraints: <sample-data / no-real-data / schema / privacy constraints>
  - Operational constraints: <manual workflow / compatibility / rollback constraints>
- Allowed files:
  - <paths allowed to change>
- Forbidden files:
  - <paths not allowed to change>
- Validation commands:
  - <command 1>
  - <command 2>
- Stop conditions:
  - <condition 1>
  - <condition 2>
- Advisory source: <assessment report / migration planning note>

Task package requirements:
- Instantiate exactly one bounded migration step.
- Preserve old entrypoints unless explicit authorization says otherwise.
- Separate files to inspect from files allowed to change.
- Include files not allowed to change.
- Include readiness class rationale without changing class semantics.
- Include target planning profile as planning-only, not a mandatory folder layout.
- Include minimal test safety net and rollback notes.
- Include execution report requirements for the future implementer.

Expected output:
- A first executable migration task package using the template structure.
- A short note listing assumptions and any missing operator inputs.

Stop conditions:
- Required inputs are missing or contradictory.
- The requested task would require changing forbidden files.
- The requested task would require deleting legacy entrypoints or changing production behavior without authorization.
- The task package would become a broad migration plan instead of one bounded step.
- The prompt would need to invent project facts, real data paths, credentials, or validation evidence.
```
