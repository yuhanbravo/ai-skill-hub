# Tools 简短中文说明

这个目录主要放一些本地 PowerShell 工具，用来做 skill hub 的导出、导入和同步。下面按“什么时候用”来快速说明，便于直接调用。

## 当前默认来源

- canonical name：`ai-skill-hub`
- 默认本地仓库路径示例：`D:\dev\ai-skill-hub`
- 项目消费侧仍保留 `.codex/`、`.codex/skills/` 等兼容入口；这里说明的是当前 hub 默认来源，不改项目消费目录结构。

## export_bundle.ps1

用途：

- 把当前 skill hub Git 仓库导出成 `.bundle` 文件。

适合什么时候用：

- 需要离线备份仓库
- 需要把仓库打包后同步到另一台机器

最短调用：

```powershell
.\tools\export_bundle.ps1
```

显式传入提交日志：

```powershell
.\tools\export_bundle.ps1 `
  -CommitMessage 'chore(bundle): export latest ai-skill-hub snapshot'
```

常用参数：

- `-RepoPath`：要导出的仓库路径
- `-OutputDir`：bundle 输出目录
- `-CommitMessage`：工作区不干净时可直接传入提交日志，避免交互输入

注意：

- 工作区不干净时，脚本会要求输入提交日志，随后自动提交并导出。
- 不传 `-RepoPath` 时，默认使用当前脚本所在仓库根目录；当前 canonical 本地路径通常为 `D:\dev\ai-skill-hub`。
- 默认会输出到 `D:\BaiduSyncdisk\Python_Lib\Git_Bundle`。
- 导出的默认 bundle 文件名已切换为 `ai-skill-hub_latest.bundle` 和 `ai-skill-hub_<date>_v1.bundle`。

## import_bundle.ps1

用途：

- 从 `.bundle` 文件恢复或更新本地 skill hub 仓库。

适合什么时候用：

- 新机器初始化 skill hub
- 用 bundle 更新已有本地仓库

最短调用：

```powershell
.\tools\import_bundle.ps1
```

显式指定 canonical 仓库与 bundle：

```powershell
.\tools\import_bundle.ps1 `
  -RepoPath 'D:\dev\ai-skill-hub' `
  -BundlePath 'D:\backup\ai-skill-hub_latest.bundle'
```

常用参数：

- `-RepoPath`：目标仓库路径
- `-BundlePath`：bundle 文件路径

注意：

- 如果目标仓库已存在，必须是干净工作区。
- 不传 `-RepoPath` 时，默认使用当前脚本所在仓库根目录；当前 canonical 本地路径通常为 `D:\dev\ai-skill-hub`。
- 默认从 `D:\BaiduSyncdisk\Python_Lib\Git_Bundle\ai-skill-hub_latest.bundle` 读取 bundle。

## sync_skill_from_project_to_hub.ps1

用途：

- 把真实项目里的单个 skill 同步回当前 hub。

适合什么时候用：

- 你在业务项目里试跑并修改了 skill
- 想把某个 skill 的改动回收进母库

最短调用：

```powershell
.\tools\sync_skill_from_project_to_hub.ps1 `
  -ProjectPath 'D:\my-project' `
  -SkillHubPath 'D:\dev\ai-skill-hub' `
  -SkillName 'chatgpt-handoff-pilot'
```

常用参数：

- `-ProjectPath`：真实项目路径
- `-SkillHubPath`：当前 hub 路径
- `-SkillName`：要同步的 skill 名称
- `-DryRun`：只预览不复制
- `-CreateIfMissing`：hub 中缺失时自动创建

注意：

- 来源固定为项目下的 `.codex\skills\<SkillName>`，该入口继续作为兼容消费入口保留。

## sync_skills_to_nongit_project.ps1

用途：

- 把 hub 中的全部或单个 skill 下发到一个非 Git 项目的 `.codex\skills`。

适合什么时候用：

- 想把最新 skill 集合推送到业务项目
- 目标项目只需要同步文件，不需要完整 Git 仓库

最短调用：

```powershell
.\tools\sync_skills_to_nongit_project.ps1 `
  -SkillHubPath 'D:\dev\ai-skill-hub' `
  -ProjectPath 'D:\my-project'
```

同步单个 skill：

```powershell
.\tools\sync_skills_to_nongit_project.ps1 `
  -SkillHubPath 'D:\dev\ai-skill-hub' `
  -ProjectPath 'D:\my-project' `
  -SkillName 'project-takeover' `
  -DryRun
```

常用参数：

- `-SkillHubPath`：hub 路径
- `-ProjectPath`：目标项目路径
- `-SkillName`：可选，只同步一个 skill
- `-DryRun`：只预览不同步

注意：

- 默认使用镜像同步思路，建议第一次先 `-DryRun`。
- 项目消费侧目录仍固定写入 `.codex\skills`，不因 hub canonical 名称切换而改名。
- 同步后会在目标项目写入一个 `_skillset_version.txt` 元数据文件。
- 全量同步时会同步 canonical skill 目录与 `_protocol/`，不会再把 `skills/` 根下的说明文件和模板文件一起下发。

## generate_skill_metadata.py

用途：

- 从 canonical `skills/` 生成 `skills_index.json`，并刷新 `.agents/skills/*.md` flat summaries。

适合什么时候用：

- 你修改了某个 `SKILL.md` 的 metadata 或 Invocation
- 想重新生成机器可读索引和 flat discovery 文件

最短调用：

```powershell
python .\tools\generate_skill_metadata.py
```

注意：

- 脚本始终以当前仓库根目录作为 `ROOT`，生成仓库根下的 `skills_index.json` 与 `.agents/skills/*.md`，不会改动生成物结构。

## skill_router.py

用途：

- 根据 `task_description` 自动匹配最合适的 skill，并给出置信度和原因。

最短调用：

```powershell
python .\tools\skill_router.py "整理技能索引并检查文档治理"
```

## skill_pipeline.py

用途：

- 将复合任务拆成子任务，并顺序匹配多个 skill。

最短调用：

```powershell
python .\tools\skill_pipeline.py "接管仓库并更新状态"
```

## 使用建议

- 想“备份或打包整个 hub”，用 `export_bundle.ps1`。
- 想“从 bundle 恢复或更新 hub”，用 `import_bundle.ps1`。
- 想“把项目里改好的单个 skill 回收到 hub”，用 `sync_skill_from_project_to_hub.ps1`。
- 想“把 hub 的 skill 下发到业务项目”，用 `sync_skills_to_nongit_project.ps1`。
