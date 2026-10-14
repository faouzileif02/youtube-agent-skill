---
name: yt-thumbnail-director
description: >-
  Create a production-ready YouTube thumbnail art direction brief: focal subject, composition, visual contrast, text policy, emotion, mobile legibility, variants, and handoff notes. Use when a designer or image model needs an exact thumbnail brief.
---

# yt-thumbnail-director

## Mission
Translate the video promise into a thumbnail concept a human designer or image generator can execute.

## Required inputs
- video idea or script
- working title
- target viewer

## Optional inputs
- brand colors
- reference thumbnails
- available photos/assets
- face/no-face preference

## Workflow
1. Reduce the video promise to one visual question or tension.
2. Choose one focal subject and one secondary supporting element maximum.
3. Write 3 distinct thumbnail concepts, not cosmetic variants.
4. For each, specify composition, crop, emotion/action, background, text (0-4 words max if needed), and mobile readability.
5. Check duplication against the title: thumbnail should add information, not repeat it.
6. Choose the recommended concept and define A/B alternatives with one variable changed at a time.

## Output contract
Always return these sections in this order:
- 3 concept briefs
- Recommended concept
- Exact asset list
- Text/no-text decision
- Mobile legibility checklist
- A/B variant plan
- Designer/image-model prompt notes

## Quality gates
- Do not use misleading imagery that the video cannot substantiate.
- Avoid tiny UI screenshots unless they remain legible on mobile.
- Do not require clickbait facial expressions by default.

## Interoperability
Works especially well with: `yt-package`, `yt-experiment`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
