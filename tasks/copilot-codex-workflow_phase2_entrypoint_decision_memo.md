# 决策稿：Phase 2 / project-side runtime pack 最薄主入口选择

## 决策标识

- decision id: `WF-PHASE2-ENTRYPOINT-DECISION-V1`
- 主题：project-side runtime pack 最薄主入口与 canonical guidance 回指机制
- 关联主线：`Copilot 主控 / Codex 施工` workflow bootstrap
- 前置输入：
  - `tasks/copilot-codex-workflow_task_package_v1.md`
  - `tasks/copilot-codex-workflow_phase1_execution_report.md`
  - `skills/workflow-bootstrap/README.md`
  - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
  - `skills/workflow-bootstrap/role_split_and_integration.md`

---

## 1. 决策问题

Phase 1 已在 hub 内完成 `workflow-bootstrap` 的 canonical 最小落地。  
进入 Phase 2 前，需要先收敛两个关键问题：

1. future project-side runtime pack 的**最薄主入口**应选择：
   - `AGENTS.md`
   - 还是 `.github/copilot-instructions.md`

2. project-side 主入口应如何**强制回指 canonical guidance**，避免项目侧 runtime pack 演化为第二事实源。

---

## 2. 决策结论

### 2.1 主结论

**future project-side runtime pack 的最薄主入口，优先选择 `AGENTS.md`。**

### 2.2 配套结论

`.github/copilot-instructions.md` 不作为主入口，  
而是作为 **Copilot-specific thin adapter** 存在。

### 2.3 结构性结论

project-side runtime pack 在入口层应采用以下层级：

1. `AGENTS.md`
   - 作为项目侧统一主入口
   - 面向跨 agent / 跨执行上下文的最小调度说明

2. `.github/copilot-instructions.md`
   - 作为 Copilot 专用超薄适配层
   - 仅保留最高频、最高约束规则
   - 强制回指 `AGENTS.md`

3. `.github/instructions/*.instructions.md`
   - 仅在确有必要时按主题或路径细分
   - 不承担主入口角色

4. `.github/agents/*.agent.md`
   - 仅作为角色化快捷入口
   - 不承担 canonical guidance 本体

---

## 3. 为什么选择 `AGENTS.md` 作为最薄主入口

### 3.1 跨工具一致性更强

当前默认 workflow 不是单一 Copilot-only 场景，  
而是：

- Copilot 主控
- Codex 施工

因此主入口不应只服务于 Copilot。  
`AGENTS.md` 更适合作为跨 agent、跨执行上下文的统一入口。

### 3.2 与当前 workflow 目标更一致

本次建设目标不是做一套只在 GitHub Copilot 内部成立的 repo instructions，  
而是要在项目侧形成一层：

- 可供 planner 理解
- 可供 implementer 遵循
- 可供 reviewer 校验

的最薄入口。  
`AGENTS.md` 更适合承担这个角色。

### 3.3 有利于控制 project-side 膨胀

如果把 `.github/copilot-instructions.md` 设成主入口，  
则项目侧规范会天然偏向 Copilot-only 表达，容易把项目内说明扩写成第二套局部规则系统。

将 `AGENTS.md` 设为主入口，有利于把 `.github/copilot-instructions.md` 压缩为**薄适配层**，避免 project-side runtime pack 过厚。

---

## 4. 为什么 `.github/copilot-instructions.md` 不作为主入口

### 4.1 它应保留为 Copilot-specific adapter

`.github/copilot-instructions.md` 更适合作为：

- repo-wide Copilot 入口
- 高优先级高频规则摘要
- 对 `AGENTS.md` 和 canonical skills 的快捷回指

而不是完整规则本体。

### 4.2 若它承担主入口角色，容易产生两个风险

#### 风险 A：Copilot-centric 偏移
会把 project-side runtime pack 设计成 Copilot 中心，而不是 workflow 中心。

#### 风险 B：说明文件膨胀
容易把详细规范不断堆到 `.github/copilot-instructions.md` 中，  
进而削弱 canonical skill 的中心地位。

---

## 5. 强制回指 canonical guidance 的决策

### 5.1 主原则

**project-side runtime pack 只能作为入口层，不能成为第二事实源。**

### 5.2 强制回指机制

建议采用以下四件套：

#### A. 入口身份声明
在 `AGENTS.md` 开头明确声明：

- 本文件是 project-side entrypoint
- 本文件不是 canonical source of truth

#### B. 必读 canonical 清单
在 `AGENTS.md` 中显式列出必须优先读取的 canonical guidance 文件，  
至少应包括：

- workflow bootstrap guidance
- handoff / bounded execution guidance
- project-local canonical skill payload（如存在）

要求：
- 使用**具体文件路径**
- 不接受只写目录名的模糊引用

#### C. 冲突优先级声明
在 `AGENTS.md` 中明确规定：

- 如本文件与 canonical guidance 冲突，以 canonical guidance 为准

#### D. 禁止扩写为第二规则库
在 `AGENTS.md` 中明确规定：

- 不得在此重复复制整套 canonical guidance
- 仅允许保留 dispatch-oriented、reference-first 的最薄说明

---

## 6. 对 `.github/copilot-instructions.md` 的约束

### 6.1 定位

`.github/copilot-instructions.md` 应明确定位为：

**Copilot-specific thin adapter**

### 6.2 内容上限

它只应包含：

1. 最高频规则
2. 最高约束规则
3. 指向 `AGENTS.md` 的回指
4. 指向 canonical skill 的快捷回指

### 6.3 不应承担的角色

它不应承担：

- 全量 workflow 说明
- 全量治理说明
- 全量项目规范说明
- canonical guidance 的复制品

---

## 7. 推荐的 project-side 入口层级

建议 future runtime pack 的最小入口层级如下：

### Level 1：统一主入口
- `AGENTS.md`

### Level 2：Copilot 薄适配
- `.github/copilot-instructions.md`

### Level 3：按主题/路径补充
- `.github/instructions/*.instructions.md`

### Level 4：角色化快捷入口
- `.github/agents/*.agent.md`

### Canonical 本体
- project-local canonical skill payload
- 引用到 hub 中沉淀出的 canonical workflow guidance

---

## 8. Phase 2 的建议落地边界

本决策只收敛“入口选择与回指机制”，  
不自动授权进入完整模板实现。

### Phase 2 合理 in scope
- 明确主入口选择
- 明确回指机制
- 明确最薄文件职责边界
- 如有需要，形成最小 task package 或 decision record

### Phase 2 明确 out of scope
- 不直接创建全量 runtime pack 模板
- 不直接在 hub 中落完整 project-side 文件族
- 不直接升级为 distribution rollout
- 不改 sync/export/import/check 工具逻辑

---

## 9. 对后续 task package 的影响

后续若进入 Phase 2 实施，建议 task package 以以下目标展开：

1. 先定义 `AGENTS.md` 的最薄结构
2. 再定义 `.github/copilot-instructions.md` 的最薄结构
3. 再决定是否需要最小 `.github/instructions/*.instructions.md`
4. 最后再判断 `.github/agents/*.agent.md` 是否需要同时进入模板

推荐顺序应为：

`AGENTS.md`  
→ `.github/copilot-instructions.md`  
→ path-specific instructions  
→ custom agents

而不是反过来。

---

## 10. 当前结论的稳定性判断

本决策适合作为：

- Phase 2 前置边界
- runtime pack 设计的入口级原则
- 后续模板设计的默认基线

但当前还**不是**最终长期治理定稿。

若未来出现以下情况，可重新评估：

- Copilot / Codex 对项目入口文件的支持边界发生明显变化
- 项目侧 runtime pack 的分发机制发生结构性变化
- 多 agent 协作模式从当前主链路发生重大转向

---

## 11. 最小下一步建议

建议下一步不要直接进入完整 runtime pack 模板设计，  
而是先新增一份 **Phase 2 task package**，只做：

- `AGENTS.md` 最薄结构草案
- `.github/copilot-instructions.md` 最薄结构草案
- 强制回指 canonical guidance 的固定文案草案

并继续坚持 bounded execution。

---

## 12. 决策摘要

### 决策一句话版
**project-side runtime pack 的最薄主入口选 `AGENTS.md`；`.github/copilot-instructions.md` 作为 Copilot-specific thin adapter；二者都必须强制回指 canonical guidance，并禁止扩写为第二规则库。**

### 直接影响
- Phase 2 不再纠结主入口选型
- 后续模板设计以 `AGENTS.md` 为中心
- `.github/copilot-instructions.md` 只承担薄适配职责
- canonical guidance 的中心地位被显式保护