# Adapter Governance

## 设计定位

Adapter Governance 是 distribution 的补充层，用来检查项目内 adapter drift，而不是参与 skill 生成或同步。

检查的基准层是项目内的 `.codex/skills/`，adapter 层是项目内的 `.agents/skills/` 与 `.github/skills/`。

目标只有一件事：发现不一致并报告，不自动修复。

## 使用方式

在目标项目根目录运行：

```powershell
python tools/check_adapter_consistency.py
```

也可以显式传入要扫描的项目路径：

```powershell
python tools/check_adapter_consistency.py D:\dev\some-project
```

脚本会检查三类问题：

- missing adapter
- orphan adapter
- wrong reference

wrong reference 的判断规则是：

- `.agents/skills/<skill>/SKILL.md` 必须引用 `../../../.codex/skills/`
- `.github/skills/<skill>.md` 必须引用 `../../.codex/skills/`

## 不做什么

- 不自动修复
- 不修改任何文件
- 不删除任何 adapter
- 不参与 sync
- 不改变 `.codex/skills` 的分发逻辑
- 不修改 canonical `skills/`

## 输出与退出码

- 无问题时退出码为 `0`
- 存在问题时退出码为 `1`

输出是人类可读的本地检查报告，用于快速识别 adapter drift。