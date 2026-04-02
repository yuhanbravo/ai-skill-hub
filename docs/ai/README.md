# AI Layer

This directory holds execution-facing protocol material for `ai-skill-hub`.

## Ownership

- Status: canonical home for AI-facing rule documents created by the semantic split
- Owns: execution protocol, invocation protocol, discovery routing guidance, and shared execution-shape references
- Does not own: active handoff/status artifacts or human-facing repository explanation

## Contents

- `EXECUTION_PROTOCOL.md`: execution-oriented skill authoring contract mirrored from `skills/SKILL_TEMPLATE.md`
- `INVOCATION_PROTOCOL.md`: unified invocation contract mirrored from `skills/_protocol/skill_invocation.md`
- `DISCOVERY_AND_INVOCATION.md`: AI-facing repository discovery and invocation guidance split out of `AI_USAGE.md`
- `PATTERNS/`: shared execution shapes extracted from project and tool documentation

These files are semantic layer copies intended to make the AI layer explicit without changing existing runtime or adapter entrypoints.
