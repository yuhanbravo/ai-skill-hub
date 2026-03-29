---
name: project-takeover
description: "Adapter entry for repository takeover packets, onboarding summaries, and unfamiliar-repo scanning. Canonical source is in skills/project-takeover."
metadata:
  triggers:
    - prepare a repository takeover packet
    - onboard a new maintainer or AI agent
    - scan docs config and task sources
    - generate an onboarding summary for a project
    - analyze an unfamiliar repository before maintenance
  side_effects:
    - read_only
    - write_files
  canonical_path: ../../../skills/project-takeover
  adapter_type: thin-wrapper
---

# project-takeover

- Canonical skill directory: `../../../skills/project-takeover`
- Canonical skill definition: `../../../skills/project-takeover/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.
