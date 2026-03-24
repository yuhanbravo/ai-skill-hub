# Financial Data Project Migration

## What is this

`financial-data-project-migration` 是一个面向金融数据 Python 项目的迁移顾问型 skill，用来先判断项目类型与迁移阶段，再给出最小安全迁移建议。

## When to use

适合在脚本密集、Excel 资产较多、存在 Wind 或桌面环境耦合时，先做保守迁移判断；如果目标是直接审计目录或立即重构，这个 skill 不是第一步。

## Quick Start

```text
Use the `financial-data-project-migration` skill on this repository and prepare a migration advisory.
Project root: <project-root>

# optional
# Need mapping candidates: yes/no
# Need minimal TODO: yes/no
```

详细迁移 playbook 见 [SKILL.md](/d:/dev/codex-skill-hub/skills/financial-data-project-migration/SKILL.md)。
