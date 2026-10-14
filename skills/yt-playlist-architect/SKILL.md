---
name: yt-playlist-architect
description: >-
  Use when the user wants to design or repair YouTube playlists around viewer journeys, binge paths, search themes, series continuity, and channel homepage structure.
---

# yt-playlist-architect

## Mission
Organize videos so the next logical watch is obvious and channel navigation reflects viewer intent.

## Required inputs
- video inventory or representative titles
- channel position

## Optional inputs
- analytics
- existing playlists
- series map
- homepage sections

## Workflow
1. Cluster videos by viewer intent, not internal creator categories.
2. Separate true series from topical collections.
3. Create playlist names that communicate a viewer outcome.
4. Order videos by best starting point and progression, not necessarily chronology.
5. Identify orphan videos and duplicate playlists.
6. Propose homepage sections and which playlist should lead each section.

## Output contract
Always return these sections in this order:
- Playlist map
- Video-to-playlist assignments
- Recommended order
- Playlist titles/descriptions
- Homepage section order
- Orphan/duplicate cleanup list

## Quality gates
- Do not invent unavailable video performance data or pretend an ordering decision is data-backed when it is heuristic.
- Avoid playlists with no coherent viewer journey.
- Every proposed playlist must have a clear entry promise, sequence logic, and reason for the next click.

## Interoperability
Works especially well with: `yt-series-builder`, `yt-audit`, `yt-plan`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
