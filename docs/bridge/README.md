# Bridge Layer

This directory holds handoff, status, and structured exchange artifacts that bridge human intent and AI execution.

## Role

- Status: canonical bridge entry for the three-layer documentation split
- Owns: bridge-layer navigation, active-source vs mirror definitions, and handoff continuity notes
- Does not own: active updates to handoff, status, root skill index, or canonical skill templates

## Asset Status

| Asset | Active source | Role in bridge layer |
| --- | --- | --- |
| `HANDOFF.md` | `docs/HANDOFF.md` | semantic mirror |
| `status/skill-hub-status.md` | `docs/status/skill-hub-status.md` | semantic mirror |
| `SKILLS_INDEX.md` | `SKILLS_INDEX.md` | bridge-facing copy |
| `templates/EXECUTION_REPORT_TEMPLATE.md` | `skills/chatgpt-handoff-pilot/templates/EXECUTION_REPORT_TEMPLATE.md` | bridge-facing copy |
| `templates/TASK_PACKAGE_TEMPLATE.md` | `skills/chatgpt-handoff-pilot/templates/TASK_PACKAGE_TEMPLATE.md` | bridge-facing copy |

## Contents

- `HANDOFF.md`: bridge-facing mirror of the active handoff artifact
- `status/skill-hub-status.md`: bridge-facing mirror of the active status artifact
- `templates/EXECUTION_REPORT_TEMPLATE.md`: structured execution report template
- `templates/TASK_PACKAGE_TEMPLATE.md`: structured task-package template
- `SKILLS_INDEX.md`: bridge-facing skill index for discovery and handoff scenarios

The active runtime paths remain unchanged. These copies make the bridge layer explicit without altering existing skill behavior.

## Freeze Notes

- Active updates continue to happen in the original active-source paths listed above.
- Bridge files remain prose-first Markdown assets and are not upgraded into a schema layer in this phase.
- If active source and bridge copy drift, the active source wins unless a later migration explicitly changes ownership.
