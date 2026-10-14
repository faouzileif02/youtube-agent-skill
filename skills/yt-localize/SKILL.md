---
name: yt-localize
description: >-
  Localize a YouTube video package for another language or region while preserving intent, natural speech, search meaning, cultural fit, and title/thumbnail relationship. Use for translations that must perform as native YouTube content, not literal text.
---

# yt-localize

## Mission
Produce native-feeling localized YouTube copy without changing factual meaning.

## Required inputs
- source title
- source description or script
- target language/region

## Optional inputs
- target audience
- keywords
- brand terms that must stay unchanged
- subtitle file

## Workflow
1. Identify non-translatable brand/product terms.
2. Translate meaning first, then rewrite for native spoken/written rhythm.
3. Create 3 localized title options with the same core promise.
4. Localize thumbnail text separately; do not mechanically mirror the title.
5. Adapt examples, units, idioms and date/number formats only when meaning remains correct.
6. List any phrase requiring creator approval because localization changes nuance.

## Output contract
Always return these sections in this order:
- Localized title options
- Localized thumbnail text options
- Localized description
- Localized CTA
- Glossary/locked terms
- Nuance warnings

## Quality gates
- Never alter factual claims to make them more exciting.
- Flag culturally sensitive or ambiguous phrases instead of guessing.

## Interoperability
Works especially well with: `yt-package`, `yt-seo`, `yt-script`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
