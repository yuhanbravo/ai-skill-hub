# Update Project Status

## What is this

`update-project-status` 是一个项目状态更新型 skill，用来把近期 Git 历史与可用任务来源整理为状态文档、状态日志和可选同步结果。

它保留原有脚本、CLI 参数和输出文件，但把执行过程明确组织为 `scan -> understand -> structure -> output` 四个阶段。

## When to use

适合在你需要刷新项目状态、整理近期变更、准备阶段汇报或 handoff 状态摘要时使用。

如果你的目标是首次接管项目而不是更新持续状态，应优先考虑 `project-takeover`。

## Quick Start

```text
Use the `update-project-status` skill for this repository and refresh the status report.
Project root: <project-root>
```

如需更细控制，可补充 `config path`、`status file override`、`log file override`、`shared doc override`、`commit limit`、`dry run`、`install post-commit hook` 等参数。详细阶段化执行方式见 [SKILL.md](/d:/dev/codex-skill-hub/skills/update-project-status/SKILL.md)。
