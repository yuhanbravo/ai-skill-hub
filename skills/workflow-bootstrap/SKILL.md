---
name: workflow-bootstrap
description: "Use when defining a tool-agnostic workflow shell, role split, and future runtime-pack mapping for a repository."
metadata:
   triggers:
      - bootstrap a role-based workflow
      - define drafter reviewer implementer reporter final reviewer boundaries
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
- Project-side thin runtime surface guidance: [runtime_pack_minimal_manifest.md](runtime_pack_minimal_manifest.md)
- Role split and protocol integration: [role_split_and_integration.md](role_split_and_integration.md)
- Non-git / low-git runtime profile: [non_git_runtime_profile.md](non_git_runtime_profile.md)
- Review tier guidance: [review_tiers.md](review_tiers.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)

## 4. 核心模式（Pattern）

### Workflow Shell Mapping Pattern（工作流壳层映射模式）

这个 pattern 的核心是先把默认协作链路和角色边界说清，再把后续执行交给更专门的协议或治理 skill。

- 默认链路是工具无关的 `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer`
- Copilot / Codex 等工具名只作为 adapter examples，不是 canonical requirements
- canonical layer 负责定义 workflow 壳层与 guidance
- runtime pack guidance 只描述项目侧 thin runtime surfaces，不在当前 hub 内创建 project-side files

Input:
- 仓库级协作目标
- 当前任务边界
- 本地规则与约束
- 相关 canonical skills

Process:
- 对齐 workflow 壳层
- 收敛最小角色分工
- 把实施协议衔接到 `chatgpt-handoff-pilot`
- 把项目侧 thin runtime surfaces 映射到 runtime pack guidance

Output:
- 默认 workflow 壳层说明
- role-chain 分工
- canonical guidance 与 project-side thin runtime surfaces 的对应关系
- 薄入口回指 canonical guidance 的使用方式

这样组织的原因是，很多多 agent 协作问题并不是缺一个新工具，而是缺一个清晰的默认链路。`workflow-bootstrap` 负责补齐这层壳，但不接管已有协议层、接管层、状态层或治理层的职责。

## 5. 核心原则（Principles）

- `skills/` 始终是唯一 canonical source of truth。  
  Keep `skills/` as the only canonical source.

- 默认使用工具无关的 role chain；具体工具只作为可替换 adapter examples。
  Use the role chain as canonical guidance; treat concrete tools as replaceable adapter examples.

- Drafter、Reviewer、Implementer、Reporter、Final Reviewer 只做职责拆分，不额外发明控制层。
  Keep role split minimal instead of introducing a new control framework.

- handoff 协议继续复用 `chatgpt-handoff-pilot`。  
  Reuse `chatgpt-handoff-pilot` for task packages, bounded execution, and execution reports.

- 在 non-git / low-git 项目侧试跑里，`tasks/` 可作为 task package / execution report 的主证据目录。  
   In non-git / low-git project-side trials, `tasks/` may serve as the primary trace path for task packages and execution reports.

- `docs/HANDOFF.md`、status surface 与 `archive/` 只承接最小闭环或历史参考，不应取代 active workflow line。  
   Keep `docs/HANDOFF.md`, status surfaces, and `archive/` limited to minimal closure or historical reference rather than the active workflow line.

- 薄入口只负责发现与回指，不复制 canonical 细节。  
  Use thin entries for discoverability and redirection, not full duplication.

- runtime pack guidance 只能写成项目侧 thin surface guidance，不能写成当前 hub 已落地事实或第二规则库。
  Describe runtime-pack assets as project-side thin surface guidance only.

## 6. 执行流程（Execution Steps）

1. 判断当前需求是否属于 workflow bootstrap。  
   当目标是定义默认链路、角色分工、runtime-pack 映射，或为后续项目侧入口做 canonical 对齐时，优先使用本 skill；如果目标其实是 handoff、takeover、status update、documentation governance 或 structure audit，则转向对应 skill。

2. 对齐默认链路。  
   明确默认路径为 `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer`。具体工具名只作为 adapter examples；role-based handoff 详见 `role_split_and_integration.md`。

3. 明确最小职责边界。  
   Drafter 负责收敛方案与任务边界；Reviewer 负责 implementation 前的 safety gate；Implementer 负责按任务包做 bounded execution；Reporter 负责 execution report；Final Reviewer 负责边界、验证与闭环检查。不要让本 skill 取代具体实现技能或治理技能。

4. 衔接 handoff 协议。  
   当实施工作需要 task package、bounded execution 和 execution report 时，显式复用 `chatgpt-handoff-pilot`。本 skill 只定义 workflow 壳层，不重新定义 handoff 协议。

5. 对齐 non-git / low-git 证据约定。  
   当项目侧试跑缺少稳定 Git 证据时，可把 `tasks/` 作为 task package / execution report 的主 trace path，并把 execution report 作为每轮实施的主证据。`docs/HANDOFF.md` 与 status surface 只保留最小闭环事实，`archive/` 只作为历史参考，不恢复为 active workflow line。

6. 映射 runtime pack guidance。
   当需要为项目侧协作入口做准备时，只描述 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/copilot-instructions.zh-CN.md`、`tasks/README.md`、task package 和 execution report 等最小候选 surface 与 canonical guidance 的关系，不在 hub 内创建这些项目侧文件。

7. 保持 discoverability 薄层。  
   若新增或维护 adapter 入口，应保持 `.agents/skills/` 与 `.github/skills/` 为薄封装或兼容入口，并回指 canonical `skills/workflow-bootstrap/`，不要复制大段 canonical 内容。

8. 输出简洁实施结果。  
   最终结果应说明：workflow 壳层是否已对齐、与现有相关 skills 的边界是否清楚、discoverability 是否补齐、以及哪些内容被明确保留到 future runtime pack 阶段。

## 7. 约束（Constraints）

- 不替代 `chatgpt-handoff-pilot` 的 task package / bounded execution / execution report 协议
- 不替代 `project-takeover` 的接管与 onboarding 输出
- 不替代 `update-project-status` 的状态刷新职责
- 不替代 `documentation-governance` 的文档治理职责
- 不替代 `file-structure-check` 的结构审计职责
- 不把 `docs/HANDOFF.md`、status surface 或 `archive/` 写成 per-task 主证据线
- 不在 hub 仓库内把 project-side runtime pack 文件族实现成当前正式层
- 不把 `.agents/skills/` 或 `.github/skills/` 升级为第二事实源

## Invocation

### When to use

- 当你需要为仓库补齐 role-based workflow 壳层，并把 Drafter / Reviewer / Implementer / Reporter / Final Reviewer 的最小分工、canonical guidance、future runtime pack 映射说清楚时使用。

### Supporting assets

- Human-oriented context: [README.md](README.md)
- Project-side thin runtime surface guidance: [runtime_pack_minimal_manifest.md](runtime_pack_minimal_manifest.md)
- Role split and protocol integration: [role_split_and_integration.md](role_split_and_integration.md)
- Non-git / low-git runtime profile: [non_git_runtime_profile.md](non_git_runtime_profile.md)
- Review tier guidance: [review_tiers.md](review_tiers.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
