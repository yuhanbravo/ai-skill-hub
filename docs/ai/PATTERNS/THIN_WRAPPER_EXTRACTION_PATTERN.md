# Thin Wrapper Extraction Pattern（薄包装抽取式收敛模式）

这个文档定义一种低风险的局部重复逻辑收敛模式。它面向 AI 施工与人工 review 场景，用来约束“把重复实现抽到共享 helper”这类小步改动，避免被误做成完整架构重构。

## 1. Purpose

Thin Wrapper Extraction Pattern 用于解决多个位置存在重复实现、但当前不适合改变外部接口或调用关系的问题。

它的目标是：

- 保留原有 entry point、函数名、调用链、返回结构和输出口径。
- 将重复实现收敛到一个 shared helper。
- 让原函数退化为薄包装转调层。
- 在最小验证下确认 behavioral equivalence。

## 2. Definition

中文定义：

在不改变原入口、调用链、返回结构和输出口径的前提下，将多个位置的重复实现收敛为共享 helper，并将原函数保留为薄包装转调层。

English definition:

Consolidate duplicated implementation into a shared helper while keeping the original entry points as thin wrappers, without changing call chains, return shapes, output wording, or observable behavior.

## 3. When to Use

适用于：

- 多个函数或方法内部存在明显重复实现。
- 重复逻辑的输入、输出和副作用可以清楚对齐。
- 外部调用方仍依赖原函数名、原模块路径或原命令入口。
- 本轮目标是局部收敛，不是重新设计接口。
- 可以用现有测试、快照、命令输出或手工检查证明行为等价。

## 4. When Not to Use

不适用于：

- 原入口本身已经需要废弃、重命名或迁移。
- 重复逻辑只是表面相似，实际业务语义不同。
- 需要改变返回结构、输出文本、错误处理口径或调用顺序才能抽取。
- 共享 helper 会跨越不应耦合的模块、层级或 ownership boundary。
- 本轮需要的是正式架构重构、公共 API 设计或模块边界重划。

## 5. Core Principles

- Keep entry points unchanged：原函数、原命令、原模块路径和原调用入口继续存在。
- Centralize implementation：真实实现只保留在 shared helper 中，薄包装只负责转调。
- Preserve behavior：返回值、异常、日志、输出口径、排序和副作用保持等价。
- Defer broader refactoring：不顺手重命名、不重排模块、不扩展成架构治理。
- Make boundaries explicit：执行报告中说明哪些改动被允许，哪些改动被明确排除。

## 6. Standard Structure

标准结构是“共享实现 + 原入口薄包装”：

```text
Before:
  entry_a() -> duplicated implementation A
  entry_b() -> duplicated implementation B

After:
  shared_helper() -> single real implementation
  entry_a() -> thin wrapper -> shared_helper()
  entry_b() -> thin wrapper -> shared_helper()
```

薄包装层可以保留原参数名、默认值、docstring、日志上下文或兼容性注释；但它不应继续承载分叉实现。

## 7. Execution Steps

1. 定位重复实现，并确认重复部分具有相同语义。
2. 记录原 entry point、调用链、返回结构、输出口径和现有验证方式。
3. 选择最小 shared helper 位置，优先放在已有模块边界内。
4. 将共同实现移入 shared helper，保持输入输出语义不变。
5. 将原函数改为 thin wrapper，只做参数转发、兼容性处理和返回结果传递。
6. 对比改动前后的可观察行为，包括输出文本、异常、排序和副作用。
7. 在 execution report 中记录已收敛内容、未改内容、验证结果和风险。

## 8. Boundaries

### Allowed Changes

- 新增一个局部 shared helper。
- 将重复实现搬入 shared helper。
- 将原函数改为 thin wrapper。
- 增加少量兼容性注释，说明原入口保留原因。
- 做必要的格式整理，使抽取后的代码可读。

### Forbidden Changes

- 删除或重命名原 entry point。
- 改变调用方需要使用的函数名、命令名、路径或参数形状。
- 改变返回结构、输出文案、错误处理口径、排序或副作用。
- 顺手合并不相关逻辑。
- 将本模式扩展为完整架构重构、模块重分层或治理体系。

### Invariants

- 入口不动。
- 行为不变。
- 输出不变。
- 调用链对外不变。
- 真实实现单点化。
- 原函数只作为 thin wrapper 存在。

### Stop Conditions

遇到以下情况应停手并报告：

- 无法证明多个重复实现具有相同业务语义。
- 抽取需要改变 public behavior 或 output wording。
- helper 的合理位置无法在现有 ownership boundary 内确定。
- 抽取会迫使多个不相关模块产生新耦合。
- 需要修改调用方、测试体系、脚本入口或治理规则才能继续。
- review 发现该改动正在滑向正式重构。

## 9. Validation

最小验证应覆盖 behavioral equivalence，而不是只确认代码能运行。

可采用：

- 运行已有单元测试或文档检查。
- 对比关键命令输出或导出结果。
- 检查返回结构、异常类型、日志和输出文案。
- 对 markdown-only pattern 文档，检查链接、标题层级和目标文件是否存在。

如果本轮只修改 markdown，可不运行代码测试，但 execution report 必须说明原因。

## 10. Review Checklist

Final review 应检查：

- 是否清楚表达 thin wrapper extraction，而不是正式重构。
- 是否保留原 entry point、函数名、调用链和返回结构。
- shared helper 是否成为唯一真实实现。
- 原函数是否只是 thin wrapper。
- observable behavior 是否保持等价。
- 是否禁止顺手重构、重命名或接口迁移。
- 是否包含 stop condition。
- 是否说明最小验证方式。
- 是否存在过度扩大适用范围或引入新治理结构。

## 11. Risks

- shared helper 会成为新的单点依赖；如果 helper 语义过宽，后续调用方可能被错误耦合。
- thin wrapper 阶段可能被误解为完整重构已经完成；实际它只完成重复实现收敛，不代表接口设计完成。
- 表面重复可能掩盖业务差异；若未确认语义，抽取会制造隐性行为回归。
- AI 执行时容易顺手重命名、整理模块或扩大抽象层，应通过 forbidden changes 和 stop conditions 约束。

## 12. Suggested Execution Report Fields

后续复用该 pattern 时，execution report 建议包含：

- Pattern used: `Thin Wrapper Extraction Pattern`
- Files changed
- Original entry points preserved
- Shared helper introduced
- Duplicated implementations removed
- Behavior equivalence evidence
- Allowed changes applied
- Forbidden changes avoided
- Stop conditions checked
- Validation commands and results
- Risks and assumptions
- Suggested follow-up, if any
