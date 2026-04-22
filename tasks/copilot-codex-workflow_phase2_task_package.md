# 任务包：Copilot 主控 / Codex 施工工作流（Phase 2：AGENTS.md / copilot-instructions 薄入口草案）

## 任务标识

- task id: `WF-PHASE2-THIN-ENTRYPOINT-DRAFT-V1`
- 名称：Phase 2 / project-side 薄入口草案最小落地
- 阶段：`Phase 2`
- 提交方：Planner
- 日期：`2026-04-22`
- 前置输入：
  - `tasks/copilot-codex-workflow_phase2_entrypoint_decision_memo.md`
  - `tasks/copilot-codex-workflow_task_package_v1.md`
  - `tasks/copilot-codex-workflow_phase1_execution_report.md`
  - `skills/workflow-bootstrap/README.md`
  - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
  - `skills/workflow-bootstrap/role_split_and_integration.md`

---

## 1. 背景

Phase 1 已完成 `workflow-bootstrap` 的 canonical 最小落地，当前仓库已经具备：

- workflow 壳层 skill
- role split 说明
- canonical layer 与 future runtime pack 的映射说明
- 最小 discoverability / adapter 入口
- execution report 与验证留痕

进入 Phase 2 前，已通过决策稿明确两项关键结论：

1. future project-side runtime pack 的**最薄主入口**，优先选择 `AGENTS.md`
2. `.github/copilot-instructions.md` 作为 **Copilot-specific thin adapter**
3. project-side 入口层必须**强制回指 canonical guidance**
4. project-side runtime pack 只能作为入口层，**不得演化为第二事实源**

本轮任务不是实现完整 runtime pack，也不是把 project-side 文件族真实落到 hub 根目录。  
本轮只做 **AGENTS.md / `.github/copilot-instructions.md` 的薄入口草案**，并把“强制回指 canonical guidance”的固定表达收敛为可复用草案。

---

## 2. 本轮目标

在不进入完整 project-side 模板实现的前提下，完成以下最小落地：

1. 为 future project-side runtime pack 形成一份 **`AGENTS.md` 最薄主入口草案**
2. 为 future project-side runtime pack 形成一份 **`.github/copilot-instructions.md` 最薄适配层草案**
3. 形成一份 **canonical guidance 强制回指规则草案**
4. 将这些草案明确收纳在 `workflow-bootstrap` canonical skill 范围内
5. 在必要时对 `workflow-bootstrap/README.md` 做最小补充，使其能引用这些草案
6. 输出 execution report

---

## 3. 本轮核心问题

本轮执行侧需要收敛的不是“实现多少文件”，而是以下三类结构问题：

### A. `AGENTS.md` 作为主入口，最薄应薄到什么程度
需要明确：
- 它必须包含什么
- 它不应包含什么
- 它如何声明自己不是 canonical source

### B. `.github/copilot-instructions.md` 作为 Copilot-specific thin adapter，最薄应如何表达
需要明确：
- 它只保留哪些高频规则
- 它如何强制回指 `AGENTS.md`
- 它如何避免膨胀成第二规则库

### C. canonical guidance 的强制回指机制应如何固定表达
需要明确：
- 入口身份声明
- 必读 canonical 清单
- 冲突优先级声明
- 禁止扩写为第二规则库的约束

---

## 4. 本次范围（In Scope）

### 允许新增的 canonical 草案文件

仅允许在 `skills/workflow-bootstrap/` 下新增以下文件：

- `skills/workflow-bootstrap/agents_md_thin_entrypoint_draft.md`
- `skills/workflow-bootstrap/copilot_instructions_thin_adapter_draft.md`
- `skills/workflow-bootstrap/canonical_backreference_rules_draft.md`

### 允许修改的已有文件

仅在必要时允许最小修改以下文件：

- `skills/workflow-bootstrap/README.md`

修改目的仅限于：
- 补一段简短导航或引用
- 说明这些草案文件属于 Phase 2 canonical draft assets
- 明确它们不是当前 project-side runtime pack 已实现事实

### 允许新增的回执文件

- `tasks/copilot-codex-workflow_phase2_execution_report.md`

---

## 5. 明确不做（Out of Scope）

### 不创建真实 project-side runtime pack 文件

本轮**不得**直接创建：

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`
- `.github/agents/*.agent.md`

### 不进入完整模板体系

本轮**不得**：
- 设计全量 runtime pack 文件族模板
- 设计 path-specific instructions 细分模板
- 设计 custom agent 正式模板
- 进入 project-side rollout

### 不改现有核心契约与工具逻辑

本轮**不得**：
- 修改 `chatgpt-handoff-pilot` 等既有 skill 的核心执行契约
- 修改 `tools/sync_skills_to_nongit_project.ps1`
- 修改 `tools/export_bundle.ps1`
- 修改 `tools/import_bundle.ps1`
- 修改 `tools/check_adapter_consistency.py`
- 修改任何索引生成逻辑

### 不新增 discoverability / adapter 入口

本轮新增的是 canonical draft assets，  
不是新 skill，  
因此**不新增**：
- `.agents/skills/*`
- `.github/skills/*`
- `SKILLS_INDEX.md`
- `skills_index.json`

---

## 6. 授权文件与目录（Authorized Files / Areas）

仅授权以下路径：

- `skills/workflow-bootstrap/README.md`
- `skills/workflow-bootstrap/agents_md_thin_entrypoint_draft.md`
- `skills/workflow-bootstrap/copilot_instructions_thin_adapter_draft.md`
- `skills/workflow-bootstrap/canonical_backreference_rules_draft.md`
- `tasks/copilot-codex-workflow_phase2_execution_report.md`

除此之外，默认无权限修改。

---

## 7. 期望交付（Expected Deliverables）

### Deliverable 1
`agents_md_thin_entrypoint_draft.md`

要求：
- 明确 `AGENTS.md` 的定位是 **project-side 主入口**
- 明确它不是 canonical source of truth
- 给出最薄建议结构
- 给出建议固定文案
- 给出必须包含项 / 明确禁止项
- 明确它如何回指 canonical guidance
- 明确它如何避免变成第二规则库

### Deliverable 2
`copilot_instructions_thin_adapter_draft.md`

要求：
- 明确 `.github/copilot-instructions.md` 的定位是 **Copilot-specific thin adapter**
- 明确它不是主入口
- 给出建议最薄结构
- 给出建议固定文案
- 明确它只保留高频高约束规则
- 明确它如何回指 `AGENTS.md`
- 明确它不应扩写成完整规则库

### Deliverable 3
`canonical_backreference_rules_draft.md`

要求：
- 形成可复用的“强制回指 canonical guidance”规则草案
- 至少包含以下四类规则：
  1. 入口身份声明
  2. 必读 canonical 清单
  3. 冲突优先级声明
  4. 禁止扩写为第二规则库
- 表达尽量接近未来可直接复用的固定文案

### Deliverable 4
必要时更新 `skills/workflow-bootstrap/README.md`

要求：
- 只做最小导航性补充
- 不重写全文
- 不把这些 Phase 2 草案误写成已正式下发到项目侧的 runtime pack

### Deliverable 5
`tasks/copilot-codex-workflow_phase2_execution_report.md`

要求：
- 说明改了什么
- 明确没改什么
- 明确本轮只形成 canonical drafts
- 明确未进入真实 project-side runtime pack 实现
- 说明验证动作和边界判断

---

## 8. 文件内容要求

### 8.1 `agents_md_thin_entrypoint_draft.md`

必须覆盖以下内容：

#### A. 定位
- `AGENTS.md` 是 project-side 统一主入口
- 它是 dispatch-oriented / reference-first / thin-entrypoint
- 它不是 canonical source

#### B. 建议结构
至少建议包含以下 section：
- Purpose
- Canonical Guidance
- High-Level Working Rules
- Boundaries
- Conflict Resolution

#### C. 必须包含的固定机制
- 身份声明
- 必读 canonical 文件清单
- 冲突时 canonical guidance 优先
- 禁止把本文件扩写成完整规则库

#### D. 明确禁止项
例如：
- 不复制整套 canonical guidance
- 不承载完整 docs governance
- 不承载完整 workflow 手册
- 不替代 skill 文档

### 8.2 `copilot_instructions_thin_adapter_draft.md`

必须覆盖以下内容：

#### A. 定位
- `.github/copilot-instructions.md` 是 Copilot-specific thin adapter
- 它不是 project-side 主入口
- 它必须回指 `AGENTS.md`

#### B. 建议结构
至少建议包含：
- Purpose
- High-Frequency Rules
- Where Full Guidance Lives

#### C. 明确保留内容
只建议保留：
- 最高频规则
- 最高约束规则
- 回指 `AGENTS.md`
- 回指 canonical guidance

#### D. 明确禁止项
例如：
- 不复制完整 workflow 说明
- 不复制完整 docs governance
- 不扩成第二规则库
- 不代替 `AGENTS.md`

### 8.3 `canonical_backreference_rules_draft.md`

必须覆盖以下内容：

#### A. 规则本体
用清晰标题写出四件套：
- entrypoint identity
- required canonical reading list
- canonical wins on conflict
- no second rulebook

#### B. 可直接复用文案
至少给出：
- `AGENTS.md` 可复用固定文案草案
- `.github/copilot-instructions.md` 可复用固定文案草案

#### C. 适用边界
明确：
- 适用于 future project-side runtime pack
- 当前 hub 内仅作为 canonical draft asset 保存
- 不代表这些 project-side 文件已存在

### 8.4 `README.md` 最小补充要求

若你判断需要更新 `skills/workflow-bootstrap/README.md`，则只能：

- 增加一个很小的 Phase 2 draft assets 导航段
- 列出新增三个草案文件
- 一句话说明这些草案用于 future project-side runtime pack 设计
- 明确它们不是当前仓库已实现的 project-side runtime files

---

## 9. 推荐执行顺序（Recommended Execution Sequence）

1. 读取：
   - `tasks/copilot-codex-workflow_phase2_entrypoint_decision_memo.md`
   - `skills/workflow-bootstrap/README.md`
   - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
   - `skills/workflow-bootstrap/role_split_and_integration.md`

2. 复述：
   - 本轮要做什么
   - 本轮明确不做什么
   - 将修改哪些文件

3. 先写：
   - `canonical_backreference_rules_draft.md`

4. 再写：
   - `agents_md_thin_entrypoint_draft.md`

5. 再写：
   - `copilot_instructions_thin_adapter_draft.md`

6. 只在必要时对 `README.md` 做最小导航补充

7. 输出 execution report

---

## 10. 执行规则（Execution Rules）

本轮必须继续遵守 bounded execution：

1. 动手前先复述目标、边界、白名单文件
2. 仅在授权路径内修改
3. 不顺手改任何工具、索引、adapter、其他 skill
4. 不把 draft 写成已实现事实
5. 不把 future runtime pack 草案写成当前可分发资产
6. 遇到命名、措辞不确定时，采用最保守实现
7. 发现范围外问题，只记录到 execution report，不修复

---

## 11. 验证与验收（Validation / Acceptance）

本轮不要求复杂脚本验证，  
因为本轮只涉及 canonical draft documents 与最小 README 导航补充。

至少完成以下检查并在回执中报告：

### 文档边界检查
确认：
- 没有创建真实 `AGENTS.md`
- 没有创建真实 `.github/copilot-instructions.md`
- 没有创建 `.github/instructions/*.instructions.md`
- 没有创建 `.github/agents/*.agent.md`

### 一致性检查
确认：
- 三份 Phase 2 草案与 Phase 2 决策稿一致
- 与 Phase 1 的 canonical / runtime pack 分层不冲突
- README 如有更新，只是最小导航补充

### 表达检查
确认：
- 明确写出 `AGENTS.md` 是主入口
- 明确写出 `.github/copilot-instructions.md` 是 Copilot thin adapter
- 明确写出 canonical guidance 冲突优先级
- 明确写出禁止形成第二规则库

验收通过标准：

- 三份草案文件都存在
- 草案表达与决策稿一致
- 没有越界进入真实 runtime pack 实现
- 没有扩展到 path-specific instructions 或 custom agents 模板
- execution report 清晰记录边界与结果

---

## 12. 执行回执要求（Execution Report Requirements）

执行完成后必须输出结构化回执，至少包含：

1. Scope Restatement
2. Files Changed
3. What Was Drafted
4. What Was Explicitly Not Implemented
5. Boundary Check
6. Risks / Assumptions
7. Recommended Next Step

回执中必须显式说明：

- 本轮只形成 canonical draft assets
- 未实现真实 project-side runtime pack
- 未进入 rollout / distribution / template pack 阶段

---

## 13. 最小下一步方向

本轮完成后，下一步才适合评估是否进入：

- Phase 2-B：最小 project-side template sketch
  或
- Phase 3：distribution / adoption / validation 准备

但本轮不得提前进入这些阶段。

---

## 14. 一句话任务摘要

**本轮只做三份 canonical drafts：`AGENTS.md` 主入口草案、`.github/copilot-instructions.md` 薄适配草案、canonical guidance 强制回指规则草案；不实现真实 project-side runtime pack。**