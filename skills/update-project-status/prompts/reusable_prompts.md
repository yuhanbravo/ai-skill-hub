# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准状态刷新模板

```text
请使用 `update-project-status` 处理以下任务。

背景：
- 需要根据 Git-first 信号，或在 no-git 场景下根据 workspace/task signals 刷新项目状态

目标：
- 生成或更新状态文档，并整理关键进展、风险和待办

范围：
- 读取最近提交
- 读取 workspace status signals（如 README/docs/TASKBOARD）
- 合并可用任务源
- 生成状态 markdown 与状态日志
- 如已授权，再执行同步

约束：
- 默认不改变项目，只做观察和结构化输出
- 未明确授权时，不安装 hook，不做额外发布

预期输出：
- 按 `scan -> understand -> structure -> output` 推进
- 刷新的状态文档
- 刷新的状态日志
- 风险、待办与后续动作摘要
```

### 模板 2：严格阶段化执行模板

```text
请按 `update-project-status` 的方法执行本次任务。

要求：
- 先总结你对本次状态更新目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 显式说明 `Phase -> Execution Mapping`
- 明确哪些动作只是观察，哪些动作会写文件或同步
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Primary goal: <status refresh | recent change summary | publish status>
- Config path: <path-or-none>
- Status file override: <path-or-none>
- Log file override: <path-or-none>
- Shared doc override: <path-or-none>
- Commit limit: <n-or-default>
- Dry run: <yes-or-no>
- Install post-commit hook: <yes-or-no>
```
