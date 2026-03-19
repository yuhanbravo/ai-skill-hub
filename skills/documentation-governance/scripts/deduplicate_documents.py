from __future__ import annotations

"""Focused wrapper over the central governance engine.

This wrapper exposes duplicate and engineering-layer source-of-truth findings
computed by the shared engine.
"""

import json

from check_documentation_governance import build_governance_report, parse_args, resolve_config


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    config, config_path = resolve_config(root, args.config)
    report = build_governance_report(root, config, config_path, args)
    payload = {
        "duplicate_candidates": report.duplicate_candidates,
        "ssot_conflicts": report.ssot_conflicts,
        "layer_placement_conflicts": report.layer_placement_conflicts,
        "readable_second_truth_conflicts": report.readable_second_truth_conflicts,
    }
    print(json.dumps(payload, default=lambda item: item.__dict__, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
