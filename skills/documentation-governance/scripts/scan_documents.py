from __future__ import annotations

"""Focused wrapper over the central governance engine.

This wrapper does not implement a separate scan engine. It reuses
`build_governance_report(...)` and returns only scan-oriented fields.
"""

import json

from check_documentation_governance import build_governance_report, parse_args, resolve_config


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    config, config_path = resolve_config(root, args.config)
    report = build_governance_report(root, config, config_path, args)
    payload = {
        "engineering_docs": report.engineering_docs,
        "readable_docs": report.readable_docs,
        "scanned_files": report.scanned_files,
        "forbidden_documents": report.forbidden_documents,
    }
    print(json.dumps(payload, default=lambda item: item.__dict__, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
