# Contributing to YouTube Agent Community Skills

Thank you for improving the pack. The goal is a small set of precise capabilities, not a collection of giant prompts.

## Before proposing a skill

A new command must solve one distinct YouTube problem that cannot be cleanly handled by an existing skill. Search `CATALOG.md` first. Prefer improving an existing skill when the mission substantially overlaps.

## Required structure

Every `skills/yt-*/SKILL.md` must contain:

- YAML frontmatter with `name` and activation-oriented `description`
- `## Mission`
- `## Required inputs`
- `## Optional inputs`
- `## Workflow`
- `## Output contract`
- `## Quality gates`
- `## Interoperability`
- `## Failure handling`
- `## Community contribution rule`

The folder name, H1 and frontmatter `name` must match exactly and use `yt-<lowercase-kebab-case>`.

## Quality score

Run:

```bash
python tools/validate_skills.py
```

A skill must score **85/100 or higher** and have no hard errors. The score is a deterministic repository hygiene check, not a prediction of whether a skill is useful.

## New-skill workflow

```bash
python tools/new_skill.py yt-your-capability --activation "..."
```

Then:

1. Fully implement `SKILL.md`.
2. Add it to `community-skills.json` with `category` and `summary`.
3. Add at least one realistic prompt to `tests/smoke-tests.md`.
4. Run `python tools/build_catalog.py`.
5. Run unit tests and validator.
6. Open a PR using the repository template.

## Safety and evidence

Do not fabricate analytics, audience research, market data, sponsorship results, music rights, legal clearance, platform-policy certainty or performance guarantees. When evidence is missing, mark the assumption or stop the unsupported part of the workflow.

Never hide publishing, uploads, deletions, account changes or other consequential actions inside an analysis/drafting skill.

## Pull requests

Explain the user problem, overlap boundary, required inputs, fixed output contract, and at least one example. Keep unrelated changes out of the same PR.
