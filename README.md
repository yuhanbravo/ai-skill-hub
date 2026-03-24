# codex-skill-hub

这是当前机器上的本地 `skill hub` 仓库，用来集中维护、测试和分发各类 `Codex skills`。

## 当前包含的 Skills

- `chatgpt-handoff-pilot`
- `documentation-governance`
- `file-structure-check`
- `financial-data-project-migration`
- `project-takeover`
- `skill-governance`
- `update-project-status`

## 仓库结构（Repository Layout）

- `skills/`：各个 skill 的源码（source）
- `tests/`：仓库级测试区域（repository-level test area）
- `examples/`：仓库级示例（repository-level examples）
- `tools/`：辅助脚本（utility scripts），用于同步、导出等操作

这个仓库最初是从业务项目中的 `.codex/skills` 同步副本重建出来的，目的是在不直接改动业务项目的前提下，统一管理 skill 的演进。

## 同步到非 Git 项目（Sync To Non-Git Project）

使用 [tools/sync_skills_to_nongit_project.ps1](/d:/dev/codex-skill-hub/tools/sync_skills_to_nongit_project.ps1) 可以把当前仓库中的 skills 同步到某个项目的 `.codex/skills` 目录。  
这个脚本默认会以“当前仓库根目录”作为 `skill hub` 源路径（source path），因此通常只需要传入目标项目路径（`ProjectPath`）。

```powershell
pwsh -File .\tools\sync_skills_to_nongit_project.ps1 `
  -ProjectPath D:\dev\some-project
```

```powershell
pwsh -File .\tools\sync_skills_to_nongit_project.ps1 `
  -ProjectPath D:\dev\some-project `
  -SkillName file-structure-check `
  -DryRun
```

- 不传 `-SkillName`：同步全部 skills
- 传入 `-SkillName`：只同步单个 skill
- 加上 `-DryRun`：只预览 `robocopy` 结果，不实际写入

## 导出仓库 Bundle（Export Bundle）

使用 [tools/export_bundle.ps1](/d:/dev/codex-skill-hub/tools/export_bundle.ps1) 可以把当前仓库导出为 `.bundle` 文件，适合做离线备份（offline backup）或跨机器分发。
