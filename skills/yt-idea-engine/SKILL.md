---
name: yt-idea-engine
description: >-
  Generate and rank YouTube video ideas using audience pain, proven formats, channel fit, freshness, production cost, and series potential. Use when the user needs what to publish next, a backlog, or ideas better than generic brainstorming.
---

# yt-idea-engine

## Mission
Create a prioritized backlog of video ideas that are specific enough to package and produce.

## Required inputs
- channel position or topic
- target viewer
- desired format (long, short, either)

## Optional inputs
- recent uploads
- competitor examples
- available hours/budget
- seasonal context
- analytics

## Workflow
1. Extract 5-10 recurring audience questions, fears, desires, mistakes, and transformations.
2. Generate ideas across at least 5 mechanisms: search intent, curiosity, comparison, challenge/experiment, story/case study, and timely angle when relevant.
3. Reject duplicates that promise the same payoff.
4. For every idea write a one-line viewer promise and why-now rationale.
5. Score 1-5 for click potential, channel fit, proof available, production cost inverse, and follow-up potential.
6. Return a ranked top 10 and mark top 3 for immediate packaging.

## Output contract
Always return these sections in this order:
- Ranked idea table
- Viewer promise per idea
- Why now
- Evidence needed
- Production difficulty
- Series potential
- Top-3 recommendation

## Quality gates
- Never label an idea viral as a certainty.
- Do not fabricate trends; if trend evidence is unavailable, mark it unverified.
- Avoid near-identical title variations presented as separate ideas.

## Interoperability
Works especially well with: `yt-positioning`, `yt-package`, `yt-script`, `yt-plan`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
