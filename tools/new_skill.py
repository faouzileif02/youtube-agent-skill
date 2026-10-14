#!/usr/bin/env python3
"""Scaffold a new yt-* community skill."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

NAME_RE = re.compile(r"^yt-[a-z0-9]+(?:-[a-z0-9]+)*$")
TEMPLATE = '''---
name: {name}
description: >-
  Use this skill when the user wants {activation}. Keep the capability narrow,
  deterministic, evidence-aware, and compatible with the YouTube Agent skill pack.
---

# {name}

## Mission
Define the single user problem this skill solves.

## Required inputs
- Input required to execute reliably.

## Optional inputs
- Optional context that improves the result.

## Workflow
1. Validate required inputs.
2. Execute the core analysis or transformation.
3. Check the result against quality gates.
4. Return the fixed output contract.

## Output contract
Return clearly named sections with reusable output.

## Quality gates
- Do not invent metrics, sources, rights, policy certainty, or performance claims.
- Mark assumptions explicitly.
- Keep the output inside this skill's mission.

## Interoperability
State which other `/yt-*` skills should run before or after this one.

## Failure handling
If required evidence is missing, say what is missing and produce only the parts that can be supported.

## Community contribution rule
Changes must preserve the narrow mission, output contract, and validation score.
'''

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    ap.add_argument("--activation", default="perform this YouTube-specific capability")
    args = ap.parse_args()
    if not NAME_RE.fullmatch(args.name):
        raise SystemExit("name must match yt-<lowercase-kebab-case>")
    root = Path(__file__).resolve().parents[1]
    folder = root / "skills" / args.name
    folder.mkdir(parents=True, exist_ok=False)
    (folder / "SKILL.md").write_text(TEMPLATE.format(name=args.name, activation=args.activation), encoding="utf-8")
    print(f"Created {folder / 'SKILL.md'}")
    print("Next: add the skill to community-skills.json and tests/smoke-tests.md")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
