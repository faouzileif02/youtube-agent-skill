---
name: yt-series-builder
description: >-
  Use when the user wants to turn one successful or promising YouTube concept into a repeatable content series with episode logic, escalation, naming, continuity, and stop/continue criteria.
---

# yt-series-builder

## Mission
Convert isolated videos into a repeatable franchise viewers can recognize and return to.

## Required inputs
- seed concept or existing video
- target audience
- channel position

## Optional inputs
- performance data
- production constraints
- desired episode count

## Workflow
1. Extract the repeatable core promise from the seed concept.
2. Define what stays constant and what must change each episode.
3. Design 3 possible series structures: numbered, thematic, progressive/challenge.
4. Create 8 episode concepts with increasing novelty without breaking the core promise.
5. Define visual/naming consistency rules.
6. Define continuation criteria after episode 3 and 5.
7. Identify saturation risks and a clean ending condition.

## Output contract
Always return these sections in this order:
- Series concept
- Series rules
- Naming pattern
- 8-episode map
- Packaging consistency brief
- Continue/kill thresholds
- Spin-off ideas

## Quality gates
- Do not assume one high-view video proves a series.
- Do not create episodes that are title swaps with identical substance.

## Interoperability
Works especially well with: `yt-idea-engine`, `yt-package`, `yt-plan`, `yt-retention`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
