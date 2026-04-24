# 任务包：Copilot 主控 / Codex 施工工作流（Phase 3D：canonical path calibration）

## 任务标识

- task id: `WF-PHASE3D-CANONICAL-PATH-CALIBRATION-V1`
- 名称：Phase 3D / canonical path calibration
- 阶段：`Phase 3D`
- 提交方：Planner
- 日期：`2026-04-24`
- 前置输入：
  - `tasks/copilot-codex-workflow_phase2_entrypoint_decision_memo.md`
  - `tasks/copilot-codex-workflow_phase2_execution_report.md`
  - `tasks/copilot-codex-workflow_phase3a_template_sketch_execution_report.md`
  - `tasks/copilot-codex-workflow_phase3b_pilot_validation_sketch_execution_report.md`
  - `tasks/copilot-codex-workflow_phase3c_single_consumer_repo_implementation_pilot_execution_report.md`
  - `skills/workflow-bootstrap/README.md`
  - `skills/workflow-bootstrap/canonical_backreference_rules_draft.md`
  - `skills/workflow-bootstrap/project_side_runtime_pack_template_sketch.md`
  - `skills/workflow-bootstrap/project_side_agents_md_template_sketch.md`
  - `skills/workflow-bootstrap/project_side_copilot_instructions_template_sketch.md`
  - `skills/workflow-bootstrap/pilot_repo_validation_sketch.md`
  - `AGENTS.md`
  - `.github/copilot-instructions.md`
- 补充上下文：
  - `tasks/copilot-codex-workflow_phase3c_single_consumer_repo_implementation_pilot_task_package.md`

---

## 1. Scope Restatement

本轮只做 **single consumer repo pilot 完成之后的 canonical path calibration**。

本轮不是 multi-repo rollout，不是 distribution，不是 adoption，不是 toolchain 改造，也不是“rollout-readiness 已完成”的宣布轮次。

本轮必须继续遵守 `workflow-bootstrap` 的既有 canonical 边界与 Phase 2 / 3A / 3B / 3C 已落定结论：

- `AGENTS.md` 是当前 project-side 的最薄主入口。
- `.github/copilot-instructions.md` 是 Copilot-specific thin adapter。
- canonical guidance 仍然优先。
- project-side runtime surface 仍然只能保持入口层，不得演化为第二规则库。

本轮必须解决的核心问题是：

1. 当前 pilot repo 中的 `<project-local-canonical-skill-path>` 是否需要实体化。
2. 如果需要实体化，应该落在哪里，采用什么最小路径结构。
3. 如果暂不实体化，占位符路径应如何从“临时占位”收敛为“受控占位表达”。
4. `AGENTS.md` 中 canonical guidance 的回指，应该如何从当前写法收敛为更稳定的真实路径表达或受控占位表达。
5. `.github/copilot-instructions.md` 对 `AGENTS.md` 的回指是否需要进一步收紧。
6. 如何在 path calibration 后继续确保：
   - canonical guidance 优先；
   - project-side 不形成第二规则库；
   - 当前 pilot 结论不会被误写成 multi-repo 通用定稿。

本轮只做 path calibration，不做：

- 新文件族扩展；
- `.github/instructions/*.instructions.md` 引入；
- `.github/agents/*.agent.md` 引入；
- rollout / distribution / tool changes；
- 对既有阶段主结论的重写。

---

## 2. 当前阶段承接关系（Phase 1 / Phase 2 / Phase 3A / Phase 3B / Phase 3C / Phase 3D）

### Phase 1 已完成的事情

Phase 1 已在 canonical layer 内确立 `Copilot 主控 / Codex 施工` 的 workflow shell，并明确：

- `planner / implementer / reviewer` 的最小角色分工；
- `skills/` 是唯一 canonical source；
- future runtime pack 只作为项目侧目标映射，不在该阶段落地。

### Phase 2 已完成的事情

Phase 2 已锁定 entrypoint 级结论：

- `AGENTS.md` 作为 future project-side runtime pack 的最薄主入口；
- `.github/copilot-instructions.md` 作为 Copilot-specific thin adapter；
- forced canonical backreference 是必需机制；
- project-side 不能膨胀为第二规则库。

### Phase 3A 已完成的事情

Phase 3A 已把上述结论收敛为 canonical template sketch，并明确：

- v1 入口对以 `AGENTS.md` + `.github/copilot-instructions.md` 为 required；
- `AGENTS.md` 的 fixed fields / project-fill fields；
- `.github/copilot-instructions.md` 的超薄边界；
- placeholder-based canonical path 表达仍可接受于 sketch 阶段。

### Phase 3B 已完成的事情

Phase 3B 已在单一 consumer repo 画像上完成 validation sketch，并明确：

- v1 entrypoint pair 在单仓画像下成立；
- `.github/instructions/*.instructions.md` 仍为 optional；
- `.github/agents/*.agent.md` 仍应 deferred；
- placeholder-first 的 path strategy 在 implementation 前仍可成立。

### Phase 3C 已完成的事情

Phase 3C 已在一个真实 single consumer repo context 中完成最小 implementation pilot，并验证：

- `AGENTS.md` 已可在真实 repo 中作为最薄主入口落位；
- `.github/copilot-instructions.md` 已可在真实 repo 中作为 Copilot-specific thin adapter 落位；
- concrete canonical backreference paths 已可在真实 repo 中表达；
- fixed fields / project-fill fields / placeholder fields 已在真实 repo 中得到 implementation 级验证；
- `<project-local-canonical-skill-path>` 仍被保留为 intentionally unresolved placeholder。

### Phase 3D 本轮承接任务

Phase 3D 不再讨论“主入口选谁”或“entrypoint pair 是否成立”。

Phase 3D 只承接 Phase 3C 的真实 pilot 结果，继续推进到：

- 对当前 pilot repo 的 canonical path strategy 做校准；
- 判断 `<project-local-canonical-skill-path>` 应实体化、受控保留，还是收敛到其他最小可控表达；
- 判断 `AGENTS.md` 与 `.github/copilot-instructions.md` 的 backreference wording 是否需要最小收紧；
- 为后续是否进入更广的 readiness 评估提供更稳的 path-level 事实基础。

Phase 3D 仍然不是 multi-repo rollout，也不是 distribution 准备完成事实。

---

## 3. Phase 3D 的 Goal / In Scope / Out of Scope

### Goal

在当前 single consumer repo pilot 的真实落地基础上，完成一轮 **canonical path calibration**，把“可用但尚未完全收敛”的 path/backreference 表达校准为：

- 真实路径表达；
- 或受控占位表达；
- 或经比较后仍维持当前占位策略但附带明确 guardrail。

### In Scope

本轮允许完成以下事情：

1. 读取并比较 Phase 2 / 3A / 3B / 3C 的 path-related 结论与当前 pilot repo 实际入口文件写法。
2. 判断 `<project-local-canonical-skill-path>` 在当前 pilot repo 中是否需要实体化。
3. 若需要实体化，提出并比较最小可控路径选项，并收敛到一个推荐方案。
4. 若不需要实体化，提出并固定当前占位策略的受控写法，防止长期漂移。
5. 判断 `AGENTS.md` 当前 canonical guidance 回指是否需要最小 wording adjustment。
6. 判断 `.github/copilot-instructions.md` 当前对 `AGENTS.md` 与 canonical guidance 的回指是否需要最小收紧。
7. 如证据明确支持，允许对当前已存在的：
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
   做**极小、path-only、backreference-only** 的 wording calibration。
8. 输出 canonical calibration deliverables 与 execution report。

### Out of Scope

本轮明确不做以下事项：

1. 不进入 multi-repo rollout。
2. 不进入 distribution / adoption / template broadcast。
3. 不新增更大的 project-side runtime surface。
4. 不新增真实 `.github/instructions/*.instructions.md`。
5. 不新增真实 `.github/agents/*.agent.md`。
6. 不修改现有 `sync / export / import / check` 工具逻辑。
7. 不修改 `.agents/skills/`、`.github/skills/`、`skills_index.json`、`SKILLS_INDEX.md` 或其他 discoverability / distribution surfaces。
8. 不把当前 pilot repo 的实现包装成通用 final template。
9. 不把 path calibration 写成 rollout-readiness 已完成事实。

---

## 4. 核心校准问题清单

执行侧必须围绕以下问题显式给出结论，不允许只给模糊建议：

1. 当前 pilot repo 是否已经具备足够条件去实体化 `<project-local-canonical-skill-path>`。
2. 若实体化，推荐路径应属于哪一类：
   - repo-local path；
   - project-local canonical payload path；
   - 还是其他最小可控路径。
3. 若实体化，最小路径结构应如何表达，为什么不会误导后续执行侧把它复制成更大的本地规则面。
4. 若不实体化，当前占位策略应如何固定写法，才能避免长期漂移、目录级模糊引用或错误复制 canonical guidance。
5. `AGENTS.md` 中 canonical guidance 的回指是否应从当前“placeholder kept intentionally”收敛为：
   - 全部真实路径；
   - 部分真实路径 + 一个受控占位；
   - 还是继续保留当前占位，但需要更严格 wording。
6. `.github/copilot-instructions.md` 对 `AGENTS.md` 的回指是否还需要进一步收紧。
7. 哪些字段必须由项目维护者手工确认，而不能由执行侧 AI 擅自定稿。
8. 哪些位置最容易发生 path drift、误复制 canonical guidance、或把 pilot repo 写成第二规则库。

执行侧必须在主 deliverables 中显式回答以下问题：

- 当前 pilot repo 是否已经具备足够条件去实体化 canonical path。
- 若实体化，路径应是 repo-local path、project-local canonical payload path，还是其他最小可控路径。
- 若不实体化，当前占位策略应如何固定写法。
- 哪些字段必须由项目维护者手工确认。
- 哪些地方最容易导致路径漂移或错误复制 canonical guidance。

---

## 5. Authorized Files / Areas

本轮仅授权以下写入范围：

### A. Canonical calibration deliverables

- `skills/workflow-bootstrap/project_side_canonical_path_calibration_memo.md`
- `skills/workflow-bootstrap/project_side_canonical_path_option_comparison_sketch.md`
- `skills/workflow-bootstrap/project_side_backreference_wording_adjustment_note.md`（仅在确有必要时创建）

### B. Current pilot repo existing entry files（条件授权）

仅当 memo / option comparison 已形成明确结论，且最小 wording adjustment 能直接降低 path ambiguity 时，才允许最小修改：

- `AGENTS.md`
- `.github/copilot-instructions.md`

这些修改必须满足：

- 只能是 path / backreference wording calibration；
- 不得新增新 section；
- 不得把文件扩写成更厚的本地规则文本；
- 不得引入新的 project-side 文件族。

### C. Execution report

- `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_execution_report.md`

### D. 明确未授权区域

本轮默认无权修改以下路径或区域：

- `skills/workflow-bootstrap/README.md`
- 任何其他 `skills/workflow-bootstrap/*.md`
- `.agents/skills/**`
- `.github/skills/**`
- `skills_index.json`
- `SKILLS_INDEX.md`
- `tools/**`
- `docs/**`
- 任何新的 `.github/instructions/**`
- 任何新的 `.github/agents/**`

---

## 6. Expected Deliverables

### Deliverable 1

`skills/workflow-bootstrap/project_side_canonical_path_calibration_memo.md`

这是本轮主文档，要求至少覆盖：

- 当前 pilot repo 的 path calibration 目标与边界；
- `<project-local-canonical-skill-path>` 是否需要实体化的判断；
- 当前 `AGENTS.md` / `.github/copilot-instructions.md` 中 backreference 写法的优点、局限与漂移风险；
- 推荐 path strategy；
- canonical guidance 优先与 anti-second-rulebook guardrails 如何在 path calibration 后继续成立；
- 明确写出：本轮只做 single consumer repo pilot 后的 calibration，不是 multi-repo ready 结论。

### Deliverable 2

`skills/workflow-bootstrap/project_side_canonical_path_option_comparison_sketch.md`

要求至少比较以下选项：

1. 保持 `<project-local-canonical-skill-path>` 为受控占位；
2. 将其实体化为明确 repo-local path；
3. 将其实体化为 project-local canonical payload path；
4. 如有必要，其他最小可控路径方案。

每个选项至少要说明：

- 适用条件；
- 优点；
- 风险；
- 对 drift / duplication / wrong-copy 的影响；
- 是否需要项目维护者手工确认；
- 推荐程度。

### Deliverable 3

`skills/workflow-bootstrap/project_side_backreference_wording_adjustment_note.md`（仅在确有必要时创建）

该 note 仅用于记录：

- 若当前 `AGENTS.md` 或 `.github/copilot-instructions.md` 需要最小 wording calibration，建议如何改；
- 为什么这些调整是 path calibration 所必需；
- 为什么这些调整不会把本轮升级成更大的 project-side runtime expansion。

如果执行侧直接对现有 `AGENTS.md` / `.github/copilot-instructions.md` 做了最小 wording adjustment，则仍需在 execution report 中说明是否还需要该 note；若不需要，必须解释原因。

### Deliverable 4

如证据明确支持，可对以下现有文件做最小 calibration：

- `AGENTS.md`
- `.github/copilot-instructions.md`

若执行侧选择修改，必须做到：

- 只收紧 backreference wording；
- 不引入第二规则库内容；
- 不新增新的 canonical payload 文本；
- 不改变 Phase 3C 已确认的主入口 / 薄适配职责分工。

### Deliverable 5

`tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_execution_report.md`

必须明确记录：

- 本轮读了哪些前序输入；
- 当前 pilot repo 是否具备实体化 canonical path 的条件；
- 最终推荐的 path strategy 是什么；
- 是否修改了 `AGENTS.md` / `.github/copilot-instructions.md`；
- 哪些事情明确没有做；
- 本轮为什么仍然不是 rollout / distribution / readiness completion。

---

## 7. Validation / Acceptance

本轮以 path-level consistency check、boundary check、和 wording-thinness check 为主。

至少需要完成以下检查：

### A. Calibration Coverage Check

确认 deliverables 已明确覆盖：

1. `<project-local-canonical-skill-path>` 是否需要实体化；
2. 若实体化，推荐路径类型与最小路径结构；
3. 若不实体化，占位策略的固定写法；
4. `AGENTS.md` backreference 的收敛建议；
5. `.github/copilot-instructions.md` 回指是否需要进一步收紧；
6. maintainer hand-confirm items；
7. drift / wrong-copy / duplication risk points。

### B. Boundary Check

确认：

1. 未进入 multi-repo rollout；
2. 未进入 distribution；
3. 未新增 `.github/instructions/*.instructions.md`；
4. 未新增 `.github/agents/*.agent.md`；
5. 未修改 `sync / export / import / check` 工具逻辑；
6. 未把 Phase 3D 写成 rollout-readiness 已完成事实。

### C. Thinness Check

若本轮修改了 `AGENTS.md` 或 `.github/copilot-instructions.md`，必须确认：

1. `AGENTS.md` 仍是 dispatch-oriented / reference-first / intentionally thin；
2. `.github/copilot-instructions.md` 仍是 Copilot-specific thin adapter；
3. 两者都没有变成第二规则库；
4. canonical guidance 优先级没有被削弱。

### D. Acceptance Standard

验收通过标准为：

1. 正式 task package 授权的 deliverables 已存在；
2. 执行侧已明确回答所有核心校准问题；
3. 推荐 path strategy 清晰，不是空泛建议；
4. 若修改了现有入口文件，这些修改保持极小且只限 backreference wording；
5. 回执清楚写出本轮仍然只是 single consumer repo pilot follow-up calibration；
6. 没有越界到 rollout / distribution / new file family / tool changes。

---

## 8. Execution Report Requirements

执行完成后，必须输出结构化 execution report，至少包含：

1. Scope Restatement
2. Current Phase Continuity
3. Files Changed
4. Current Pilot Repo Inputs Used
5. Calibration Questions Answered
6. Path Option Comparison Summary
7. Decision / Recommendation
8. What Was Explicitly Not Implemented
9. Validation Notes
10. Risks / Assumptions
11. Maintainer Confirmation Items
12. Recommended Next Step

回执中必须显式写出以下结论：

1. 本轮只完成 canonical path calibration。
2. 本轮未进入 multi-repo rollout。
3. 本轮未进入 distribution。
4. 本轮未改 sync / export / import / check 工具逻辑。
5. 本轮未新增更大的 project-side runtime surface。
6. 本轮未把 current pilot repo 的实现包装成通用 final template。
7. 本轮未把 path calibration 写成 rollout readiness 已完成。

若执行侧判断“当前还不应实体化 `<project-local-canonical-skill-path>`”，必须明确说明：

- 为什么不应实体化；
- 当前占位策略的固定写法是什么；
- 未来什么条件满足时才值得再次讨论实体化。

若执行侧判断“当前已经可以实体化”，必须明确说明：

- 为什么当前条件已足够；
- 推荐落在哪里；
- 哪些字段仍需项目维护者手工确认。

---

## 9. 推荐落盘路径

本轮正式 task package 落盘路径：

- `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_task_package.md`

本轮推荐 deliverables 落盘路径：

- `skills/workflow-bootstrap/project_side_canonical_path_calibration_memo.md`
- `skills/workflow-bootstrap/project_side_canonical_path_option_comparison_sketch.md`
- `skills/workflow-bootstrap/project_side_backreference_wording_adjustment_note.md`（仅在必要时创建）
- `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_execution_report.md`

本轮条件授权的现有 pilot repo 文件：

- `AGENTS.md`
- `.github/copilot-instructions.md`

本轮明确禁止的落盘方向：

- 任何新的 `.github/instructions/*.instructions.md`
- 任何新的 `.github/agents/*.agent.md`
- 任何 distribution / rollout / adapter / tooling 产物
- 任何将当前 pilot repo 包装成 multi-repo 通用 final template 的文档写法

一句话任务摘要：

**Phase 3D 只在当前 single consumer repo pilot 的真实落地基础上，完成 canonical path calibration，收敛 `<project-local-canonical-skill-path>` 与 backreference wording 的表达策略，并在必要时对现有 `AGENTS.md` 与 `.github/copilot-instructions.md` 做极小 path-only 校准；不进入 multi-repo rollout、distribution、tool changes 或更大的 project-side runtime surface。**
