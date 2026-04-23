# 任务包：Copilot 主控 / Codex 施工工作流（Phase 3A：project-side runtime pack template sketch）

## 任务标识

- task id: `WF-PHASE3A-TEMPLATE-SKETCH-V1`
- 名称：Phase 3A / project-side runtime pack template sketch
- 阶段：`Phase 3A`
- 提交方：Planner
- 日期：`2026-04-23`
- 前置输入：
  - `tasks/copilot-codex-workflow_phase2_entrypoint_decision_memo.md`
  - `tasks/copilot-codex-workflow_phase2_execution_report.md`
  - `skills/workflow-bootstrap/README.md`
  - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
  - `skills/workflow-bootstrap/agents_md_thin_entrypoint_draft.md`
  - `skills/workflow-bootstrap/copilot_instructions_thin_adapter_draft.md`
  - `skills/workflow-bootstrap/canonical_backreference_rules_draft.md`
- 补充上下文：
  - `tasks/copilot-codex-workflow_phase1_execution_report.md`

---

## 1. Scope Restatement

本轮仅为 future project-side runtime pack 形成一版 **canonical-layer template sketch**。

本轮必须解决的核心问题是：

1. future project-side runtime pack 第一版中，哪些文件是必选，哪些文件是可选。
2. `AGENTS.md` 的最薄结构里，哪些字段应固定，哪些字段留给项目自填。
3. `.github/copilot-instructions.md` 应薄到什么程度，才不会与 `AGENTS.md` 重复。
4. canonical guidance 在 consumer repo 中应如何做更稳的路径回指。
5. 如何防止 project-side runtime pack 被持续扩写成第二规则库。

本轮必须继续遵守 `workflow-bootstrap` 的既有 canonical 边界与 Phase 2 结论：

- `AGENTS.md` 是 future project-side 的最薄主入口。
- `.github/copilot-instructions.md` 是 Copilot-specific thin adapter。
- project-side entrypoints 必须强制回指 canonical guidance。
- project-side runtime pack 只能是入口层，不得演化为第二事实源。

本轮只做 sketch，不做真实 project-side runtime pack 实现，不做 rollout，不做 distribution，不做工具变更。

---

## 2. 当前阶段承接关系（Phase 1 / Phase 2 / Phase 3A）

### Phase 1 已完成的事情

Phase 1 已在 `skills/workflow-bootstrap/` 内完成 canonical workflow shell 的最小落地，并明确：

- `Copilot 主控 / Codex 施工` 是当前默认协作壳层；
- `planner / implementer / reviewer` 的最小角色分工；
- canonical layer 与 future runtime pack 的关系；
- future runtime pack 的候选最小文件族只在 canonical 文档中描述，不在 hub 内真实实现。

### Phase 2 已完成的事情

Phase 2 已进一步锁定 entrypoint 级结论，并形成 canonical drafts：

- `AGENTS.md` 作为 future project-side runtime pack 的最薄主入口；
- `.github/copilot-instructions.md` 作为 Copilot-specific thin adapter；
- 入口文件必须采用 forced backreference 机制；
- project-side runtime pack 不得膨胀为第二规则库。

Phase 2 的产物已经回答了“主入口选谁”和“强制回指如何表达”的问题，但还没有进入第一版 template sketch。

### Phase 3A 本轮承接任务

Phase 3A 只在上述 Phase 1 / Phase 2 结论之上，继续向前推进到：

- 将 future project-side runtime pack 第一版文件族区分为 required / optional；
- 将 future `AGENTS.md` 分解为 fixed fields / project-fill fields；
- 将 future `.github/copilot-instructions.md` 压缩到真正的 thin adapter 粒度；
- 形成 canonical-only 的 template sketch 落盘方案；
- 明确 anti-expansion guardrails，防止 future project-side runtime pack 演化为第二事实源。

Phase 3A 不重写 Phase 1 / Phase 2 结论，只做承接与收敛。

---

## 3. Phase 3A 的 Goal / In Scope / Out of Scope

### Goal

在不进入真实 project-side 实现的前提下，为 future runtime pack 形成一版足够清晰、可交接给后续执行侧 AI 的 canonical template sketch。

### In Scope

本轮允许在 canonical 层内完成以下事情：

1. 明确 future project-side runtime pack v1 的 required / optional 文件清单。
2. 为 future `AGENTS.md` 形成 template sketch，明确哪些字段固定、哪些字段由项目自填。
3. 为 future `.github/copilot-instructions.md` 形成 template sketch，明确其与 `AGENTS.md` 的职责边界与非重复原则。
4. 为 consumer repo 中的 canonical backreference 路径表达，提出更稳的写法规则与占位方式。
5. 形成防止 runtime pack 膨胀为第二规则库的 guardrails。
6. 如有必要，对 `skills/workflow-bootstrap/README.md` 做最小导航补充。
7. 输出 execution report。

### Out of Scope

本轮明确不做以下事项：

1. 不创建真实 project-side runtime pack 文件：
   - 不创建仓库根目录 `AGENTS.md`
   - 不创建真实 `.github/copilot-instructions.md`
   - 不创建真实 `.github/instructions/*.instructions.md`
   - 不创建真实 `.github/agents/*.agent.md`
2. 不进入 rollout、distribution、bundle、adapter 下发或 consumer-side 落地。
3. 不改 `workflow-bootstrap` 的既有 canonical 主结论。
4. 不改 `chatgpt-handoff-pilot` 的协议层契约。
5. 不修改任何 sync/export/import/check/index 工具逻辑。
6. 不新增 `.agents/skills/`、`.github/skills/`、`SKILLS_INDEX.md` 或 `skills_index.json` 相关 discoverability / distribution 变更。
7. 不触碰现有 `tasks/phase3_*` planning-only 文档链路；本轮只处理 `copilot-codex-workflow_*` 这一条 workflow 线。

---

## 4. Authorized Files / Areas

本轮仅授权以下写入范围：

- `skills/workflow-bootstrap/project_side_runtime_pack_template_sketch.md`
- `skills/workflow-bootstrap/project_side_agents_md_template_sketch.md`
- `skills/workflow-bootstrap/project_side_copilot_instructions_template_sketch.md`
- `skills/workflow-bootstrap/README.md`
- `tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`

授权边界说明：

- `README.md` 只允许最小导航性补充，不允许整篇重写。
- 除上述路径外，默认无权限修改。
- Phase 2 的 decision memo、execution report 与 draft assets 仅作为输入参考，不在本轮修改范围内。

---

## 5. Expected Deliverables

### Deliverable 1

`skills/workflow-bootstrap/project_side_runtime_pack_template_sketch.md`

要求至少回答：

- future runtime pack v1 哪些文件是 required，哪些文件是 optional；
- required / optional 的判定理由；
- optional 文件何时才值得进入后续阶段；
- canonical guidance 在 consumer repo 中如何做具体文件路径回指；
- 如何通过 manifest-level guardrails 防止 project-side runtime pack 持续扩写。

该文件必须保持为 canonical sketch，不得把 sketch 写成已实现事实。

### Deliverable 2

`skills/workflow-bootstrap/project_side_agents_md_template_sketch.md`

要求至少回答：

- `AGENTS.md` 的身份声明中，哪些字段必须固定；
- `Canonical Guidance` 部分中，哪些内容必须固定为 backreference contract；
- 哪些字段允许项目自填，例如项目名、项目局部边界、项目本地 canonical payload 路径；
- 如何保证 future `AGENTS.md` 保持最薄主入口，而不是完整规则库；
- 如何明确它与 canonical guidance 冲突时的优先级。

该 sketch 必须显式承接 Phase 2 中 `AGENTS.md` 是主入口的结论，不得改写结论本身。

### Deliverable 3

`skills/workflow-bootstrap/project_side_copilot_instructions_template_sketch.md`

要求至少回答：

- `.github/copilot-instructions.md` 的超薄职责边界；
- 哪些内容只能保留在 `AGENTS.md`，不能再在 Copilot adapter 中重复；
- 哪些高频高约束规则可以保留在 Copilot adapter；
- 如何要求它强制回指 `AGENTS.md` 与 canonical guidance；
- 如何用结构或固定文案防止它膨胀成第二规则库。

该 sketch 必须显式承接 Phase 2 中 “Copilot-specific thin adapter” 的结论，不得把它重新提升为主入口。

### Deliverable 4

如确有必要，可对 `skills/workflow-bootstrap/README.md` 做最小导航补充。

允许内容仅限：

- 新增一个很小的 Phase 3A navigation 段；
- 指向新的 template sketch 文档；
- 明确这些文档是 canonical-only sketches；
- 明确它们不是已下发到 consumer repo 的真实 runtime pack 文件。

### Deliverable 5

`tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`

必须明确：

- 本轮新增或更新了哪些 canonical sketch 文档；
- 本轮没有实现哪些东西；
- 本轮如何验证边界与表达；
- 是否还存在 deferred questions，且这些问题为什么留到后续阶段。

---

## 6. Validation / Acceptance

本轮以文档边界校验和表达一致性校验为主，不要求工具链或分发验证。

至少需要完成以下检查：

### A. Boundary Check

确认：

- 没有创建真实 project-side `AGENTS.md`；
- 没有创建真实 `.github/copilot-instructions.md`；
- 没有创建真实 `.github/instructions/*.instructions.md`；
- 没有创建真实 `.github/agents/*.agent.md`；
- 没有进入 rollout / distribution / tool changes。

### B. Consistency Check

确认：

- Phase 3A sketch 与 Phase 1 的 canonical/runtime-pack 分层不冲突；
- Phase 3A sketch 不改写 Phase 2 的主入口与 thin-adapter 结论；
- 所有新文档都明确表述自己是 sketch / future target / canonical-only asset。

### C. Coverage Check

确认本轮 sketch 已明确覆盖以下五项核心问题：

1. required / optional 文件划分；
2. `AGENTS.md` fixed fields / project-fill fields；
3. Copilot adapter 的最薄粒度；
4. consumer repo 中的更稳 canonical backreference 表达；
5. 防止第二规则库化的 guardrails。

### D. Acceptance Standard

验收通过标准为：

- 所有授权 deliverables 已存在；
- 内容表述与既有阶段结论一致；
- 没有越界到真实 runtime pack 实现；
- 没有触发 distribution、adapter、工具或索引层改动；
- execution report 清楚记录本轮范围、未做事项、验证动作与下一步建议。

---

## 7. Execution Report Requirements

执行完成后，必须输出结构化 execution report，至少包含：

1. Scope Restatement
2. Files Changed
3. What Was Sketched
4. What Was Explicitly Not Implemented
5. Boundary Check
6. Validation Notes
7. Risks / Assumptions
8. Deferred Questions
9. Recommended Next Step

回执中必须显式写出以下结论：

- 本轮只完成 canonical-layer template sketch；
- 未创建真实 project-side runtime pack 文件；
- 未进入 rollout / distribution / tooling / adapter changes；
- Phase 3A 只是为后续实现阶段准备更稳的模板边界，而不是直接下发 runtime pack。

---

## 8. 推荐落盘路径

推荐落盘必须继续留在 canonical layer，而不是落到真实 consumer runtime surface。

推荐路径如下：

- `skills/workflow-bootstrap/project_side_runtime_pack_template_sketch.md`
- `skills/workflow-bootstrap/project_side_agents_md_template_sketch.md`
- `skills/workflow-bootstrap/project_side_copilot_instructions_template_sketch.md`
- `skills/workflow-bootstrap/README.md`（仅在必要时最小补充）
- `tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`

明确禁止的落盘路径：

- 仓库根目录 `AGENTS.md`
- 真实 `.github/copilot-instructions.md`
- 真实 `.github/instructions/`
- 真实 `.github/agents/`

一句话任务摘要：

**Phase 3A 只在 canonical layer 内形成 future project-side runtime pack 的 template sketch，明确 required/optional 文件、`AGENTS.md` 固定与自填字段、Copilot thin adapter 的最薄边界、canonical backreference 写法与 anti-expansion guardrails；不进入真实实现、rollout、distribution 或工具改动。**
