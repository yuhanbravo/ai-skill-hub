# ai-skill-hub

这是当前机器上的本地 `ai-skill-hub` 仓库，也是一个面向多代理协作的 skill platform，用来集中维护、测试和分发各类 AI skills。

它可以理解为 AI Capability OS 的 skill layer：以 `skills/` 作为 canonical source，通过 adapter、index、tools 和 automation 为不同 AI 入口提供统一的技能发现与分发能力。

## Legacy Alias

- canonical name: `ai-skill-hub`
- legacy name: `codex-skill-hub`
- 消费者侧目录如 `.codex/`、`.codex/skills/`、`.codex/skill-config/` 继续作为兼容入口保留，不因本次仓库内部重命名而强制调整。

## 当前包含的 Skills

- `chatgpt-handoff-pilot`
- `documentation-governance`
- `file-structure-check`
- `financial-data-project-migration`
- `project-takeover`
- `skill-governance`
- `system-takeover`
- `update-project-status`

## 仓库结构（Repository Layout）

- `skills/`：各个 skill 的源码（source）
- `.agents/skills/`：通用 AI 入口层（thin adapter layer）
- `.github/skills/`：GitHub Copilot 兼容入口层（fallback adapter layer）
- `tests/`：仓库级测试区域（repository-level test area）
- `examples/`：仓库级示例（repository-level examples）
- `tools/`：辅助脚本（utility scripts），用于同步、导出等操作
- `SKILLS_INDEX.md`：跨 AI 通用 skill 索引
- `AI_USAGE.md`：跨 AI 使用说明

这个仓库最初是从业务项目中的 `.codex/skills` 同步副本重建出来的。这个背景仅用于解释历史来源；当前默认主名与平台定位均以 `ai-skill-hub` 为准，目标是在不直接改动业务项目的前提下，统一管理 skill 的演进。

## AI 兼容入口（Cross-AI Adapter Layer）

本仓库将 `skills/` 保持为唯一事实源，不在其他入口层复制完整 skill 内容。

- `skills/<skill>/`：canonical source，包含真实 `SKILL.md`、脚本、测试、参考资料
- `.agents/skills/<skill>/SKILL.md`：面向通用 AI 与 legacy adapter discovery 的薄入口
- `.github/skills/<skill>.md`：面向 Copilot 的兼容入口

当前仓库未使用 symlink，而是采用“adapter + index”策略：

- 通过相对路径把入口文件指向 canonical skill
- 通过 `SKILLS_INDEX.md` 提供统一索引
- 通过 `AI_USAGE.md` 说明发现与解析方式

如果某个 AI 只能看到入口层，应继续读取入口文件中给出的 canonical path，再回到 `skills/` 目录读取完整 skill 定义。

## SkillHub Status Template

`ai-skill-hub` 本身就是一个 multi-agent skill platform 项目，它的主要演进对象不是业务功能，而是 skills、adapter layers、invocation contracts、indexes、tests 和 automation tools。

对这类仓库使用 [skills/update-project-status](skills/update-project-status) 时，建议在 `.codex/skill-config/update-project-status.json` 中设置 `template_type=skillhub`，这样状态输出会优先围绕 skill coverage、invocability、governance 和 automation 来组织。

如果目标仓库只是普通应用项目、数据项目或服务项目，则继续使用默认模板即可，不需要切换 `template_type`。

## 同步到非 Git 项目（Sync To Non-Git Project）

使用 [tools/sync_skills_to_nongit_project.ps1](tools/sync_skills_to_nongit_project.ps1) 可以把当前仓库中的 skills 同步到某个项目的 `.codex/skills` 目录。  
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

使用 [tools/export_bundle.ps1](tools/export_bundle.ps1) 可以把当前仓库导出为 `.bundle` 文件，适合做离线备份（offline backup）或跨机器分发。
