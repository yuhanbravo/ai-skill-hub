# audit_reseed_targets.ps1

`tools/audit_reseed_targets.ps1` 是 rollout 前的预审计工具。
它只读扫描目标项目的 skill system 状态，帮助我们先判断项目是否适合做 clean re-seed，再决定是否进入 `DryRun` 或正式 re-seed。

它不是分发工具，不会调用正式 sync，不会修改项目目录，也不会向项目内写入任何内容。

## 支持的输入方式

按根目录扫描一层或多层候选项目：

```powershell
.\tools\audit_reseed_targets.ps1 -RootPath "D:\BaiduSyncdisk\Python_Lib" -RecurseDepth 1
```

显式传项目列表：

```powershell
.\tools\audit_reseed_targets.ps1 -ProjectPaths "D:\Work\ProjectA","D:\Work\ProjectB"
```

从文本文件读取项目列表：

```powershell
.\tools\audit_reseed_targets.ps1 -ProjectsFile ".\projects.txt" -Format csv -OutputPath ".\reports"
```

## 主要参数

- `-RootPath`: 扫描根目录，默认把深度 `1..RecurseDepth` 的子目录都当作候选项目。
- `-ProjectPaths`: 显式指定项目路径数组。
- `-ProjectsFile`: 从文本文件读取项目路径，支持空行和 `#` 注释行。
- `-OutputPath`: 导出目录或导出文件路径。
- `-Format`: `table | csv | json | md`，默认 `table`。
- `-RecurseDepth`: 根目录扫描深度，默认 `1`。
- `-IncludeHidden`: 根目录扫描时包含隐藏目录。
- `-VerboseReport`: 控制台表格增加 `SourcePath` 和 `Notes` 等详细列。

## 输出字段

每个项目至少输出以下字段：

- `ProjectPath`
- `Exists`
- `HasCodexSkills`
- `HasAgentsSkills`
- `HasGithubSkills`
- `HasSkillConfig`
- `IsHubRepository`
- `HubSignals`
- `SkillConfigFiles`
- `HasBackupDir`
- `BackupDirNames`
- `HasSkillsetVersion`
- `SourceHub`
- `SourcePath`
- `SeedStatus`
- `RiskLevel`
- `RecommendedAction`
- `Notes`

另外还会补充：

- `SyncedAt`
- `RobocopyExitCode`

## 审计状态分类

- `already_seeded`
  条件：`.codex/skills` 存在、`_skillset_version.txt` 存在、`source_hub=ai-skill-hub`、且 `.codex/skill-config` 存在。
  建议：`no_action`

- `ready_for_reseed`
  条件：存在 skill 分发痕迹、存在 `.codex/skill-config`、不属于 `already_seeded`、且没有高风险灰区。
  建议：`dryrun_then_reseed`

- `risky_manual_review`
  条件：发现 `_backup_before_reset` / backup / archive 等灰区，或发现难以确认来源的自定义分发结构。
  建议：`manual_review_backup` 或 `inspect_custom_distribution`

- `missing_config`
  条件：存在 skill 痕迹，但缺少 `.codex/skill-config`。
  建议：`restore_or_create_skill_config`

- `no_skill_structure`
  条件：`.codex` / `.agents` / `.github` 没有 skill 痕迹。
  建议：`verify_project_first`

- `inaccessible`
  条件：项目不存在、不可访问、或单项目扫描异常。
  建议：`inspect_path_access`

- `hub_repository`
  条件：命中保守的 hub self-detection 信号组合，例如 `skills/`、`tools/sync_skills_to_nongit_project.ps1`、`VERSION`、`README.md`、`docs/status/skill-hub-status.md` 中的多个强信号。
  建议：`skip_hub_repo`

## Hub Self-Detection

审计工具会对 `ai-skill-hub` 这类 skill hub 本体做保守识别。
如果同时命中 `skills/` 和 `tools/sync_skills_to_nongit_project.ps1`，并且总信号数达到至少 3 个，就会输出 `hub_repository`，而不是把它当作普通 clean re-seed 目标。

命中该规则时：

- `SeedStatus = hub_repository`
- `RecommendedAction = skip_hub_repo`
- `IsHubRepository = true`

## 版本文件识别

如果存在 `.codex/skills/_skillset_version.txt`，脚本会尽量解析这些字段：

- `source_hub`
- `source_path`
- `synced_at`
- `robocopy_exit_code`

其中：

- `source_hub=ai-skill-hub` 是 `already_seeded` 的强证据。
- `source_hub=codex-skill-hub` 可作为 `ready_for_reseed` 的证据。
- 有大量 skill 内容但缺失 `_skillset_version.txt` 时，会提升为 `risky_manual_review`。

## 报告示例

```text
Re-seed audit summary
GeneratedAt: 2026-04-01T11:00:00+08:00
TotalProjects: 3
StatusSummary: already_seeded=1, ready_for_reseed=1, risky_manual_review=1

ProjectPath                       SeedStatus           RiskLevel RecommendedAction     HasSkillConfig HasBackupDir SourceHub
-----------                       ----------           --------- -----------------     -------------- ------------ ---------
D:\Work\ProjectA                  already_seeded       low       no_action            True           False        ai-skill-hub
D:\Work\ProjectB                  ready_for_reseed     low       dryrun_then_reseed   True           False        codex-skill-hub
D:\Work\ProjectC                  risky_manual_review  high      manual_review_backup True           True
```

## 与 clean re-seed 的衔接方式

推荐顺序是：

1. 先运行 `audit_reseed_targets.ps1` 做批量预审计。
2. 对 `ready_for_reseed` 项目优先做 `DryRun`。
3. 对 `risky_manual_review` 或 `missing_config` 项目先人工处理灰区和配置问题。
4. 审计通过后，再进入 clean re-seed 流程。
