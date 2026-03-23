# Project Takeover

## What is this

`project-takeover` 是一个项目接管型 skill，用来为陌生仓库生成最小可用的 takeover packet，帮助新维护者或 AI 代理快速进入项目。

它保留原有脚本的输入输出逻辑，但把执行过程明确组织为 `scan -> understand -> structure -> output` 四个阶段。

## When to use

适合在你要接手一个仓库、准备 onboarding 材料、生成 handoff 输出，或者希望快速盘点环境、文档和任务来源时使用。

如果你的目标只是更新项目进度，而不是首次接管项目，应优先考虑 `update-project-status`。

## Quick Start

```text
Use the `project-takeover` skill on this repository and prepare a takeover packet.
Project root: <project-root>
```

如需更细控制，可补充 `config path`、`report dir`、`shared dir`、`dry run`、`apply safe fixes`、`install`、`structure script override`、`docs script override` 等参数。详细执行方式见 [SKILL.md](/d:/dev/codex-skill-hub/skills/project-takeover/SKILL.md)。
