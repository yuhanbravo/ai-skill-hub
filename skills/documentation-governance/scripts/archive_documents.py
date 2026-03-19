from __future__ import annotations

"""Focused wrapper over the central governance engine.

This wrapper exposes archive-oriented fields from the shared engine.
It is not a standalone archive classifier.
"""

import json

from check_documentation_governance import build_governance_report, parse_args, resolve_config


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    config, config_path = resolve_config(root, args.config)
    report = build_governance_report(root, config, config_path, args)
    payload = {
        "archive_candidates": report.archive_candidates,
        "forbidden_documents": report.forbidden_documents,
    }
    print(json.dumps(payload, default=lambda item: item.__dict__, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
