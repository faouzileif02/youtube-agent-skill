#!/usr/bin/env python3
"""Build or verify CATALOG.md from community-skills.json."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

HEADER = """# Skill Catalog\n\nThis file is generated from `community-skills.json`. Do not edit it manually.\n\n| Command | Category | Purpose |\n|---|---|---|\n"""

def render(root: Path) -> str:
    data = json.loads((root / "community-skills.json").read_text(encoding="utf-8"))
    rows = []
    for s in sorted(data["skills"], key=lambda x: x["name"]):
        rows.append(f"| `/{s['name']}` | {s.get('category','other')} | {s.get('summary','')} |")
    return HEADER + "\n".join(rows) + "\n"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    target = root / "CATALOG.md"
    expected = render(root)
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != expected:
            print("CATALOG.md is out of date. Run: python tools/build_catalog.py")
            return 1
        print("CATALOG.md is up to date")
        return 0
    target.write_text(expected, encoding="utf-8")
    print(f"Wrote {target}")
    return 0
if __name__ == "__main__":
    sys.exit(main())
