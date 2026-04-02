# Documentation Architecture

This file is the one-page navigation guide for the AI / Human / Bridge documentation split.

## Why Three Layers Exist

- `docs/ai/` keeps execution-facing rules explicit so AI agents know where canonical protocol guidance lives.
- `docs/human/` keeps explanation-oriented material explicit so maintainers can orient quickly without reading execution contracts first.
- `docs/bridge/` keeps handoff, status, and structured exchange artifacts visible in one place without replacing the active source paths that already exist.

## Where AI Should Look

- Execution section rules: [docs/ai/EXECUTION_PROTOCOL.md](ai/EXECUTION_PROTOCOL.md)
- Skill invocation contract: [docs/ai/INVOCATION_PROTOCOL.md](ai/INVOCATION_PROTOCOL.md)
- Discovery and entrypoint rules: [docs/ai/DISCOVERY_AND_INVOCATION.md](ai/DISCOVERY_AND_INVOCATION.md)
- Compatibility quick entry: [AI_USAGE.md](../AI_USAGE.md)

## Where Humans Should Look

- Repository reading guide: [docs/human/REPOSITORY_CONSUMPTION_GUIDE.md](human/REPOSITORY_CONSUMPTION_GUIDE.md)
- Repository overview: [docs/human/REPOSITORY_OVERVIEW.md](human/REPOSITORY_OVERVIEW.md)
- Lifecycle and phase references: [docs/human/PROJECT_LIFECYCLE.md](human/PROJECT_LIFECYCLE.md), [docs/human/PHASE_MODEL.md](human/PHASE_MODEL.md)

## Where Handoff And Exchange Assets Live

- Active handoff source: [docs/HANDOFF.md](HANDOFF.md)
- Active status source: [docs/status/skill-hub-status.md](status/skill-hub-status.md)
- Bridge-facing copies and mirrors: [docs/bridge/README.md](bridge/README.md)
- Skill-local task package and execution report templates:
  [skills/chatgpt-handoff-pilot/templates/TASK_PACKAGE_TEMPLATE.md](../skills/chatgpt-handoff-pilot/templates/TASK_PACKAGE_TEMPLATE.md),
  [skills/chatgpt-handoff-pilot/templates/EXECUTION_REPORT_TEMPLATE.md](../skills/chatgpt-handoff-pilot/templates/EXECUTION_REPORT_TEMPLATE.md)

## Compatibility Entries

- Quick AI compatibility entry: [AI_USAGE.md](../AI_USAGE.md)
- Root cross-AI index: [SKILLS_INDEX.md](../SKILLS_INDEX.md)

## Active Source vs Mirror

- Active sources stay in their existing paths until a later migration explicitly changes ownership.
- Bridge mirrors and bridge-facing copies exist for continuity and navigation, not to silently replace active sources.
- If active source and mirror diverge, treat the active source as authoritative in this phase.
