# Governance Rules

## Rewrite Budget

- `20%`: 只允许轻量结构修整、措辞收敛、README 或 prompt 对齐
- `50%`: 允许中等规模重组，修复结构缺口、原则不清、类型错位
- `full`: 允许完整重写当前 skill 文档包，但仍只限单个目标 skill

## Pattern Alignment Rules

- `pattern`：重点检查 Pattern、Principles、Reusable Prompt 的抽象稳定性
- `project`：重点检查 Problem Context、Execution Steps、阶段推进是否清晰
- `tool`：重点检查输入、处理、输出链路，以及 Constraints 和 Risks 是否明确
- `governance`：重点检查控制边界、评估优先级、重写授权和 Non-intrusive 原则

## Skill Type Definitions

- `pattern`: 面向协作方法、抽象工作流和可复用执行模式的 skill
- `project`: 面向阶段化项目任务、交接流程和仓库级输出的 skill
- `tool`: 面向单个工具、脚本或审计链路的 skill
- `governance`: 面向其他 skill 的评估、约束、决策与受控重写的 meta-skill

## Governance Baselines

- 默认只评估，不修改
- rewrite 必须显式触发
- 一次只处理一个 skill
- 默认不改变项目
- 禁止跨 skill 批量操作

## Repository Commit Governance

- `commit-convention-check` 负责校验仓库级 commit message
- 提交主题只接受 `docs / feat / fix / refactor / test / chore` 六类 type
- 支持 `<type>: <action>`、`<type>(<scope>): <action>`、`<type>: Phase <n>[.<m>] - <scope> - <action>`
- 若存在 body，必须使用 subject 后空一行的标准多行格式
