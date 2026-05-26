# Skill Catalog / Entry Surface Audit

- Status: scan-only audit recorded for governance planning
- Scope baseline: `Yuhanbravo/ai-skill-hub`
- Audit type: documentation governance evidence (no implementation changes)

## 1) Scope scanned

本次 scan-only 审计覆盖以下 surface（只读扫描）：

- Canonical skill layer: `skills/`
- Adapter / fallback discovery layer: `.agents/skills/`, `.github/skills/`
- Bridge / mirror layer: `docs/bridge/`
- State snapshots: `docs/HANDOFF.md`, `docs/status/`
- Historical execution evidence: `tasks/`
- Supporting operational surfaces: `tools/`, `tests/`

审计结论基于仓库可见内容，不依赖本地 IDE 或未提交状态。

## 2) Source-surface classification

### A. Canonical

- `skills/`
- 定义：skill 内容唯一 canonical source。
- 治理要求：不得在其他 surface 复制或重写 canonical skill 内容。

### B. Adapter

- `.agents/skills/`
- `.github/skills/`
- 定义：thin adapter / fallback discovery layer。
- 治理要求：仅用于发现与路由，不作为 authoring surface。

### C. Bridge / mirror

- `docs/bridge/`
- 定义：mirror / reference surface。
- 治理要求：不是 active source，不承载 canonical ownership。

### D. Historical evidence

- `tasks/`
- 定义：历史 task package / execution report 证据层。
- 治理要求：可作为 candidate pattern 来源；不自动晋升为 canonical。

### E. Status / handoff

- `docs/HANDOFF.md`
- `docs/status/`
- 定义：state / phase snapshots。
- 治理要求：用于状态表达，不作为模板入口目录。

### F. Tools / tests

- `tools/`
- `tests/`
- 定义：校验与工具支持层。
- 治理要求：不承载 skill catalog 或 template registry 的 canonical 文本。

## 3) Key findings

1. 主问题不是内容缺失，而是开发者入口分散与 source status 不清晰。
2. 同一资产类型（template / snippet / prompt / example）分布在多个 surface，发现路径成本高。
3. `skills/` canonical 与 adapter/bridge/historical 的边界虽有声明，但入口层尚缺集中索引。
4. `tasks/` 中存在高价值 candidate pattern，但当前没有正式 candidate index。

## 4) Risk classification

### P0

- Bridge template copies 与 canonical templates 并存，存在误用风险。
- Adapter / bridge surfaces 可能被误认为 authoring surfaces。

### P1

- 近似 skill 边界可能混淆，尤其 `project-takeover` vs `system-takeover`。
- `workflow-bootstrap` supporting assets 较多，入口学习成本高。

### P2

- examples / templates / snippets 可发现但未集中索引。
- historical tasks 含有可复用 candidate pattern，但缺少正式 candidate indexing。

## 5) Recommended direction

推荐方向：**Option B — Skill Catalog + Template Registry**。

原因：

- 可以在不改 canonical 内容的前提下，先解决“入口清晰度”和“source-surface 可辨识性”。
- 适合分阶段落地，保留回滚与审阅边界。

## 6) Explicit non-goals (this round)

本轮（PR 1 governance landing）明确不做：

- 不做 full developer entry guide
- 不做 skill migration
- 不做 renaming
- 不做 adapter sync
- 不做 bridge refresh
- 不做 HANDOFF / STATUS update

## 7) Why separate PR 1 and PR 2

将治理落地拆分为两轮：

- PR 1：记录 scan-only audit 证据 + 固化 Phase 1 bounded task package。
- PR 2：按已审阅 task package 执行最小实现（仅新增 catalog/registry + execution report）。

拆分收益：

1. 先定边界再施工，减少误改风险。
2. 先对齐 canonical/adapter/bridge/historical 语义，再进入文件创建。
3. 保持审计证据可追踪，便于后续 reviewer 复核。

## 8) Recommended PR 2 target files

- `docs/SKILL_CATALOG.md`
- `docs/TEMPLATE_REGISTRY.md`
- `tasks/skill_catalog_phase1_catalog_registry_execution_report.md`

