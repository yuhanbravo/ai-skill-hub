# Standard Execution Shapes

This document makes the recurring skill execution shapes explicit for the AI layer.

## Pattern Skill

- `Input -> Process -> Output`

## Project Skill

- `scan -> understand -> structure -> output`

## Tool Skill

- `audit -> report -> fix(optional)`

## Governance Skill

- `evaluate -> diagnose -> decide -> refactor(optional)`

## System Wrapper Skill

- Reuse the canonical skill first
- Narrow the target to a system-scoped artifact
- Add output or section constraints without forking canonical logic
