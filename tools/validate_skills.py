#!/usr/bin/env python3
"""Validate YouTube Agent community skills using only Python stdlib."""
from __future__ import annotations
import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

NAME_RE = re.compile(r"^yt-[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_HEADINGS = [
    "Mission",
    "Required inputs",
    "Optional inputs",
    "Workflow",
    "Output contract",
    "Quality gates",
    "Interoperability",
    "Failure handling",
    "Community contribution rule",
]

@dataclass
class SkillResult:
    path: Path
    name: str | None
    score: int
    errors: list[str]
    warnings: list[str]


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing opening YAML frontmatter delimiter"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, ["missing closing YAML frontmatter delimiter"]
    block = text[4:end]
    data: dict[str, str] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value in {">-", ">", "|-", "|"}:
            folded: list[str] = []
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                folded.append(lines[i].strip())
                i += 1
            data[key] = " ".join(x for x in folded if x).strip()
            continue
        data[key] = value.strip('"\'')
        i += 1
    return data, errors


def section_body(text: str, heading: str) -> str:
    pattern = re.compile(rf"^## {re.escape(heading)}\s*$", re.MULTILINE)
    m = pattern.search(text)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^##\s+", text[start:], flags=re.MULTILINE)
    end = start + nxt.start() if nxt else len(text)
    return text[start:end].strip()


def validate_skill(path: Path) -> SkillResult:
    text = path.read_text(encoding="utf-8")
    fm, errors = parse_frontmatter(text)
    warnings: list[str] = []
    score = 100
    name = fm.get("name")
    description = fm.get("description", "").strip()

    if not name:
        errors.append("frontmatter.name is required")
        score -= 20
    elif not NAME_RE.fullmatch(name):
        errors.append("name must match yt-<lowercase-kebab-case>")
        score -= 15

    if name and path.parent.name != name:
        errors.append(f"folder name '{path.parent.name}' must equal frontmatter name '{name}'")
        score -= 10

    if len(description) < 60:
        errors.append("description must be at least 60 characters and state activation intent")
        score -= 10
    if description and not re.search(r"\b(use|when|whenever|for|activate|trigger)\b", description, re.I):
        warnings.append("description may not clearly explain when to activate the skill")
        score -= 3

    h1 = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    if not h1:
        errors.append("missing H1 title")
        score -= 5
    elif name and h1.group(1).strip() != name:
        errors.append("H1 title must exactly match frontmatter.name")
        score -= 5

    for heading in REQUIRED_HEADINGS:
        body = section_body(text, heading)
        if not body:
            errors.append(f"missing or empty section: ## {heading}")
            score -= 5

    workflow = section_body(text, "Workflow")
    if workflow and not re.search(r"(^|\n)\s*\d+[.)]\s+", workflow):
        warnings.append("Workflow should contain numbered deterministic steps")
        score -= 3

    quality = section_body(text, "Quality gates")
    if quality and len(quality.split()) < 18:
        warnings.append("Quality gates are unusually short")
        score -= 2

    failure = section_body(text, "Failure handling")
    if failure and len(failure.split()) < 15:
        warnings.append("Failure handling is unusually short")
        score -= 2

    risky_patterns = [
        (r"(?<!never\s)(?<!do not\s)(?<!don't\s)publish automatically", "publish automatically"),
        (r"(?<!never\s)(?<!do not\s)(?<!don't\s)upload automatically", "upload automatically"),
        (r"guaranteed viral", "guaranteed viral"),
        (r"guarantee virality", "guarantee virality"),
    ]
    lower = text.lower()
    for pattern, label in risky_patterns:
        if re.search(pattern, lower):
            errors.append(f"prohibited unsafe/overclaim phrase: '{label}'")
            score -= 10

    return SkillResult(path, name, max(0, score), errors, warnings)


def validate_repo(root: Path, min_score: int) -> int:
    skills_dir = root / "skills"
    manifest_path = root / "community-skills.json"
    if not skills_dir.exists():
        print("ERROR: skills/ directory not found")
        return 2
    files = sorted(skills_dir.glob("yt-*/SKILL.md"))
    if not files:
        print("ERROR: no skills/yt-*/SKILL.md files found")
        return 2

    results = [validate_skill(p) for p in files]
    names = [r.name for r in results if r.name]
    duplicates = sorted({n for n in names if names.count(n) > 1})
    global_errors: list[str] = []
    if duplicates:
        global_errors.append("duplicate skill names: " + ", ".join(duplicates))

    manifest_names: list[str] = []
    if not manifest_path.exists():
        global_errors.append("community-skills.json is missing")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            entries = manifest.get("skills", [])
            manifest_names = [e.get("name") for e in entries]
            if len(manifest_names) != len(set(manifest_names)):
                global_errors.append("community-skills.json contains duplicate names")
            disk = set(names)
            listed = set(manifest_names)
            missing = sorted(disk - listed)
            stale = sorted(listed - disk)
            if missing:
                global_errors.append("skills missing from manifest: " + ", ".join(missing))
            if stale:
                global_errors.append("manifest entries without skill folders: " + ", ".join(stale))
            for e in entries:
                n, p = e.get("name"), e.get("path")
                expected = f"skills/{n}/SKILL.md" if n else None
                if expected and p != expected:
                    global_errors.append(f"manifest path for {n} must be {expected}")
        except Exception as exc:
            global_errors.append(f"invalid community-skills.json: {exc}")

    failed = False
    print(f"Validating {len(results)} skills (minimum score: {min_score})\n")
    for r in results:
        status = "PASS" if not r.errors and r.score >= min_score else "FAIL"
        print(f"[{status}] {r.name or r.path.parent.name}: {r.score}/100")
        for w in r.warnings:
            print(f"  WARN: {w}")
        for e in r.errors:
            print(f"  ERROR: {e}")
        if status == "FAIL":
            failed = True
    for e in global_errors:
        print(f"GLOBAL ERROR: {e}")
        failed = True
    print("\nRepository validation " + ("FAILED" if failed else "PASSED"))
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--min-score", type=int, default=85)
    args = ap.parse_args()
    return validate_repo(Path(args.root).resolve(), args.min_score)

if __name__ == "__main__":
    sys.exit(main())
