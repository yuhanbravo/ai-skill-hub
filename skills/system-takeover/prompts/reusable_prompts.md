# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 11. Prompt 模板（Reusable Prompt）

### 模板 1：标准系统接管模板

```text
请使用 `system-takeover` 处理以下任务。

背景：
- 目标对象是一个 capability system，而不是普通业务项目

目标：
- 分析系统结构、能力地图、调用就绪度、调度层、适配层、工具链和治理成熟度

范围：
- `skills/`
- `tools/`
- `docs/`
- `.agents/`
- `.github/`
- `tests/`

约束：
- 不修改现有 protocol、router、pipeline 或已有 skills
- 只做 system-level takeover analysis

预期输出：
- System Structure
- Capability Map
- Maturity Assessment
- Top Bottlenecks
- Evolution Plan
```

### 模板 2：严格分层分析模板

```text
请按 `system-takeover` 的方法执行本次任务。

要求：
- 先确认该对象是否属于 capability system
- 按 Capability Map、Invocation Readiness、Routing Layer、Pipeline Layer、Adapter Layer、Tooling & Automation、Governance 七个维度推进
- 明确哪些结论是已确认事实，哪些是推断
- 输出系统结构图、按层成熟度、Top 3 瓶颈和下一阶段建议

任务内容：
- System root: <project-root>
- System type: <skill-hub | multi-agent system | orchestration system | capability OS>
- Focus layers: <one-or-more>
- Output mode: <report | summary | takeover packet>
```
