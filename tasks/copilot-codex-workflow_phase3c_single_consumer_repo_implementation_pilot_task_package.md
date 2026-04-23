# 任务包：Copilot 主控 / Codex 施工工作流（Phase 3C：single consumer repo implementation pilot）

## 任务标识

- task id: `WF-PHASE3C-SINGLE-CONSUMER-IMPLEMENTATION-PILOT-V1`
- 名称：Phase 3C / single consumer repo implementation pilot
- 阶段：`Phase 3C`
- 提交方：Planner
- 日期：`2026-04-23`
- 前置输入：
  - `tasks/copilot-codex-workflow_phase2_entrypoint_decision_memo.md`
  - `tasks/copilot-codex-workflow_phase2_execution_report.md`
  - `tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`
  - `tasks/copilot-codex-workflow_phase3b_pilot_validation_sketch_execution_report.md`
  - `skills/workflow-bootstrap/README.md`
  - `skills/workflow-bootstrap/agents_md_thin_entrypoint_draft.md`
  - `skills/workflow-bootstrap/copilot_instructions_thin_adapter_draft.md`
  - `skills/workflow-bootstrap/canonical_backreference_rules_draft.md`
  - `skills/workflow-bootstrap/project_side_runtime_pack_template_sketch.md`
  - `skills/workflow-bootstrap/project_side_agents_md_template_sketch.md`
  - `skills/workflow-bootstrap/project_side_copilot_instructions_template_sketch.md`
  - `skills/workflow-bootstrap/pilot_repo_validation_sketch.md`
  - `skills/workflow-bootstrap/single_consumer_repo_file_layout_sketch.md`
- 补充上下文：
  - `tasks/copilot-codex-workflow_phase3a_template_sketch_task_package.md`
  - `tasks/copilot-codex-workflow_phase3b_pilot_validation_sketch_task_package.md`

---

## 1. Scope Restatement

本轮进入 **single consumer repo 的真实 implementation pilot**，但仍然必须保持 bounded execution。

本轮不是 rollout，不是 distribution，不是 multi-repo adoption，也不是工具链改造。

本轮必须继续遵守 `workflow-bootstrap` 的既有 canonical 边界与既有结论：

- `AGENTS.md` 是 project-side 的最薄主入口。
- `.github/copilot-instructions.md` 是 Copilot-specific thin adapter。
- project-side entrypoints 必须强制回指 canonical guidance。
- project-side runtime pack 只能是入口层，不得演化为第二事实源。

本轮必须解决的核心问题是：

1. 选择一个真实 single consumer repo 作为 implementation pilot 对象，并明确它的基本画像与边界。
2. 只在该 pilot repo 中最小实现：
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
3. 验证这两个入口在真实 repo 中的最小落位是否成立。
4. 验证 canonical guidance 的路径回指在真实 repo 中如何具体落地。
5. 验证 `AGENTS.md` 的固定字段、项目自填字段、占位符字段在真实 repo 中如何填写。
6. 验证 `.github/copilot-instructions.md` 是否仍能保持 Copilot-specific thin adapter 的最薄边界。
7. 验证在真实 repo 中如何继续防止 project-side runtime pack 演化为第二规则库。
8. 明确本轮 implementation pilot 完成后，是否已满足进入下一阶段的条件。

执行前置条件：

- 若 pilot repo 尚未最终指定，执行侧必须先锁定目标 repo，再开始任何 implementation。
- 若无法锁定一个真实、可写、被授权的 single consumer repo，本轮不得伪造 implementation 结果，必须回执阻塞。

执行协议要求：

- 必须复用 `chatgpt-handoff-pilot` 的最小协议：先读取输入，再复述边界，再只在授权文件内做 bounded execution，最后输出 execution report。

---

## 2. 当前阶段承接关系（Phase 1 / Phase 2 / Phase 3A / Phase 3B / Phase 3C）

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
- project-side entrypoints 必须采用 forced backreference 机制；
- project-side runtime pack 不得膨胀为第二规则库。

### Phase 3A 已完成的事情

Phase 3A 已在 canonical layer 内完成 template sketch 收敛，并明确：

- v1 project-side runtime pack 以 `AGENTS.md` + `.github/copilot-instructions.md` 为 required entrypoint pair；
- `AGENTS.md` 的 fixed fields / project-fill fields；
- `.github/copilot-instructions.md` 的超薄职责边界；
- placeholder-based canonical backreference 写法；
- anti-expansion guardrails。

### Phase 3B 已完成的事情

Phase 3B 已完成 single consumer repo profile 的 validation sketch，并明确：

- 单仓画像下，v1 entrypoint pair 仍然成立；
- `.github/instructions/*.instructions.md` 仍然只是 optional；
- `.github/agents/*.agent.md` 仍然 deferred / not recommended in v1；
- 字段映射、路径回指与 anti-second-rulebook guardrails 在单仓画像中可操作。

### Phase 3C 本轮承接任务

Phase 3C 不重写既有阶段结论，只把前面已经收敛的结论推进到一个真实 single consumer repo 的最小 implementation pilot。

本轮的职责是：

- 把“validation sketch”推进到“真实 repo 中的最小落位”；
- 用一个真实 repo 验证 entrypoint pair、字段填写、路径回指与 anti-bloat guardrails 是否成立；
- 为后续是否进入下一阶段提供事实基础；
- 但不把本轮 pilot 误写成 rollout、distribution 或通用模板分发已完成。

---

## 3. Phase 3C 的 Goal / In Scope / Out of Scope

### Goal

在一个真实 single consumer repo 中，最小实现并验证 `AGENTS.md` 与 `.github/copilot-instructions.md` 两个入口文件，确认：

- entrypoint pair 能否在真实 repo 中稳定落位；
- canonical backreference 能否被具体、清晰地解析；
- `AGENTS.md` 与 Copilot adapter 的边界能否在 implementation 阶段仍保持足够薄；
- project-side runtime pack 是否仍然能被限制在“入口层”，而不是演化为第二规则库。

### In Scope

本轮允许完成以下事情：

1. 选择并锁定一个真实 single consumer repo 作为唯一 pilot 对象。
2. 记录该 pilot repo 的基础画像、约束、已有结构和实施边界。
3. 在该 pilot repo 中最小创建或最小更新：
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
4. 将 placeholder-based canonical backreference 解析为该真实 repo 中可执行的具体路径表达。
5. 在真实 repo 中填写 `AGENTS.md` 的 fixed fields、project-fill fields 与必要占位符收口策略。
6. 在真实 repo 中验证 `.github/copilot-instructions.md` 是否仍可保持为 Copilot-specific thin adapter。
7. 如确有必要，补充一份最小 implementation note 或 mapping note，用于记录本轮具体路径映射或无法直接内嵌到入口文件中的极少量实现说明。
8. 进行 bounded validation，并输出 execution report。

### Out of Scope

本轮明确不做以下事项：

1. 不进入 multi-repo rollout。
2. 不进入 distribution、bundle、export/import、sync 或通用模板分发。
3. 不修改 `sync / export / import / check` 相关现有工具逻辑。
4. 不修改 `skills/workflow-bootstrap/` 下的 canonical drafts、template sketches 或 validation sketches。
5. 不修改 `.agents/skills/`、`.github/skills/`、`skills_index.json`、`SKILLS_INDEX.md` 或任何 discoverability / adapter / index 层。
6. 不创建真实 `.github/instructions/*.instructions.md`。
7. 不创建真实 `.github/agents/*.agent.md`。
8. 不在 pilot repo 中顺手创建额外的 runtime-pack 文件族或 project-local rulebook。
9. 不把 single consumer repo pilot 写成“通用 rollout 已完成”或“项目侧 runtime pack 已定稿”。

---

## 4. Pilot Repo Selection Assumptions

执行侧必须显式写清 pilot repo 的选择条件，并在真正实施前完成目标 repo 锁定。

最低选择条件如下：

1. 必须是一个真实 consumer repo，而不是 `ai-skill-hub` 自身。
2. 必须是单一 repo 试点对象，本轮不允许同时触达多个 repo。
3. 必须已具备基本仓库结构，至少应有稳定的根目录与可容纳 `.github/` 的常规 Git repo 形态。
4. 必须具备实际写入授权；若无写权限或无明确授权，不得开始 implementation。
5. 优先选择尚未存在成熟 `AGENTS.md` 与 `.github/copilot-instructions.md` 体系的 repo，以保持 pilot 最小且可归因。
6. 优先选择不会立即触发 distribution、模板分发、工具改造或跨仓对齐需求的 repo。
7. 优先选择能清楚表达 canonical backreference 的 repo，即项目结构足以承载明确文件路径，而不是只能给出目录级模糊引用。

若 pilot repo 尚未最终指定，执行侧必须先完成以下动作：

1. 锁定一个候选 repo。
2. 用 3 到 8 行说明它为何满足上述条件。
3. 说明该 repo 的基本画像与已知边界。
4. 说明本轮是否为新建两个入口文件，还是对已有薄文件做最小更新。

阻塞条件：

- 若候选 repo 已存在复杂、成熟、不可轻易替换的 `AGENTS.md` 或 `.github/copilot-instructions.md`，执行侧不得直接覆盖，必须说明为何该 repo 不再适合作为本轮最小 pilot，或记录为阻塞并停止 implementation。
- 若候选 repo 需要额外 `.github/instructions/*`、`.github/agents/*`、distribution 资产或工具改造才能成立，则说明该 repo 不符合本轮最小 pilot 条件。

---

## 5. Authorized Files / Areas

### A. Pilot Repo 中授权写入的文件

本轮在真实 pilot repo 中，默认只授权以下文件：

1. `<pilot-repo>/AGENTS.md`
2. `<pilot-repo>/.github/copilot-instructions.md`

若 `.github/` 目录尚不存在，仅允许为了落位 `.github/copilot-instructions.md` 而创建该目录。

### B. 条件授权文件

仅在确有必要，且执行前已明确说明理由时，才允许额外创建一份最小 note：

1. `<pilot-repo>/<existing-docs-dir>/runtime-pack-implementation-note.md`
2. 或 `<pilot-repo>/<existing-docs-dir>/runtime-pack-mapping-note.md`

该 note 仅可用于：

- 记录真实 repo 中 canonical backreference 的具体路径映射；
- 记录两个入口文件无法承载、但本轮验收又必须保留的极少量 implementation 说明；
- 记录为什么本轮仍然没有进入更大 file family。

若没有上述硬性需要，则不得创建 note 文件。

### C. Hub 仓库中授权写入的文件

本轮仅允许在当前 `ai-skill-hub` 仓库中新增 execution report：

1. `tasks/copilot-codex-workflow_phase3c_single_consumer_repo_implementation_pilot_execution_report.md`

除 execution report 外，本轮不授权修改 hub 内其他 canonical、adapter、tooling、status 或 handoff 资产。

### D. 绝对禁止顺手创建或修改的文件/区域

1. 任何其他 consumer-repo runtime surfaces：
   - `<pilot-repo>/.github/instructions/*.instructions.md`
   - `<pilot-repo>/.github/agents/*.agent.md`
   - `<pilot-repo>/skills/**`
   - `<pilot-repo>/docs/HANDOFF.md`
2. 任何 distribution / bundle / sync / export / import / check 相关文件。
3. 任何 hub 内 `skills/workflow-bootstrap/` canonical 草案或模板文件。
4. 任何索引、适配、发现层文件：
   - `.agents/skills/**`
   - `.github/skills/**`
   - `skills_index.json`
   - `SKILLS_INDEX.md`
5. 任何与本轮 pilot 无关的项目级治理、状态、handoff 或工具文件。

---

## 6. Expected Deliverables

### Deliverable 1

一个真实 single consumer repo 中的 `AGENTS.md`。

要求至少覆盖：

- 主入口身份声明；
- required canonical reading list；
- fixed fields / project-fill fields 的真实填写结果；
- canonical wins on conflict；
- no-second-rulebook boundary；
- 足够薄的 high-level working rules。

### Deliverable 2

同一真实 repo 中的 `.github/copilot-instructions.md`。

要求至少覆盖：

- Copilot-specific thin adapter 身份声明；
- 对 `AGENTS.md` 的明确回指；
- 仅保留高频、高约束、Copilot-specific 的最薄提醒；
- 对完整 guidance 所在位置的具体文件路径回指；
- 明确不替代 `AGENTS.md`，也不复制完整 workflow / governance / skill guidance。

### Deliverable 3

如确有必要，一份最小 implementation note 或 mapping note。

只有在以下情况之一发生时才允许出现：

1. 真实 repo 的 canonical backreference 解析需要额外说明才可验收；
2. 两个入口文件无法在保持“超薄”前提下同时容纳必要的本轮 implementation 说明；
3. 执行侧需要明确记录为什么没有进入 `.github/instructions/*` 或其他更大 file family。

### Deliverable 4

`tasks/copilot-codex-workflow_phase3c_single_consumer_repo_implementation_pilot_execution_report.md`

必须明确：

- pilot repo 最终选定对象及其选择理由；
- 本轮实际创建或更新了哪些文件；
- 哪些文件明确没有创建；
- canonical backreference 在真实 repo 中如何具体落地；
- `AGENTS.md` 的 fixed/project-fill/placeholder 字段是如何填写与收口的；
- Copilot thin adapter 边界是否成立；
- anti-second-rulebook guardrails 是否成立；
- 本轮完成后是否满足进入下一阶段的条件。

---

## 7. Validation / Acceptance

本轮以真实 repo 中的最小 implementation validation 为主，但仍然必须保持 bounded。

至少需要完成以下检查：

### A. Pilot Repo Lock Check

确认：

1. 已锁定一个真实 single consumer repo。
2. 已说明该 repo 的基本画像与选择理由。
3. 已确认具备写入授权。
4. 已确认本轮不需要 multi-repo rollout 或 distribution 才能完成最小 pilot。

### B. File Placement Check

确认：

1. `AGENTS.md` 已在 pilot repo 根目录正确落位。
2. `.github/copilot-instructions.md` 已在 pilot repo 正确落位。
3. 除条件授权 note 外，没有新增其他 runtime-pack 文件族。

### C. Fixed / Project-Fill / Placeholder Check

确认：

1. `AGENTS.md` 中固定字段仍保持 canonical contract。
2. 项目自填字段已根据真实 repo 正确填写。
3. 占位符仅在确有必要时保留，并在 execution report 中解释其去留。
4. 没有因为填字段而把 `AGENTS.md` 扩写成完整规则库。

### D. Canonical Backreference Check

确认：

1. 回指使用具体文件路径，而不是目录级模糊引用。
2. 没有使用 host-specific 绝对路径。
3. 没有把 canonical guidance 复制进 project-side 文件。
4. 真实 repo 中的路径回指对执行侧是可理解、可操作的。

### E. Thin Adapter Check

确认：

1. `.github/copilot-instructions.md` 仍然是 Copilot-specific thin adapter。
2. 它没有重新成为主入口。
3. 它没有复制 `AGENTS.md` 或 canonical guidance 的大段内容。
4. 它只保留高频、高约束、Copilot-facing 的必要提醒。

### F. Anti-Second-Rulebook Check

确认：

1. 没有顺手创建 `.github/instructions/*.instructions.md`。
2. 没有顺手创建 `.github/agents/*.agent.md`。
3. 没有在 pilot repo 中复制 `skills/` 或其他 canonical payload 作为第二规则库。
4. 若出现 note 文件，其内容仍然是最小实现说明，而不是新的本地手册。

### G. Acceptance Standard

本轮验收通过标准为：

1. 一个真实 single consumer repo 已被锁定并完成最小 implementation pilot。
2. `AGENTS.md` 与 `.github/copilot-instructions.md` 已在真实 repo 中落位或最小更新成功。
3. canonical backreference 已被解析为具体、可执行的路径表达。
4. `AGENTS.md` 的字段填写与 `.github/copilot-instructions.md` 的 thin boundary 都经真实 repo 验证可成立。
5. 没有越界到 `.github/instructions/*`、`.github/agents/*`、distribution、multi-repo rollout 或工具改造。
6. execution report 已清楚记录本轮事实、边界遵守情况、验证结果与下一阶段判断。

### H. Next-Phase Entry Gate

只有在以下条件同时成立时，才可建议进入下一阶段：

1. 单仓最小 pilot 已在真实 repo 中成立。
2. entrypoint pair 在真实 repo 中没有立即诱发额外 file family 扩张。
3. canonical backreference 的具体落地方式清晰且可复用为后续实施经验。
4. `AGENTS.md` 与 Copilot adapter 的职责边界在真实 implementation 中仍然稳定。
5. execution report 明确显示：当前仍未进入 rollout、distribution 或工具链改造，但已有足够事实支持讨论下一阶段。

若任一条件不成立，则下一步应继续停留在 pilot follow-up 或局部修正层，不得直接升级为 rollout phase。

---

## 8. Execution Report Requirements

执行完成后，必须输出结构化 execution report，至少包含：

1. Scope Restatement
2. Pilot Repo Selected
3. Pilot Repo Profile and Boundaries
4. Files Changed
5. Concrete Canonical Backreference Mapping
6. Fixed / Project-Fill / Placeholder Resolution
7. What Was Explicitly Not Implemented
8. Validation Notes
9. Boundary Check
10. Risks / Assumptions
11. Phase Advancement Recommendation

回执中必须显式写出以下结论：

1. 本轮只完成一个真实 single consumer repo 的最小 implementation pilot。
2. 本轮未进入 multi-repo rollout。
3. 本轮未进入 distribution、通用模板分发或工具链改造。
4. 本轮未把 pilot 实现误写成通用 rollout 完成。
5. 若创建了 implementation note / mapping note，必须解释为什么它是必要且仍保持最小。
6. 必须明确回答：
   - 是否建议进入下一阶段；
   - 若建议进入，依据是什么；
   - 若不建议进入，卡点是什么。

---

## 9. 推荐落盘路径

本轮正式 task package 落盘路径：

- `tasks/copilot-codex-workflow_phase3c_single_consumer_repo_implementation_pilot_task_package.md`

本轮 execution report 推荐落盘路径：

- `tasks/copilot-codex-workflow_phase3c_single_consumer_repo_implementation_pilot_execution_report.md`

本轮真实 pilot repo 中的目标落位路径：

- `<pilot-repo>/AGENTS.md`
- `<pilot-repo>/.github/copilot-instructions.md`

仅在确有必要且预先声明时允许的附加路径：

- `<pilot-repo>/<existing-docs-dir>/runtime-pack-implementation-note.md`
- 或 `<pilot-repo>/<existing-docs-dir>/runtime-pack-mapping-note.md`

明确禁止误用的落盘方向：

- 不在多个 consumer repo 同步铺开；
- 不在 hub 内新增 distribution / adapter / tooling 产物；
- 不新增 `.github/instructions/*` 或 `.github/agents/*` 作为本轮顺手扩展；
- 不把本轮 pilot 的文件落位描述成通用 rollout 已完成。

一句话任务摘要：

**Phase 3C 只在一个真实 single consumer repo 中完成 `AGENTS.md` 与 `.github/copilot-instructions.md` 的最小 implementation pilot，验证字段填写、canonical backreference、thin-adapter 边界与 anti-second-rulebook guardrails；不进入 multi-repo rollout、distribution、通用模板分发或工具改造，并以 execution report 判断是否具备进入下一阶段的条件。**