---
name: yt-sponsor-fit
description: >-
  Evaluate sponsor fit and draft an integration brief that protects audience trust. Use when a brand approaches the creator or when the creator is considering outreach.
---

# yt-sponsor-fit

## Mission
Decide whether a sponsor belongs on the channel and, if yes, design a credible integration.

## Required inputs
- brand/product
- channel audience
- video concept or channel topic

## Optional inputs
- offer terms
- required talking points
- usage experience
- exclusivity conditions

## Workflow
1. Map sponsor product to a real audience need.
2. List credibility requirements: personal use, demo, evidence, disclaimers, limitations.
3. Score fit: relevance, trust risk, integration naturalness, repeat potential, conflict with existing positions.
4. Return accept, conditional, or reject with reasons.
5. If accepted, write an integration structure: transition, problem, product role, proof/demo, caveat, CTA.
6. Flag contractual/business terms requiring creator review.

## Output contract
Always return these sections in this order:
- Fit verdict
- Fit scorecard
- Trust risks
- Integration brief
- Questions for sponsor
- Claims that must not be made without evidence

## Quality gates
- Never fabricate personal experience or product results.
- Never hide sponsorship/disclosure requirements.
- Do not provide legal contract approval.

## Interoperability
Works especially well with: `yt-monetization`, `yt-script`, `yt-publish-gate`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
