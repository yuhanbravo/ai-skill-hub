# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准 system handoff 更新

```text
请使用 `system-handoff` 处理以下任务。

背景：
- 目标对象是 `ai-skill-hub` 自身的 handoff 主文档

目标：
- 以 section-aware merge 的方式更新 system handoff

范围：
- `docs/HANDOFF.md`
- 当前 phase
- system capabilities
- hard boundaries

约束：
- 复用 `chatgpt-handoff-pilot`
- 不全文重写
- 不输出代码 diff 或逐文件说明

预期输出：
- Current Status
- Hard Boundaries
- Key Design Decisions
- Intentional Gaps
- Next Phase Direction
```

### 模板 2：严格 section-aware merge 调用

```text
请按 `system-handoff` 的方法执行本次任务。

要求：
- 先读取 `docs/HANDOFF.md`
- 复用 `chatgpt-handoff-pilot` 的 section-aware merge 思路
- 只增量更新 `Current Status`、`Hard Boundaries`、`Key Design Decisions`、`Intentional Gaps`、`Next Phase Direction`
- 不全文重写
- `Next Phase Direction` 只写方向级演进

任务内容：
- Handoff document: docs/HANDOFF.md
- System phase: <phase>
- New system facts: <facts>
```
