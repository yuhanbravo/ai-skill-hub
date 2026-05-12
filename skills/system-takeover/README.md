# System Takeover

## What is this

`system-takeover` 是一个 system-level takeover skill，用来分析 `skill-hub`、AI capability system、multi-agent system 和 orchestration system 的整体结构、成熟度与演进瓶颈。

## When to use

适合在需要接管一个“能力系统”而不是普通业务仓库时使用，例如分析 skill layer、routing layer、pipeline layer、adapter layer、tooling 和 governance 的协同状态；如果目标只是首次理解普通项目，应优先使用 `project-takeover`。

## Quick Start

```text
Use the `system-takeover` skill on this repository and analyze the capability system.
System root: <project-root>

# optional
# Focus layers: skill / routing / pipeline / adapter / governance
# Dry run: yes/no
```

详细执行方式见 [SKILL.md](SKILL.md)。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

## 1. 背景（Problem Context）

这个 skill 用来解决“如何接管一个能力系统”这一类问题，而不是解决普通业务项目 onboarding 的问题。

当目标对象是 `skill-hub`、AI agent system、orchestration layer 或 capability OS 时，调用方通常面对的不是单一代码库，而是一个由 `skills`、`protocol`、`router`、`pipeline`、`adapter`、`tooling` 和 `governance` 组成的能力系统。仅用普通 `project-takeover` 视角去看，会遗漏 system layer、invocation readiness、discoverability 和 orchestration maturity 这些核心问题。

`system-takeover` 的目标是把这类系统的接管过程稳定组织成“先识别系统结构，再盘点能力与协议，再评估路由、编排、适配和治理成熟度，最后输出瓶颈与演进建议”的系统分析流程。

它在 skill-hub 中属于 `project` 型 system-skill：重点不是单个技能执行，而是对整个 capability system 做分层接管分析。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要分析 `skill-hub` 的能力地图、调用协议和系统边界
- 需要评估一个 AI capability system 的 architecture、layering 和 maturity
- 需要分析 multi-agent system 的 router、pipeline 和 adapter readiness
- 需要接管一个 orchestration system，并判断其 bottlenecks 和 next phase
- 需要从 capability OS 视角，而不是业务项目视角，生成系统级 takeover 结论

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用：

- 当前目标只是首次进入普通业务仓库并生成基础 onboarding 材料，此时更接近 `project-takeover`
- 任务只要求修改单个 skill，此时更接近 `skill-governance`
- 任务只要求更新最近进展或周报，而不是接管系统结构，此时更接近 `update-project-status`
- 当前无法读取 `skills/`、`tools/`、`docs/`、adapter 或测试等系统层材料，导致无法形成分层判断
- 需要直接重构 router、pipeline 或 protocol，而不是先形成 system-level diagnosis

## 5. 分析维度（Analysis Dimensions）

### Capability Map

- 盘点当前 skills 列表与能力域分布
- 判断哪些能力已经有 canonical skill，哪些仍是空洞
- 区分职责重叠、边界相邻和真正冲突的能力单元

### Invocation Readiness

- 检查是否存在统一 invocation protocol
- 检查各 skill 是否包含完整 invocation section 和示例
- 判断 readiness 是文档约定级、测试校验级，还是 enforcement 级

### Routing Layer

- 检查是否存在 router 与 runtime index
- 判断是否支持 `top-k`、confidence、scoring 和多候选输出
- 评估 routing 是否仅为 heuristic，还是已经具备稳定调度基础

### Pipeline Layer

- 检查是否支持 task splitting 与 subtask routing
- 判断是否仅支持 ordered sequence，还是具备 orchestration 能力
- 评估 context passing、dependency handling 和 failure strategy 是否存在

### Adapter Layer

- 检查 `.agents`、`.github` 和其他 adapter entry 是否覆盖 canonical skills
- 判断 discoverability 是单 AI 兼容，还是 multi-AI discoverability
- 检查 canonical 与 adapter 是否存在 drift 风险

### Tooling & Automation

- 盘点 metadata generator、bundle、import/export、sync 和其他自动化脚本
- 判断这些工具是否只支持维护，还是已能支撑 capability system 的分发与同步
- 检查测试、生成器和索引之间是否闭环

### Governance

- 检查 lifecycle、phase model、status management 和 governance skill 是否存在
- 判断治理是否只是文档说明，还是已经进入 CI / enforcement
- 输出治理缺口及下一阶段治理重点

## 8. 输出格式（Output Structure）

输出必须尽量包含以下五部分：

1. `System Structure`
2. `Capability Map`
3. `Maturity Assessment`
4. `Top Bottlenecks`
5. `Evolution Plan`

如果需要更细化，可以在 `Maturity Assessment` 中按以下层输出：

- skill layer
- routing layer
- pipeline layer
- adapter layer
- governance layer

## 10. 风险（Risks）

- 如果把能力系统当作普通项目接管，输出会遗漏真正的系统瓶颈
- 如果只看 README 或单个 skill，而不看 router、pipeline 和 adapter，成熟度判断会偏高
- 如果把 invocation section 的存在误判为 enforcement，可能高估系统 readiness
- 如果忽略 capability overlap 与 capability gaps，演进建议会流于泛泛而谈
- 如果在证据不完整时做强判断，system takeover 结果会误导后续治理优先级

## 11. Prompt 模板（Reusable Prompt）

### 模板 1：标准系统接管模板

```text
请使用 `system-takeover` 处理以下任务。

背景：
- 目标对象是一个 capability system，而不是普通业务项目

目标：
- 分析系统结构、能力地图、调用就绪度、调度层、适配层、工具链和治理成熟度

范围：
- `skills/`
- `tools/`
- `docs/`
- `.agents/`
- `.github/`
- `tests/`

约束：
- 不修改现有 protocol、router、pipeline 或已有 skills
- 只做 system-level takeover analysis

预期输出：
- System Structure
- Capability Map
- Maturity Assessment
- Top Bottlenecks
- Evolution Plan
```

### 模板 2：严格分层分析模板

```text
请按 `system-takeover` 的方法执行本次任务。

要求：
- 先确认该对象是否属于 capability system
- 按 Capability Map、Invocation Readiness、Routing Layer、Pipeline Layer、Adapter Layer、Tooling & Automation、Governance 七个维度推进
- 明确哪些结论是已确认事实，哪些是推断
- 输出系统结构图、按层成熟度、Top 3 瓶颈和下一阶段建议

任务内容：
- System root: <project-root>
- System type: <skill-hub | multi-agent system | orchestration system | capability OS>
- Focus layers: <one-or-more>
- Output mode: <report | summary | takeover packet>
```

## 12. 总结（Summary）

`system-takeover` 最适合解决“如何接管一个能力系统，而不是一个普通项目”这一类问题。它的价值不在于列文件或做一般性审计，而在于把 capability、invocation、routing、pipeline、adapter、tooling 和 governance 组织成一个可判断、可演进的系统视图。

使用时最重要的边界有两条：第一，必须明确对象是 capability system；第二，必须区分“结构存在”“可调用”“可编排”“可治理”这几种不同成熟度，而不能把它们混为一谈。

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)

## 文档语言与 SSOT 说明（2026-05-11）

- 本文档面向开发人员（developer-facing），统一采用**中文为主、英文术语辅助**（例如：`Pattern`、`Invocation`、`Constraints`、`read_only`、`write_files`）。
- 本仓库的 **SSOT（Single Source of Truth）** 仍是当前 skill 目录下的 `SKILL.md`；`README.md` 仅提供可读性说明与快速上手，不得与 `SKILL.md` 发生规则分叉。
- 若 `README.md` 与 `SKILL.md` 出现冲突，必须以 `SKILL.md` 为准，并在后续修订中消除偏差。
- 本节为当前状态声明，更新日期：**2026-05-11**。

