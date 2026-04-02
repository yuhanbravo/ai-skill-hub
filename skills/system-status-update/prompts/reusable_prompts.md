# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准 system status 调用

```text
请使用 `system-status-update` 处理以下任务。

背景：
- 目标对象是 `ai-skill-hub` 自身，不是普通业务项目

目标：
- 刷新 system status，并按 layer / phase / capabilities / stability 输出

范围：
- `skills/`
- `.agents/`
- `.github/`
- `tools/`
- `docs/status/`

约束：
- 复用 `update-project-status`
- 不输出文件级变更清单
- 不退化为项目施工日报

预期输出：
- Layer Status
- Current Phase
- Capabilities
- Stability
```

### 模板 2：严格 system-layer 输出调用

```text
请按 `system-status-update` 的方法执行本次任务。

要求：
- 先确认目标对象是 capability system
- 复用 `update-project-status` 的状态刷新过程
- 输出必须包含 `Canonical Skill Layer`、`Distribution Layer`、`Governance Layer`、`Tooling Layer`
- 明确当前 `Phase`、`Capabilities`、`Stability`
- 不输出文件级改动摘要

任务内容：
- System root: <project-root>
- Status artifact: <path-or-none>
- Dry run: <yes-or-no>
```
