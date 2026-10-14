---
name: yt-positioning
description: >-
  Define or repair a YouTube channel position: audience, promise, category, differentiation, content pillars, exclusions, and success metrics. Use when the channel feels vague, inconsistent, hard to describe, or before building a new content strategy.
---

# yt-positioning

## Mission
Turn a vague channel into a precise editorial position that can guide every later YouTube decision.

## Required inputs
- channel topic or current channel description
- target audience or best known viewer
- creator constraints (time, expertise, language, format)

## Optional inputs
- top videos
- competitor channels
- revenue goal
- geography/language
- existing analytics

## Workflow
1. State the current channel in one sentence without marketing language.
2. Identify the primary viewer problem/desire and the moment they would search or click.
3. Produce 3 positioning options: narrow, balanced, broad.
4. Score each option on clarity, repeatability, differentiation, monetization fit, and creator fit (1-5).
5. Choose one recommended position and define 3-5 content pillars.
6. Write explicit exclusions: topics/formats the channel should not chase.
7. Define 3 measurable validation signals for the next 30-90 days.

## Output contract
Always return these sections in this order:
- Recommended positioning statement
- Audience definition
- Channel promise
- 3-5 content pillars
- Do-not-cover list
- Validation metrics
- Next 3 videos that fit the position

## Quality gates
- Do not invent market size, audience numbers, CPM or growth forecasts.
- Do not force a niche narrower than the creator can sustainably produce.
- Distinguish evidence from inference.

## Interoperability
Works especially well with: `yt-plan`, `yt-idea-engine`, `yt-audit`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
