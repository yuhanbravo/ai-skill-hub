from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_migration_plan.py"
TMP_ROOT = Path(__file__).resolve().parents[1] / ".tmp"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_plan(project_root: Path) -> dict:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(project_root), "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def prepare_project(name: str) -> Path:
    project_root = TMP_ROOT / name
    if project_root.exists():
        shutil.rmtree(project_root, ignore_errors=True)
    project_root.mkdir(parents=True, exist_ok=True)
    return project_root


def main() -> None:
    TMP_ROOT.mkdir(parents=True, exist_ok=True)

    project_root = prepare_project("sample_project")
    try:
        write_file(project_root / "README.md", "# Sample\n")
        write_file(project_root / "fetch_prices.py", "print('fetch')\n")
        write_file(project_root / "daily_report.py", "print('report')\n")
        write_file(project_root / "requirements.txt", "pandas\n")

        payload = run_plan(project_root)
        assert payload["project_root"].endswith("sample_project")
        assert payload["project_type_judgment"]
        assert payload["migration_stage_judgment"]
        assert payload["target_structure_recommendation"]
        assert payload["file_role_classification"]
        assert payload["minimal_migration_todo"]
    finally:
        shutil.rmtree(project_root, ignore_errors=True)

    project_root = prepare_project("desktop_project")
    try:
        write_file(
            project_root / "Task_Monthly_Report.py",
            "import subprocess\nfrom pathlib import Path\nDATA_ROOT=r'\\\\server\\share\\data'\nprint(Path.cwd())\nsubprocess.run(['python','Monthly_AMS_Portfolio.py'])\n",
        )
        write_file(
            project_root / "Monthly_AMS_Portfolio.py",
            "from WindPy import w\nimport xlwings as xw\nimport pandas as pd\nfrom pathlib import Path\nPath.cwd()\nres = w.wpf('demo','fields','options')\ndf = pd.DataFrame({'a':[1]})\ndf.groupby('a').sum()\ndf.to_excel('out.xlsx')\n",
        )
        write_file(project_root / "verify_data.py", "print('verify')\n")
        write_file(project_root / "docs" / "HANDOFF.md", "# Handoff\n")
        for idx in range(12):
            write_file(project_root / f"asset_{idx:02d}.xlsx", "")

        payload = run_plan(project_root)
        assert "desktop_excel_wind_script_project" in payload["project_type_judgment"]
        assert payload["migration_stage_judgment"] == "冻结现状 / 建立清单 / 边界识别"
        assert payload["risk_assessment"]
        assert "example_mapping_candidates" in payload["target_structure_recommendation"]
        assert any(item["name"] == "外部桌面环境依赖" for item in payload["risk_assessment"])
    finally:
        shutil.rmtree(project_root, ignore_errors=True)

    print("financial-data-project-migration self-test passed")


if __name__ == "__main__":
    main()
