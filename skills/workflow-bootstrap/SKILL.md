---
name: workflow-bootstrap
description: "Use when defining the default Copilot-led / Codex-implemented workflow shell, minimal role split, and future runtime-pack mapping for a repository."
metadata:
   triggers:
      - bootstrap a Copilot-led Codex-implemented workflow
      - define planner implementer reviewer boundaries
      - map canonical guidance to a future runtime pack
      - explain thin entry versus full canonical guidance
      - document workflow shell boundaries without replacing handoff protocols
   side_effects:
      - read_only
      - write_files
---
# Workflow Bootstrap

This execution-focused skill definition keeps the workflow-shell behavior, invocation shape, and adapter-facing contract in one canonical location while moving explanation-oriented detail into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Future project-side target mapping: [runtime_pack_minimal_manifest.md](runtime_pack_minimal_manifest.md)
- Role split and protocol integration: [role_split_and_integration.md](role_split_and_integration.md)

## 4. 核心模式（Pattern）

### Workflow Shell Mapping Pattern（工作流壳层映射模式）

这个 pattern 的核心是先把默认协作链路和角色边界说清，再把后续执行交给更专门的协议或治理 skill。

- 默认链路是 `Copilot 主控 / Codex 施工`
- 最小角色分工是 `planner -> implementer -> reviewer`
- canonical layer 负责定义 workflow 壳层与 guidance
- future runtime pack 只作为项目侧目标映射，不在当前 hub 内实现

Input:
- 仓库级协作目标
- 当前任务边界
- 本地规则与约束
- 相关 canonical skills

Process:
- 对齐 workflow 壳层
- 收敛最小角色分工
- 把实施协议衔接到 `chatgpt-handoff-pilot`
- 把项目侧入口映射到 future runtime pack

Output:
- 默认 workflow 壳层说明
- planner / implementer / reviewer 分工
- canonical guidance 与 future runtime pack 的对应关系
- 薄入口回指 canonical guidance 的使用方式

这样组织的原因是，很多多 agent 协作问题并不是缺一个新工具，而是缺一个清晰的默认链路。`workflow-bootstrap` 负责补齐这层壳，但不接管已有协议层、接管层、状态层或治理层的职责。

## 5. 核心原则（Principles）

- `skills/` 始终是唯一 canonical source of truth。  
  Keep `skills/` as the only canonical source.

- 默认由 Copilot 收敛方案，由 Codex 执行受边界约束的施工。  
  Let Copilot drive planning and Codex perform bounded implementation by default.

- planner、implementer、reviewer 只做最小职责拆分，不额外发明控制层。  
  Keep role split minimal instead of introducing a new control framework.

- handoff 协议继续复用 `chatgpt-handoff-pilot`。  
  Reuse `chatgpt-handoff-pilot` for task packages, bounded execution, and execution reports.

- 薄入口只负责发现与回指，不复制 canonical 细节。  
  Use thin entries for discoverability and redirection, not full duplication.

- future runtime pack 只能写成项目侧目标，不能写成当前 hub 已落地事实。  
  Describe future runtime-pack assets as project-side targets only.

## 6. 执行流程（Execution Steps）

1. 判断当前需求是否属于 workflow bootstrap。  
   当目标是定义默认链路、角色分工、runtime-pack 映射，或为后续项目侧入口做 canonical 对齐时，优先使用本 skill；如果目标其实是 handoff、takeover、status update、documentation governance 或 structure audit，则转向对应 skill。

2. 对齐默认链路。  
   明确默认路径为 `planner -> implementer -> reviewer`，并把 `Copilot 主控 / Codex 施工` 作为首选协作形态；只有项目本地规则明确要求其他主控关系时，才偏离这个默认值。

3. 明确最小职责边界。  
   `planner` 负责收敛方案与任务边界；`implementer` 负责按任务包做 bounded execution；`reviewer` 负责检查边界、文档、索引与验证是否闭环。不要让本 skill 取代具体实现技能或治理技能。

4. 衔接 handoff 协议。  
   当实施工作需要 task package、bounded execution 和 execution report 时，显式复用 `chatgpt-handoff-pilot`。本 skill 只定义 workflow 壳层，不重新定义 handoff 协议。

5. 映射 future runtime pack。  
   当需要为项目侧协作入口做准备时，只描述 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 等候选文件族与 canonical guidance 的关系，不在 hub 内创建这些项目侧文件。

6. 保持 discoverability 薄层。  
   若新增或维护 adapter 入口，应保持 `.agents/skills/` 与 `.github/skills/` 为薄封装或兼容入口，并回指 canonical `skills/workflow-bootstrap/`，不要复制大段 canonical 内容。

7. 输出简洁实施结果。  
   最终结果应说明：workflow 壳层是否已对齐、与现有相关 skills 的边界是否清楚、discoverability 是否补齐、以及哪些内容被明确保留到 future runtime pack 阶段。

## 7. 约束（Constraints）

- 不替代 `chatgpt-handoff-pilot` 的 task package / bounded execution / execution report 协议
- 不替代 `project-takeover` 的接管与 onboarding 输出
- 不替代 `update-project-status` 的状态刷新职责
- 不替代 `documentation-governance` 的文档治理职责
- 不替代 `file-structure-check` 的结构审计职责
- 不在 hub 仓库内把 future runtime pack 文件族实现成当前正式层
- 不把 `.agents/skills/` 或 `.github/skills/` 升级为第二事实源

## Invocation

### When to use

- 当你需要为仓库补齐默认的 `Copilot 主控 / Codex 施工` workflow 壳层，并把 planner / implementer / reviewer 的最小分工、canonical guidance、future runtime pack 映射说清楚时使用。

### Supporting assets

- Human-oriented context: [README.md](README.md)
- Future project-side target mapping: [runtime_pack_minimal_manifest.md](runtime_pack_minimal_manifest.md)
- Role split and protocol integration: [role_split_and_integration.md](role_split_and_integration.md)
