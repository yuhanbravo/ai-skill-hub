# Update Project Status

## What is this

`update-project-status` 是一个项目状态更新型 skill，用来把近期 Git 历史与可用任务来源整理为状态文档、状态日志和可选同步结果。

它默认面向普通项目状态更新，但也支持 `skill-hub` 这种“以 skills、adapters、indexes、tests 和 automation 为主要产物”的仓库形态。

## When to use

适合在需要刷新项目状态、整理近期变更、准备阶段汇报或 handoff 状态摘要时使用；如果目标是首次接管项目，应优先考虑 `project-takeover`。

当目标仓库本身是一个 `skill-hub project`，并且你更关心 `skill coverage`、`invocation readiness`、`adapter/discovery coverage`、`governance readiness` 和 `automation readiness` 时，应使用 `template_type=skillhub`。

## Quick Start

```text
Use the `update-project-status` skill for this repository and refresh the status report.
Project root: <project-root>

# optional
# Config path: <path-or-none>
# Dry run: yes/no
```

## SkillHub Template

如果目标仓库是 skill-hub，可在配置中切换：

```json
{
  "template_type": "skillhub"
}
```

对应模板结构位于 [templates/skillhub_status_template.md](/d:/dev/codex-skill-hub/skills/update-project-status/templates/skillhub_status_template.md)。

切换后，状态输出会采用 skill-hub 口径，而不会继续使用普通项目的 `Recent Features / Fixed Bugs / Upcoming Tasks` 主视角。

详细阶段化执行方式见 [SKILL.md](/d:/dev/codex-skill-hub/skills/update-project-status/SKILL.md)。
