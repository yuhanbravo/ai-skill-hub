# Future Runtime Pack Minimal Manifest

Status: this document describes a future project-side target, not a currently implemented hub layer.

`workflow-bootstrap` 在 hub 内只维护 canonical guidance。下面这些文件或文件族属于未来项目仓库可下发的最小 runtime pack 候选，不应被写成当前 `ai-skill-hub` 已经实现的事实。

## `AGENTS.md`

- Role: 仓库级协作规则入口，说明工作方式、结构边界、维护约束和默认协作链路。
- Why it exists: 给项目内的 AI 和维护者一个薄而稳定的仓库级工作约束入口。
- Relation to canonical guidance: 应引用或概括 `workflow-bootstrap` 与相关 canonical skills 的关键边界，而不是成为新的事实源。
- Why not implemented in the hub now: 它属于项目侧 runtime 入口，内容会依赖具体项目结构和本地约束，当前 hub 只负责 canonical 壳层说明。

## `.github/copilot-instructions.md`

- Role: Copilot 的仓库级薄入口，承接最高频、最高约束的协作规则。
- Why it exists: 让 Copilot 在项目内有一个轻量入口，而不必把完整 canonical guidance 全量复制进 compatibility 文件。
- Relation to canonical guidance: 应保持精简，并回指 `AGENTS.md`、canonical skills 或项目本地更细的 instructions。
- Why not implemented in the hub now: 这是 future project-side target；当前阶段只需要在 canonical 中说明“薄入口 -> 指向更完整 guidance”的思路。

## `.github/instructions/*.instructions.md`

- Role: 按主题、路径或文件模式拆分的项目级专用规范。
- Why it exists: 当仓库需要按代码区域、工作流主题或文件类型细化规则时，避免把所有细节堆进单一入口。
- Relation to canonical guidance: 应从 canonical workflow guidance 和项目本地事实中派生，不应反向覆盖 `skills/` 中的 canonical 定义。
- Why not implemented in the hub now: 这些文件高度依赖项目上下文，本轮只需保留最小文件族设计，不在 hub 内预创建模板集合。

## `.github/agents/*.agent.md`

- Role: 项目内可显式切换的专用 agent 入口，用于 planner、implementer、reviewer 或其他角色专精。
- Why it exists: 在项目侧把角色入口做成可发现的显式切换点，但不把角色系统硬编码进 canonical hub。
- Relation to canonical guidance: 应遵守 `workflow-bootstrap` 定义的最小角色分工，并在需要 handoff 时回接 `chatgpt-handoff-pilot`。
- Why not implemented in the hub now: 这些 agent files 属于项目侧 runtime surface；当前 hub 只负责说明推荐分工，不负责为所有项目预置 agent 模板。

## Optional Project-Local Skill Payload And Adapters

- Role: 在项目仓库承接项目本地 skill payload，以及面向不同消费者的 discoverability 入口。
- Why it exists: 让项目在不修改 hub canonical 的前提下，承接项目专用约束和分发入口。
- Relation to canonical guidance: 应继续遵守 `skills/` canonical source、`.agents/.github` discoverability、以及现有 consumer adapter contract。
- Why not implemented in the hub now: 本轮目标是 canonical documentation / mapping，不是 project-local runtime-pack 下发或 consumer-side 全量实现。
