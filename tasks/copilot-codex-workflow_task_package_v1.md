# 任务包：Copilot 主控 / Codex 施工工作流（Canonical 最小落地，v1）

## 任务标识

- task id: `WF-CANONICAL-BOOTSTRAP-V1`
- 名称：Copilot 主控 / Codex 施工工作流最小落地（增强版）
- 阶段：Phase 0 + Phase 1（最小实现）
- 提交方：Planner
- 日期：2026-04-21
- 前置输入：`tasks/copilot-codex-workflow_task_package_v0.md`

## 背景

当前仓库 `ai-skill-hub` 已具备 canonical skill 层、adapter 层、桥接文档层、治理文档层与分发工具层。
本任务不是新建平行 workflow 母库，而是在现有母库内补齐一条清晰的“Copilot 主控 / Codex 施工”默认链路，并为未来下发到项目仓库的 runtime pack 预留最小而清晰的结构描述。

本任务必须保留以下既定路线：

1. `ai-skill-hub` 继续作为 canonical workflow / skill 母库。
2. 明确区分：
   - canonical workflow assets（在 hub 内维护）
   - future runtime pack assets（未来下发到项目仓库）
3. 优先复用已有 skills：
   - `chatgpt-handoff-pilot`
   - `project-takeover`
   - `update-project-status`
   - `documentation-governance`
   - `file-structure-check`
4. `chatgpt-handoff-pilot` 继续定位为协议层：task package / bounded execution / execution report。

本次增强版任务包额外吸收三类结构启发，但不改变本仓库现实：

- 借鉴多资源类型分层与“新增资源必须同步更新索引/校验/文档”的治理意识。
- 借鉴 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 的最小文件族分工。
- 借鉴 `copilot-instructions.md` 作为薄入口、保持精简、把详细规则回指到更完整 canonical guidance 的写法。

## 本次目标

在不改动现有 sync/export/import/check 工具逻辑、不做 runtime pack 全量实现的前提下，完成 workflow 的 canonical 最小落地：

1. 新增一个中性 workflow/bootstrap canonical skill。
2. 明确该 skill 与现有五个相关 skills 的职责边界。
3. 在 canonical 资产中写清 future runtime pack 的最小文件族与轻重分层。
4. 保持 adapter / distribution / index / 文档治理的一致性可校验。
5. 让下一轮 Codex 可以在 bounded execution 条件下继续分阶段施工。

## canonical layer 与 future runtime pack 的边界

### A. Canonical layer（当前母库内维护，属于本次优先落点）

- `skills/workflow-bootstrap/`
- 对应 `.agents/skills/` 薄封装入口
- 对应 `.github/skills/` Copilot fallback 入口
- `SKILLS_INDEX.md` 与必要的机器索引更新
- 新 skill 内部的最小模板/说明资产

这些内容属于 source-of-truth 或直接从 source-of-truth 派生的发现入口，应首先落在 `ai-skill-hub` 内。

### B. Future runtime pack（未来项目侧下发资产，本轮只文档化，不实现）

建议作为未来项目仓库最小文件族考虑：

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`
- `.github/agents/*.agent.md`
- project-local canonical skill payload（如项目侧 `.codex/skills/`）
- project-local generated adapters（如项目侧 `.agents/.github`，仅在需要时）

这些内容属于消费侧 runtime 入口、项目级指令分层或项目本地 skill payload；本轮不得在 hub 中把它们误写成“已落地事实”。

### C. 二者关系

- canonical layer 负责定义通用 workflow 方法、边界和模板。
- future runtime pack 负责把这些方法转成项目侧可消费的最小入口与项目级专用约束。
- project-local runtime pack 不得反向成为 hub 的第二事实源。

## 本次范围（In Scope）

- 新增 1 个 canonical skill 目录，用于承载 workflow/bootstrap 最小能力。
- 为该 skill 新增最小 `SKILL.md` 与 `README.md`。
- 在该 skill 内增加少量说明型或模板型资产，用于表达：
  - Copilot 主控 / Codex 施工链路
  - future runtime pack 最小文件族
  - planner / implementer / reviewer 分工
  - 薄入口与详细 guidance 的分层关系
- 新增对应 `.agents` / `.github` adapter 入口。
- 更新索引与必要的生成物，使新 skill 可发现。
- 输出 execution report。

## 明确不做（Out of Scope）

- 不创建完整 `.github/instructions/`、`.github/agents/`、`AGENTS.md` runtime pack 模板集合。
- 不在 hub 仓库中引入 `agents/`、`instructions/`、`hooks/`、`workflows/`、`plugins/` 顶层目录重构。
- 不改动既有 canonical skills 的核心执行契约。
- 不改动 `tools/sync_skills_to_nongit_project.ps1`、`tools/export_bundle.ps1`、`tools/import_bundle.ps1`、`tools/check_adapter_consistency.py` 的逻辑。
- 不做 repo-wide rename、目录迁移、controller 化 orchestration。
- 不把外部公开项目的生态设计、插件机制、教学结构直接移植到本仓库。

## 新增 workflow/bootstrap skill 的职责边界

建议名称：`workflow-bootstrap`

其职责应限定为：

1. 说明默认链路：Copilot 主控，Codex 施工。
2. 定义最小角色分工：planner / implementer / reviewer。
3. 定义 canonical guidance 与 future runtime pack 的映射关系。
4. 定义项目侧最小文件族的推荐清单与轻重分层。
5. 说明何时使用薄入口，何时回到更完整 canonical guidance。

其不应承担的职责：

- 不替代 `chatgpt-handoff-pilot` 的 handoff 协议层能力。
- 不替代 `project-takeover` 的仓库接管与 onboarding 输出。
- 不替代 `update-project-status` 的状态刷新能力。
- 不替代 `documentation-governance` 的文档层级与 SSOT 审计能力。
- 不替代 `file-structure-check` 的结构审计能力。

建议边界表达如下：

- `workflow-bootstrap`：定义 workflow 壳层与 runtime pack 映射。
- `chatgpt-handoff-pilot`：定义任务包、bounded execution、execution report 协议。
- `project-takeover`：负责首次进入仓库时的扫描、理解与接管材料。
- `update-project-status`：负责状态文档与状态信号刷新。
- `documentation-governance`：负责文档角色、事实源与重复风险治理。
- `file-structure-check`：负责目录结构与错位文件审计。

## Future runtime pack 最小文件族（仅作为后续阶段目标）

本轮只要求在 canonical asset 中写清以下建议清单，不要求立即创建：

1. `AGENTS.md`
   - 角色：仓库级工作方式说明、结构边界、资源类型分层、维护约束。
   - 要求：面向仓库级协作，不承载所有细节实现。

2. `.github/copilot-instructions.md`
   - 角色：Copilot 仓库级薄入口。
   - 要求：只保留最高频、最高约束信息；更细规则应回指 `AGENTS.md`、canonical skill、项目本地 instructions 或其他更完整 guidance。

3. `.github/instructions/*.instructions.md`
   - 角色：按主题、路径或文件模式拆分的项目级专用规范。
   - 要求：先从最小公共格式开始，按需细化，不预先铺满。

4. `.github/agents/*.agent.md`
   - 角色：项目内可显式切换的专用 agent 入口。
   - 要求：用于角色专精，不替代 canonical skill。

5. project-local skill payload 与 adapters
   - 角色：承接项目本地 skill 内容与 discoverability。
   - 要求：继续遵守现有 `.codex/skills -> .agents/.github` consumer contract，不得绕回 hub `skills/`。

## 授权文件与目录（Authorized Files / Areas）

- `skills/`（仅新增 `workflow-bootstrap/` 子目录及其最小资产）
- `.agents/skills/`（仅新增 `workflow-bootstrap` 薄封装入口与 flat summary）
- `.github/skills/`（仅新增 `workflow-bootstrap` 兼容入口）
- `SKILLS_INDEX.md`
- `skills_index.json`（如通过既有生成脚本刷新）
- `tasks/`（仅允许新增 execution report，或保留本任务包）

未在以上白名单内的路径，默认无权限修改。

## 期望交付（Expected Deliverables）

1. 新 canonical skill：`workflow-bootstrap`
2. 新 skill 的 `SKILL.md`（执行向）与 `README.md`（说明向）
3. 新 skill 内最小支持资产，建议不超过 2 个 Markdown 文件：
   - runtime pack 文件族说明或 manifest 模板
   - role split / bounded execution integration 说明
4. 对应 adapter 入口：
   - `.agents/skills/workflow-bootstrap/SKILL.md`
   - `.agents/skills/workflow-bootstrap.md`
   - `.github/skills/workflow-bootstrap.md`
5. 索引更新：`SKILLS_INDEX.md`，以及必要时的 `skills_index.json`
6. execution report

## 资源分层与治理要求

本轮虽然不引入新的顶层资源目录，但必须把以下治理意识写进新增资产或相关索引更新中：

1. 新增 canonical skill 后，必须同步更新 discoverability 入口与索引。
2. 若新增模板或说明资产，必须在 canonical skill 内被引用，避免悬空文件。
3. 不得把 future runtime pack 文件族写成当前 hub 已存在的事实目录。
4. 不得让 `.github/copilot-instructions.md` 承担全部详细规范；它应保持薄入口定位。
5. 文档表达必须与当前仓库的 canonical / adapter / governance / bridge 边界一致。

## 执行顺序（Recommended Execution Sequence）

1. 复述边界与本次拟改文件。
2. 创建 `skills/workflow-bootstrap/` 最小骨架。
3. 写入 `SKILL.md` 与 `README.md`，先把职责边界与 runtime pack 分层写清。
4. 只在必要时增加最小支持资产，不超过任务授权范围。
5. 新增 `.agents/.github` 入口。
6. 更新索引与必要生成物。
7. 运行最小验证。
8. 输出 execution report。

## 执行规则（Execution Rules）

必须遵循 `chatgpt-handoff-pilot` 的 bounded execution 风格：

1. 动手前先复述：目标、范围、明确不做、将触及文件。
2. 仅在授权目录内修改。
3. 不顺手修复范围外问题；发现后单列为风险或后续建议。
4. 若遇到命名或边界不确定项，先记录假设并采用最保守实现。
5. 全程保持 canonical source-of-truth 原则：`skills/` 为唯一权威层。
6. 如需提到 future runtime pack，只能作为后续阶段目标表达，不得伪装成当前已实现事实。

## 验证与验收（Validation / Acceptance）

至少完成以下检查并在回执中报告结果：

1. 结构检查：新增 skill 目录满足仓库 skill 结构要求。
2. adapter 合规：
   - `python tools/check_adapter_consistency.py --mode hub`
3. 本地最小验证入口：
   - `powershell.exe -NoProfile -ExecutionPolicy Bypass -File tools\run_local_checks.ps1 -Checks governance`
4. 索引可发现：新 skill 出现在 `SKILLS_INDEX.md`，且 adapter 路径可追溯到 canonical。
5. 文档边界检查：
   - 新增内容未把 future runtime pack 误写成当前仓库已存在的正式层。
   - `.github/copilot-instructions.md` 被表述为未来项目侧薄入口，而不是当前 hub 内已落地的完整规范层。

验收通过标准：

- 新 skill 可被发现（canonical + adapters + index）。
- `workflow-bootstrap` 与现有五个相关 skills 的边界明确且无明显职责重叠。
- 文档明确了 canonical layer 与 future runtime pack 的关系。
- 文档写清 future runtime pack 最小文件族，但未越界实现这些文件。
- 未破坏现有 hub / consumer adapter contract。

## 执行回执要求（Execution Report Requirements）

执行完成后必须输出结构化回执，至少包含：

1. 本次改了什么。
2. 本次没改什么，尤其是明确未实现的 runtime pack 文件族。
3. 实际运行了哪些验证命令及结果摘要。
4. 当前阻塞、假设与风险。
5. 下一步最小建议动作。

## 补充上下文

- 关键本地参考：
  - `tasks/copilot-codex-workflow_task_package_v0.md`
  - `README.md`
  - `SKILLS_INDEX.md`
  - `skills/chatgpt-handoff-pilot/SKILL.md`
  - `docs/ai/DISCOVERY_AND_INVOCATION.md`
  - `docs/governance/adapter_governance.md`
  - `docs/governance/documentation_status_coordination.md`

- 本任务包吸收的外部结构启发仅限于：
  - 多资源类型分层与新增资源同步更新索引/校验/文档的治理意识
  - `AGENTS.md` / `copilot-instructions` / `instructions` / `agents` 的文件族分工
  - `copilot-instructions.md` 作为薄入口的精简写法

- 明确不照搬：
  - marketplace / plugin 生态
  - npm/build 实现细节
  - 教学式组织与示例语气
  - 任何外部仓库的业务领域规则
