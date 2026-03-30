# Documentation Governance OS

## What is this

`documentation-governance` 是一个文档治理审计型 skill，用来基于双层文档模型、单一事实源和命名规则检查仓库 markdown 结构，并输出治理报告。

## When to use

适合在需要检查 `docs/` 与 `docs_readable/` 的关系、识别重复主题、命名违规、归档候选或 README 治理缺口时使用；如果目标是直接批量改写文档，这个 skill 不应作为第一步。

## Quick Start

```text
Use the `documentation-governance` skill on this repository and audit the documentation structure.
Project root: <project-root>

# optional
# Config path: <path-or-none>
# Dry run: yes/no
```

详细治理模式见 [SKILL.md](SKILL.md)。
