# 任务包：Phase 3 结构性评估（Planning-Only）

## 任务标识

- 名称：Phase 3 Structural Evaluation（ADR + Migration/No-Migration 结论）
- 阶段：Phase 3
- 提交方：ChatGPT（上游）
- 日期：2026-04-21

## 背景

当前 handoff 指向 Phase 3：需要评估长期扩展策略，但避免在治理基础尚未稳定时提前重构。
重点议题包括：
1. `docs/bridge` 全量镜像策略是否继续保留，或改为自动生成/部分镜像。
2. `router/pipeline` 是否需要更强确定性策略层（但明确非 controller 化）。

## 本次目标

- 形成 ADR 风格结构性决策记录（至少覆盖上述两项议题）。
- 给出迁移/不迁移结论（now/later/not-now）。
- 明确每个结论的收益、风险、触发条件与回滚路径。

## 本次范围

- 允许修改：仅 `./tasks` 目录中的任务产物文档。
- 重点关注：
  - 决策选项对比
  - 治理一致性与维护成本
  - 风险控制与回滚可行性

## 明确不做

- 不改动业务代码或现有仓库结构。
- 不进行 repo-wide 重命名或大规模迁移。
- 不新增自动化工具链实现（可提出建议但不落地）。
- 不将 router/pipeline 演进为 controller 架构。

## 目标文件或目录

- `tasks/phase3_task_package.md`（本任务包）
- `tasks/phase3_structural_decision_record.md`（执行产物）
- `tasks/phase3_execution_report.md`（执行回执）

## 验收标准

- 两个核心议题均形成 ADR 风格记录。
- 结论包含清晰收益-风险-回滚路径。
- 明确迁移/不迁移建议和时机（now/later/not-now）。
- 输出内容不越界到代码重构或结构改造实施。

## 约束条件

- 必须遵守仓库本地规则（`AGENTS.md`）。
- 必须按 chatgpt-handoff-pilot 模式推进：读取输入 → 复述边界 → bounded execution → execution report。
- 仅在授权范围内实施。

## 输出要求

- 是否需要 execution report：是
- 是否需要列出风险/待确认项：是
- 是否需要附验证说明：是（至少包含本轮读取/检查命令）

## 补充上下文

- 相关文档：
  - `AGENTS.md`
  - `skills/chatgpt-handoff-pilot/SKILL.md`
- 参考说明：
  - 优先低风险、增量式、边界清晰的结构评估。
