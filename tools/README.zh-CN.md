# Tools 简短中文说明

这个目录主要放一些本地 PowerShell 工具，用来做 skill hub 的导出、导入和同步。下面按“什么时候用”来快速说明，便于直接调用。

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

常用参数：
- `-RepoPath`：要导出的仓库路径
- `-OutputDir`：bundle 输出目录

注意：
- 要求仓库工作区干净，否则会拒绝导出。

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

常用参数：
- `-RepoPath`：目标仓库路径
- `-BundlePath`：bundle 文件路径

注意：
- 如果目标仓库已存在，必须是干净工作区。

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
  -SkillHubPath 'D:\dev\codex-skill-hub' `
  -SkillName 'chatgpt-handoff-pilot'
```

常用参数：
- `-ProjectPath`：真实项目路径
- `-SkillHubPath`：当前 hub 路径
- `-SkillName`：要同步的 skill 名称
- `-DryRun`：只预览不复制
- `-CreateIfMissing`：hub 中缺失时自动创建

注意：
- 来源固定为项目下的 `.codex\skills\<SkillName>`。

## sync_skills_to_nongit_project.ps1

用途：
- 把 hub 中的全部或单个 skill 下发到一个非 Git 项目的 `.codex\skills`。

适合什么时候用：
- 想把最新 skill 集合推送到业务项目
- 目标项目只需要同步文件，不需要完整 Git 仓库

最短调用：

```powershell
.\tools\sync_skills_to_nongit_project.ps1 `
  -SkillHubPath 'D:\dev\codex-skill-hub' `
  -ProjectPath 'D:\my-project'
```

同步单个 skill：

```powershell
.\tools\sync_skills_to_nongit_project.ps1 `
  -SkillHubPath 'D:\dev\codex-skill-hub' `
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
- 同步后会在目标项目写入一个 `_skillset_version.txt` 元数据文件。

## 使用建议

- 想“备份或打包整个 hub”，用 `export_bundle.ps1`。
- 想“从 bundle 恢复或更新 hub”，用 `import_bundle.ps1`。
- 想“把项目里改好的单个 skill 回收到 hub”，用 `sync_skill_from_project_to_hub.ps1`。
- 想“把 hub 的 skill 下发到业务项目”，用 `sync_skills_to_nongit_project.ps1`。
