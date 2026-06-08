# First Executable Migration Task Package Template

Template purpose: define the structure of a first bounded migration task package.

Template boundary:
- This is a generated artifact structure, not an execution prompt.
- It does not authorize migration work by itself.
- It must be instantiated from a prior migration assessment or planning note.
- Keep all project-specific facts as placeholders until supplied by the operator.

```md
# Task Package: <migration_step_name>

## Scope
- This round only does: <single bounded step>
- This round does not do: <explicit exclusions>
- Advisory source: <assessment report / migration planning note>

## Repository / Project Path
- <repository-or-project-path>

## Files to Inspect
- <paths>

## Files Allowed to Change
- <paths>

## Files Not Allowed to Change
- <paths>

## Migration Readiness Class
- <inventory_only | wrapper_first | module_extract_ready | src_package_ready>
- Rationale: <why this class was chosen>

## Desktop Script vs Package Decision
- Recommended path: <keep desktop script | compatibility wrapper | extract reusable module | move toward src layout | add CLI/tests | defer API/service>
- Deferred path(s): <what is intentionally not happening now>

## Current Constraints
- Runtime constraints: <Excel / Wind / network drive / CWD / scheduler / database / report-output constraints>
- Data constraints: <sample-data / no-real-data / schema / privacy constraints>
- Operational constraints: <manual workflow / compatibility / rollback constraints>

## Coupling Matrix
- Excel coupling: <0-3> (evidence: <path/line>)
- Wind/external coupling: <0-3> (evidence: <path/line>)
- Local absolute path coupling: <0-3> (evidence: <path/line>)
- Network drive coupling: <0-3> (evidence: <path/line>)
- CWD coupling: <0-3> (evidence: <path/line>)
- Manual desktop coupling: <0-3> (evidence: <path/line>)
- Database coupling: <0-3> (evidence: <path/line>)
- Scheduler/batch coupling: <0-3> (evidence: <path/line>)
- Report output coupling: <0-3> (evidence: <path/line>)

## Target Planning Profile
- Primary profile: <script_wrapper_profile | batch_pipeline_profile | data_service_profile | analytics_report_profile>
- Fallback profile: <optional>
- Note: planning profile only; not a mandatory folder template.

## Legacy Wrapper Strategy
- Old entrypoint preservation: <path / behavior / caller compatibility>
- First-step extraction boundary: <smallest safe boundary>
- Compatibility window: <operator-confirmed window>
- Rollback trigger: <trigger>
- Wrapper retirement condition: <condition>

## Minimal Test Safety Net
- Import smoke test: <command-or-check>
- Sample input/output test: <command-or-check>
- Schema/column test: <command-or-check>
- Idempotency or duplicate-write test, if relevant: <command-or-check>
- Report artifact existence check, if relevant: <command-or-check>
- No-real-data / sample-data-first assumption: <assumption>

## Proposed First Step
- <wrapper creation | function extraction | inventory freeze>

## Validation Commands
- <command 1>
- <command 2>

## Stop Conditions
- <condition that stops implementation before changes>
- <condition that prevents changing allowed/forbidden files>

## Rollback Notes
- Trigger: <trigger>
- Rollback action: <action>

## Execution Report Requirement
The implementer must output a structured execution report covering:
- Scope Restatement
- Files Changed
- What Changed / What Not Changed
- Validation Performed
- Boundary Checks
- Risks and Assumptions
- Deferred Follow-ups
```
