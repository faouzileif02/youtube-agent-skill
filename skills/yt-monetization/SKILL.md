---
name: yt-monetization
description: >-
  Map monetization options for a YouTube channel based on audience intent, trust, content format, expertise, and operational complexity. Use for revenue strategy beyond generic ads.
---

# yt-monetization

## Mission
Build a monetization ladder that matches the audience and channel instead of forcing random products.

## Required inputs
- channel topic
- audience
- current offers/revenue if any
- creator capabilities

## Optional inputs
- traffic scale
- geography
- email list
- products/services
- sponsors

## Workflow
1. Classify audience intent: entertainment, learning, buying, professional, community, or mixed.
2. List monetization mechanisms that fit: ads, affiliate, service, digital product, membership, sponsorship, licensing, lead generation, events, etc.
3. Score each on audience fit, trust requirement, setup effort, margin potential qualitatively, and dependency risk.
4. Create a three-stage ladder: now, next, later.
5. Connect monetization to content without degrading viewer value.
6. Define validation experiments before building expensive offers.

## Output contract
Always return these sections in this order:
- Monetization matrix
- Recommended now/next/later ladder
- Validation experiments
- Content-to-offer mapping
- Risks and dependencies

## Quality gates
- Do not invent CPM/RPM, conversion rates, income forecasts, or sponsor prices.
- Do not recommend deceptive funnels or undisclosed promotion.

## Interoperability
Works especially well with: `yt-positioning`, `yt-plan`, `yt-sponsor-fit`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
