# Skills 简短中文说明

这个目录下目前有几类可复用 skill，用来帮助项目接管、状态同步、文档治理和 handoff 协作。下面先汇总最常用的几个，并给出最短使用方式。

## project-takeover

用途：
- 为一个仓库生成接手资料和 onboarding 输出，适合“我要接管这个项目”或“帮我生成交接包”这类场景。

最短用法：

```text
Use the `project-takeover` skill on this repository and prepare a takeover packet.
Project root: <project-root>
```

典型输出：
- 项目接手报告
- onboarding 摘要
- 欢迎说明或交接说明

适合什么时候用：
- 新人接手项目
- AI 代理首次进入陌生仓库
- 需要快速盘点文档、环境和任务来源

## update-project-status

用途：
- 根据最近 Git 提交和任务来源生成项目状态文档，适合“更新项目进度”或“整理最近做了什么”。

最短用法：

```text
Use the `update-project-status` skill for this repository and refresh the status report.
Project root: <project-root>
```

典型输出：
- 状态报告
- 状态日志
- 可选同步到共享文档或外部平台

适合什么时候用：
- 周报 / 阶段总结
- 交接前整理最近变更
- 自动维护项目状态文档

## chatgpt-handoff-pilot

用途：
- 建立“上游出任务包，下游按范围实施并回传 execution report”的最小协作流程。

最短用法：

```text
请按 `chatgpt-handoff-pilot` 模式执行下面的任务包，并在开始前先复述理解，完成后输出 execution report。
```

典型输出：
- 明确边界的任务包
- 按范围实施的代码或文档改动
- execution report 回执

适合什么时候用：
- ChatGPT 负责方案，Codex / Copilot 负责落地
- 希望控制任务边界，减少“顺手多做”
- 希望每轮执行后有标准化回执

## 其他 skill

- `documentation-governance`：检查文档治理相关结构和约束。
- `file-structure-check`：检查项目目录结构是否符合预期。
- `financial-data-project-migration`：面向金融数据项目迁移场景的专项 skill。

## 使用建议

- 想“先接手项目”，优先用 `project-takeover`。
- 想“更新当前进展”，优先用 `update-project-status`。
- 想“把任务拆清楚再交给另一个代理做”，优先用 `chatgpt-handoff-pilot`。
- 如果是第一次试用，先从 `--dry-run` 或小范围任务开始更稳。
