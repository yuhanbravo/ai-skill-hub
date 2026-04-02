# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准接管调用

```text
请使用 `project-takeover` 处理以下仓库接管任务。

背景：
- 这是一个需要接手或 onboarding 的项目

目标：
- 生成 takeover packet，并帮助新维护者快速理解仓库

范围：
- 扫描项目环境、关键文档、任务来源和可用审计脚本
- 整理接手所需的结构化输出

约束：
- 保留项目本地配置优先级
- 不做未授权的高风险副作用

预期输出：
- 按 `scan -> understand -> structure -> output` 推进
- `project_takeover_report.md`
- `project_onboarding_summary.md`
- `welcome_email.md`
- 风险与下一步建议
```

### 模板 2：严格阶段化执行模板

```text
请按 `project-takeover` 的方法执行本次任务。

要求：
- 先总结你对项目接管目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 明确当前使用的配置、脚本和可选参数
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Primary goal: <takeover | onboarding | handoff prep>
- Config path: <path-or-none>
- Report dir: <path-or-default>
- Shared dir: <path-or-none>
- Dry run: <yes-or-no>
- Apply safe fixes: <yes-or-no>
- Install: <yes-or-no>
- Structure script override: <path-or-none>
- Docs script override: <path-or-none>
```
