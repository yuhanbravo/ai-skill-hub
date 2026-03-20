# codex-skill-hub

Local rebuilt skill hub on this machine.

## Included skills

- documentation-governance
- file-structure-check
- project-takeover
- update-project-status

## Layout

- skills/ - source of each skill
- tests/ - repository-level test area
- examples/ - repository-level examples

This repository was rebuilt from the synced project copy under `.codex/skills` without modifying the business project.

## Sync To Non-Git Project

Use `tools/sync_skills_to_nongit_project.ps1` to sync hub skills into a project workspace that does not use Git for its `.codex/skills` copy.

```powershell
pwsh -File .\tools\sync_skills_to_nongit_project.ps1 `
  -SkillHubPath D:\dev\codex-skill-hub `
  -ProjectPath D:\dev\some-project
```

```powershell
pwsh -File .\tools\sync_skills_to_nongit_project.ps1 `
  -SkillHubPath D:\dev\codex-skill-hub `
  -ProjectPath D:\dev\some-project `
  -SkillName file-structure-check `
  -DryRun
```
