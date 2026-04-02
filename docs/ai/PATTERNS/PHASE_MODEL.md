# Phase Model

这个文档定义 skill-hub 中可复用的阶段语义，帮助不同类型的 skill 使用一致的执行语言。

## Project-Type Phases

- `scan` = 获取原始事实，不做推断。
- `understand` = 基于已获取事实形成解释，允许有限推断。
- `structure` = 将事实与解释组织成稳定输出结构。
- `output` = 写入、发布或同步结果。

## Tool-Type Audit Phases

- `audit` = 检查当前对象是否符合规则或约束。
- `report` = 输出结构化结果、问题清单和建议。
- `fix` = 执行修复动作，必须显式触发。

## Usage Notes

- `scan -> understand -> structure -> output` 适合 handoff、takeover、status 等项目过程型 skill。
- `audit -> report -> fix` 适合结构检查、规则校验、治理检查等工具型 skill。
- `fix` 不应默认发生，必须与审计和报告阶段分开表达。

