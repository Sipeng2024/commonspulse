from __future__ import annotations

import argparse
import json
from pathlib import Path

from .watcher import build_snapshot, render_markdown


def main() -> None:
    parser = argparse.ArgumentParser(description="Evidence-based grant portfolio watcher")
    parser.add_argument("config", help="Path to YAML config file")
    parser.add_argument("--out", default="output/report.md", help="Output markdown path")
    parser.add_argument("--json", dest="json_out", default="output/report.json", help="Output JSON path")
    args = parser.parse_args()

    snapshot = build_snapshot(Path(args.config))
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render_markdown(snapshot), encoding="utf-8")

    json_path = Path(args.json_out)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Wrote markdown report to {out_path}")
    print(f"Wrote JSON snapshot to {json_path}")
