# DEV NOTES

## 2026-03-20 Real Dry Run Feedback: AMS_Report

### Why this note exists

The first real dry run showed that v1 was too optimistic for a class of financial-data repositories that are not merely "script-heavy Python projects", but operational desktop systems coupled to Excel, Wind, templates, and network shares.

### Observed repository shape

Target project: `D:\BaiduSyncdisk\Python_Lib\AMS_Report`

Observed signals:
- Dozens of root-level Python scripts.
- Hundreds of Excel assets mixed with code, outputs, archives, and reference files.
- `WindPy` dependency in core scripts.
- `xlwings` and `openpyxl` used for Excel automation and workbook writes.
- Script-style orchestration entrypoints such as `Task_Monthly_Report.py`.
- Fixed network-share paths in orchestration logic.
- Current-working-directory assumptions in some scripts.
- Single scripts combining fetch + compute + Excel write responsibilities.

### Main failure in old v1 behavior

Old v1 tended to classify this kind of repo as:
- `analysis-reporting`
- `batch-pipeline`
- stage: `script-sprawl`

That output was not fully wrong, but it was not conservative enough. It missed the stronger reality that this project is a desktop Excel + Wind + network-share coupled script system and therefore should not receive package-first migration guidance as the next action.

### Minimal enhancements added

1. Added project type label:
- `desktop_excel_wind_script_project`

2. Added stage downgrade rule:
- If the project shows Excel-heavy assets or desktop/runtime coupling signals, prefer:
  `冻结现状 / 建立清单 / 边界识别`

3. Added fixed risk output:
- 外部桌面环境依赖
- 网络盘依赖
- 当前工作目录依赖
- Excel 资产角色不清

4. Added concrete target-structure examples:
- `example_mapping_candidates`
- Purpose: make structure advice more actionable on real repos without triggering auto-migration behavior.

### Guardrail reminder

Do not let this skill jump from "script-heavy" directly to "create src and move logic" when the runtime contract is still dominated by:
- Excel desktop state
- Wind availability
- network shares
- opaque template assets
- root-relative execution assumptions

### What to watch in the next dry run

- Whether the new label triggers only on the intended combined signal set, rather than any repo that merely has many Excel files.
- Whether the stage downgrade fires on truly risky script systems but stays out of the way for cleaner hybrid repos.
- Whether `example_mapping_candidates` remains concrete and useful instead of just echoing noisy top-level files.
