# 任务包：Copilot 主控 / Codex 施工工作流（Phase 3B：pilot repo validation sketch）

## 任务标识

- task id: `WF-PHASE3B-PILOT-VALIDATION-SKETCH-V1`
- 名称：Phase 3B / pilot repo validation sketch
- 阶段：`Phase 3B`
- 提交方：Planner
- 日期：`2026-04-23`
- 前置输入：
  - `tasks/copilot-codex-workflow_phase2_entrypoint_decision_memo.md`
  - `tasks/copilot-codex-workflow_phase2_execution_report.md`
  - `tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`
  - `skills/workflow-bootstrap/README.md`
  - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
  - `skills/workflow-bootstrap/agents_md_thin_entrypoint_draft.md`
  - `skills/workflow-bootstrap/copilot_instructions_thin_adapter_draft.md`
  - `skills/workflow-bootstrap/canonical_backreference_rules_draft.md`
  - `skills/workflow-bootstrap/project_side_runtime_pack_template_sketch.md`
  - `skills/workflow-bootstrap/project_side_agents_md_template_sketch.md`
  - `skills/workflow-bootstrap/project_side_copilot_instructions_template_sketch.md`
- 补充上下文：
  - `tasks/copilot-codex-workflow_phase3a_template_sketch_task_package.md`

---

## 1. Scope Restatement

本轮仅为 future project-side runtime pack 形成一版 **single consumer repo pilot validation sketch**。

本轮必须继续遵守 `workflow-bootstrap` 当前 canonical 边界与既有结论：

- `AGENTS.md` 是 future project-side 的最薄主入口。
- `.github/copilot-instructions.md` 是 Copilot-specific thin adapter。
- project-side entrypoints 必须强制回指 canonical guidance。
- project-side runtime pack 只能是入口层，不得演化为第二事实源。

本轮必须解决的核心问题是：

1. 以一个单一 consumer repo 画像为对象，验证 v1 project-side runtime pack 的入口组合是否成立。
2. 验证 v1 中哪些文件应视为 required，哪些是 optional，哪些应继续 deferred。
3. 验证 `AGENTS.md` 的 fixed fields、project-fill fields、placeholder fields 在 consumer repo 中如何表达。
4. 验证 `.github/copilot-instructions.md` 的最薄边界在 consumer repo 中是否足够。
5. 验证 canonical guidance 的路径回指在 consumer repo 中如何表达更稳。
6. 验证如何防止 project-side runtime pack 在试点仓库中膨胀成第二规则库。

本轮只做 sketch / validation，不做真实 implementation，不做 rollout，不做 distribution，不修改任何 consumer repo，也不触发工具链变更。

---

## 2. 当前阶段承接关系（Phase 1 / Phase 2 / Phase 3A / Phase 3B）

### Phase 1 已完成的事情

Phase 1 已在 `skills/workflow-bootstrap/` 内完成 canonical workflow shell 的最小落地，并明确：

- `Copilot 主控 / Codex 施工` 是当前默认协作壳层；
- `planner / implementer / reviewer` 的最小角色分工；
- canonical layer 与 future runtime pack 的关系；
- future runtime pack 只作为项目侧目标映射，不在 hub 内真实实现。

### Phase 2 已完成的事情

Phase 2 已锁定 entrypoint 级结论，并形成 canonical drafts：

- `AGENTS.md` 作为 future project-side runtime pack 的最薄主入口；
- `.github/copilot-instructions.md` 作为 Copilot-specific thin adapter；
- 入口文件必须采用 forced backreference 机制；
- project-side runtime pack 不得膨胀为第二规则库。

### Phase 3A 已完成的事情

Phase 3A 已在 canonical layer 内完成 template sketch 收敛，并明确：

- project-side runtime pack v1 的 required / optional / not-recommended 初步划分；
- future `AGENTS.md` 的 fixed fields 与 project-fill fields；
- future `.github/copilot-instructions.md` 的超薄职责边界；
- placeholder-based canonical backreference 写法；
- anti-expansion guardrails。

### Phase 3B 本轮承接任务

Phase 3B 不重写 Phase 1 / Phase 2 / Phase 3A 的结论，只在这些结论之上推进到单一 consumer repo 试点验证草案。

本轮目标是把 Phase 3A 的 template sketch 放进一个明确的 consumer repo 画像中，验证：

- 入口组合是否在单仓画像中成立；
- required / optional / deferred 分类是否稳；
- 字段、占位符与路径回指如何在 consumer repo 里表达；
- anti-second-rulebook guardrails 是否足以约束 project-side runtime pack。

本轮依然不是 consumer repo implementation，也不是 rollout 前的 distribution 准备。

---

## 3. Phase 3B 的 Goal / In Scope / Out of Scope

### Goal

在不进入真实 consumer repo 实现的前提下，为一个单一 consumer repo 画像形成一版可交接的 pilot validation sketch，判断 v1 project-side runtime pack 的入口组合与最薄边界是否成立。

### In Scope

本轮允许在 canonical layer 内完成以下事情：

1. 明确并固定一个试点 consumer repo 画像，作为本轮唯一验证对象。
2. 基于该画像，对 v1 project-side runtime pack 的入口组合进行 sketch-level validation。
3. 验证 `AGENTS.md` 与 `.github/copilot-instructions.md` 在该画像中的 required / optional / deferred 边界。
4. 验证 `AGENTS.md` 的 fixed fields、project-fill fields、placeholder fields 应如何表达。
5. 验证 `.github/copilot-instructions.md` 是否足以保持 Copilot-specific thin adapter 身份，而不重新成为主入口。
6. 验证 canonical guidance 的路径回指在单仓画像中的更稳表达方式。
7. 验证 anti-expansion guardrails 如何在试点画像中防止第二规则库化。
8. 形成可直接交给后续执行侧 AI 的文档化 deliverables。
9. 输出 execution report。

### Out of Scope

本轮明确不做以下事项：

1. 不创建真实 consumer repo 文件：
   - 不创建真实 `AGENTS.md`
   - 不创建真实 `.github/copilot-instructions.md`
   - 不创建真实 `.github/instructions/*.instructions.md`
   - 不创建真实 `.github/agents/*.agent.md`
2. 不创建或修改任何真实 consumer repo。
3. 不进入 implementation、adoption、rollout、distribution、bundle 或下发。
4. 不修改 sync/export/import/check/index/tooling 逻辑。
5. 不改写 `workflow-bootstrap`、`chatgpt-handoff-pilot` 或既有 phase conclusions 的 canonical contract。
6. 不把 validation sketch 写成 project-side runtime pack 已实现事实。
7. 不为多个 consumer repo 同时建模；本轮只允许一个试点画像。

---

## 4. 核心验证问题清单

执行侧必须围绕以下问题显式给出验证结论：

1. 对于一个单一 consumer repo 画像，`AGENTS.md` + `.github/copilot-instructions.md` 是否足以构成 v1 的基础入口组合。
2. 在该画像下，`.github/instructions/*.instructions.md` 是否仍应保持 optional，而不是提前变成 required。
3. 在该画像下，`.github/agents/*.agent.md` 是否应继续 deferred，而不是进入 v1。
4. `AGENTS.md` 中哪些字段必须固定为 canonical contract，哪些字段必须由项目自填，哪些字段适合作为 placeholder 保留到后续实现阶段。
5. `.github/copilot-instructions.md` 只保留哪些高频高约束内容才算“足够薄”。
6. canonical guidance 的回指路径在 consumer repo 中应如何表达，才能避免目录级模糊引用、绝对路径假设或 hub/consumer 同构假设。
7. 哪些 guardrails 可以显式阻止试点仓库把 runtime pack 膨胀成第二规则库。
8. 哪些问题仍应继续 deferred 到后续 implementation 阶段，而不是在 Phase 3B 里抢答。

此外，执行侧必须在 deliverables 中显式写出一个“试点 consumer repo 画像”，建议以如下基线为默认对象：

- Python 脚本 / 分析型项目；
- 已有 Git 仓库；
- 具备 `README` / `docs` / `src` / `tests` 的基本结构；
- 将来可能接入 `AGENTS.md` 与 `.github/copilot-instructions.md`；
- 当前尚未接入 project-side runtime pack。

如执行侧对该画像做有限调整，必须说明调整理由，并保持“单一 consumer repo、基本结构稳定、未来可接入入口组合”这三个约束不变。

---

## 5. Authorized Files / Areas

本轮仅授权以下写入范围：

- `skills/workflow-bootstrap/pilot_repo_validation_sketch.md`
- `skills/workflow-bootstrap/single_consumer_repo_file_layout_sketch.md`
- `skills/workflow-bootstrap/field_placeholder_mapping_sketch.md`（仅在确有必要时创建）
- `skills/workflow-bootstrap/README.md`（仅在必要时最小导航补充）
- `tasks/copilot-codex-workflow_phase3b_pilot_validation_sketch_execution_report.md`

授权边界说明：

- `README.md` 只允许最小导航性补充，不允许整篇重写。
- `field_placeholder_mapping_sketch.md` 只有在主文档无法清晰承载字段/占位符映射时才授权创建。
- 除上述路径外，默认无权限修改。
- Phase 2 / Phase 3A 相关 memo、report、draft、template sketch 仅作为输入参考，不在本轮修改范围内。

---

## 6. Expected Deliverables

### Deliverable 1

`skills/workflow-bootstrap/pilot_repo_validation_sketch.md`

这是一份本轮主文档，必须至少覆盖：

- 单一试点 consumer repo 画像；
- 为什么选择该画像做 Phase 3B 验证对象；
- 在该画像下，v1 入口组合是否成立；
- required / optional / deferred 分类在该画像中的判断；
- canonical backreference 在该画像中的稳健表达建议；
- anti-second-rulebook guardrails 在该画像中的应用方式；
- 明确哪些结论只是 validation sketch，而不是 implementation 决议。

该文档必须保持 sketch / validation 语气，不得写成真实 consumer repo 方案落地说明。

### Deliverable 2

`skills/workflow-bootstrap/single_consumer_repo_file_layout_sketch.md`

要求至少回答：

- 单一试点 consumer repo 在本轮验证中的文件布局画像；
- `AGENTS.md`、`.github/copilot-instructions.md`、可选 `.github/instructions/`、deferred `.github/agents/` 在画像中的相对位置如何表达；
- 哪些位置是 sketch-level 候选，而不是要立刻创建的真实文件；
- 哪些路径需要保持 placeholder 或 project-filled 状态。

该文档必须明确自己只是 file layout sketch，不是 consumer repo 变更计划。

### Deliverable 3

`skills/workflow-bootstrap/field_placeholder_mapping_sketch.md`（如有必要）

如果创建，要求至少回答：

- `AGENTS.md` 的 fixed fields、project-fill fields、placeholder fields 映射；
- `.github/copilot-instructions.md` 中哪些字段必须固定，哪些只能保留最小 project-filled 内容；
- 哪些字段应继续 deferred 到 implementation 阶段再解析；
- 如何用字段级约束防止 consumer repo 本地扩写成第二规则库。

如果不创建该文档，执行侧必须在 execution report 中说明为什么主文档已足以承载这部分内容。

### Deliverable 4

`tasks/copilot-codex-workflow_phase3b_pilot_validation_sketch_execution_report.md`

必须明确：

- 本轮新增或更新了哪些 canonical sketch / validation 文档；
- 本轮没有实现哪些东西；
- 本轮如何验证边界、画像、required/optional/deferred 分类与路径表达；
- 是否仍存在 deferred questions，以及为什么继续 defer。

### Deliverable 5

如确有必要，可对 `skills/workflow-bootstrap/README.md` 做最小导航补充。

允许内容仅限：

- 新增一个很小的 Phase 3B navigation 段；
- 指向新的 validation sketch 文档；
- 明确这些文档是 canonical-only validation assets；
- 明确它们不是已下发到 consumer repo 的真实 runtime pack 文件。

---

## 7. Validation / Acceptance

本轮以文档边界校验、画像一致性校验和表达稳健性校验为主，不要求 consumer repo、distribution 或工具链验证。

至少需要完成以下检查：

### A. Boundary Check

确认：

- 没有创建或修改任何真实 consumer repo；
- 没有创建真实 project-side `AGENTS.md`；
- 没有创建真实 `.github/copilot-instructions.md`；
- 没有进入 rollout / distribution / tooling / adapter changes；
- 所有新文档都停留在 canonical sketch / validation layer。

### B. Phase-Continuity Check

确认：

- Phase 3B 没有改写 Phase 2 的主入口与 thin-adapter 结论；
- Phase 3B 没有改写 Phase 3A 的 required / optional / deferred 基线，只做单仓画像验证；
- 所有新文档都明确承接既有阶段结论，而不是重新决策。

### C. Coverage Check

确认本轮 deliverables 已明确覆盖以下内容：

1. 单一试点 consumer repo 画像；
2. v1 入口组合成立性；
3. required / optional / deferred 分类验证；
4. `AGENTS.md` fixed/project-fill/placeholder 字段表达；
5. `.github/copilot-instructions.md` 的最薄边界；
6. canonical backreference 的稳健路径表达；
7. 防止第二规则库化的 guardrails。

### D. Acceptance Standard

验收通过标准为：

- 所有必需 deliverables 已存在；
- 文档明确只做 pilot validation sketch，不声称真实 implementation；
- 单一 consumer repo 画像清楚且稳定；
- 表述与既有阶段结论一致；
- 没有越界到 consumer repo 修改、distribution、rollout 或工具变更；
- execution report 清楚记录范围、未做事项、验证动作、deferred questions 与下一步建议。

---

## 8. Execution Report Requirements

执行完成后，必须输出结构化 execution report，至少包含：

1. Scope Restatement
2. Files Changed
3. Pilot Consumer Repo Profile Used
4. What Was Validated
5. What Was Explicitly Not Implemented
6. Boundary Check
7. Validation Notes
8. Risks / Assumptions
9. Deferred Questions
10. Recommended Next Step

回执中必须显式写出以下结论：

- 本轮只完成 canonical-layer pilot validation sketch；
- 未创建或修改真实 consumer repo 文件；
- 未进入 implementation / rollout / distribution / tooling / adapter changes；
- Phase 3B 只是为后续是否进入单仓 implementation 准备更稳的验证草案，而不是直接下发 runtime pack。

---

## 9. 推荐落盘路径

推荐落盘必须继续留在 canonical layer，而不是落到真实 consumer runtime surface。

推荐路径如下：

- `skills/workflow-bootstrap/pilot_repo_validation_sketch.md`
- `skills/workflow-bootstrap/single_consumer_repo_file_layout_sketch.md`
- `skills/workflow-bootstrap/field_placeholder_mapping_sketch.md`（仅在必要时创建）
- `skills/workflow-bootstrap/README.md`（仅在必要时最小补充）
- `tasks/copilot-codex-workflow_phase3b_pilot_validation_sketch_execution_report.md`

明确禁止的落盘路径：

- 任何真实 consumer repo 下的 `AGENTS.md`
- 任何真实 consumer repo 下的 `.github/copilot-instructions.md`
- 任何真实 consumer repo 下的 `.github/instructions/`
- 任何真实 consumer repo 下的 `.github/agents/`

一句话任务摘要：

**Phase 3B 只在 canonical layer 内，以一个单一 consumer repo 画像验证 future project-side runtime pack v1 的入口组合、required/optional/deferred 分类、字段/占位符表达、canonical backreference 稳健写法与 anti-expansion guardrails；不进入真实 implementation、rollout、distribution、consumer repo 修改或工具改动。**
