from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    script = repo_root / "skills" / "financial-data-project-migration" / "scripts" / "generate_migration_plan.py"
    project_root = repo_root / ".tmp" / "financial_data_project_migration_self_test"

    if project_root.exists():
        shutil.rmtree(project_root, ignore_errors=True)
    project_root.mkdir(parents=True, exist_ok=True)

    try:
        write_file(project_root / "README.md", "# Sample\n")
        write_file(project_root / "fetch_prices.py", "print('fetch')\n")
        write_file(project_root / "daily_report.py", "print('report')\n")
        write_file(project_root / "requirements.txt", "pandas\n")

        result = subprocess.run(
            [sys.executable, str(script), str(project_root), "--json"],
            capture_output=True,
            text=True,
            check=True,
        )

        payload = json.loads(result.stdout)
        assert payload["project_root"].endswith("financial_data_project_migration_self_test")
        assert "project_type_judgment" in payload
        assert "migration_stage_judgment" in payload
        assert "target_structure_recommendation" in payload
        assert "file_role_classification" in payload
        assert "minimal_migration_todo" in payload
        assert payload["project_type_judgment"]
        assert payload["minimal_migration_todo"]

        print("financial-data-project-migration self-test passed")
    finally:
        shutil.rmtree(project_root, ignore_errors=True)


if __name__ == "__main__":
    main()
