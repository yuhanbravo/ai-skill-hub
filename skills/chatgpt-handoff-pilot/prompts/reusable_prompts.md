# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：生成任务包

```text
请使用 `chatgpt-handoff-pilot` 的方法，为下面的任务生成一份可直接交给 Codex / Copilot 执行的 task package。

背景：
- <背景>

目标：
- <目标>

本次范围：
- <范围>

明确不做：
- <不做事项>

目标文件或目录：
- <文件或目录>

验收标准：
- <验收标准>

约束条件：
- <约束>

输出要求：
- 先形成边界清晰的 `task package`
- 生成结构清晰、边界明确的任务包
- 如果上下文不完整，单列“假设前提”
- 任务包应能直接用于 handoff
```

### 模板 2：执行任务包

```text
请按 `chatgpt-handoff-pilot` 的方法执行下面的任务包。

要求：
- 先完整阅读任务包和其中引用的本地规则
- 按“读取输入 -> 复述边界 -> bounded execution -> execution report”推进
- 动手前先用 2-4 句话复述目标、边界、修改范围和不做事项
- 只在授权范围内实施
- 完成后输出 execution report

任务包：
<粘贴任务包正文>
```

### 模板 3：生成或更新项目 handoff 主文档

```text
请使用 `chatgpt-handoff-pilot` 更新本项目的 handoff 主文档。

要求：
- 先读取 `docs/HANDOFF.md`（如果存在）
- 优先按 section 进行增量合并，而不是全文重写
- 重点更新：`Update Log`、`Current Status/当前状态`、`Hard Boundaries/边界`、`Recommended Next Steps/下一步建议`、`Environment Blockers/环境阻塞`
- 保留已有结构和人工编辑内容
- 若缺少合适章节，可以补 section，但不要整体重排
- 若 `docs/HANDOFF.md` 不存在，则创建它
- 不要默认生成 `minimal_handoff_manual.md`
- 如有历史 `minimal_handoff_manual.md`，仅标记为 legacy/generated，不再更新
- 追加一条 `Update Log` 记录

输出：
- 更新后的 `docs/HANDOFF.md`
- 简短 execution report
```

### 模板 4：生成 execution report

```text
请基于本次实施结果输出 execution report。

请至少覆盖以下内容：
- 本次改了什么
- 本次没改什么
- 如何验证
- 当前阻塞
- 下一步建议
- 假设清单

附加要求：
- 如果有阻塞项，单列说明
- 如果有未完成项，说明原因
- 额外发现的问题只记录，不混入本次完成项
```
