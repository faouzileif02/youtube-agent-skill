---
name: yt-publish-gate
description: >-
  Run a final pre-publish quality-control gate for a YouTube video package and assets. Use before upload or scheduling to catch broken promises, missing assets, metadata gaps, policy-sensitive claims, and operational mistakes.
---

# yt-publish-gate

## Mission
Prevent avoidable publishing errors with a deterministic release checklist.

## Required inputs
- final title
- thumbnail concept/file description
- description
- video/transcript or detailed outline

## Optional inputs
- chapters
- links
- sponsor copy
- captions
- end-screen plan
- playlist destination

## Workflow
1. Verify title/thumbnail/script promise alignment.
2. Check that claims, numbers, links, names, dates, and product references are supported.
3. Check description first lines, links, chapters, CTA, credits, disclosures, and pinned-comment plan when applicable.
4. Check captions/subtitles, end screens/cards plan, playlist assignment, and file naming.
5. Flag policy/copyright areas that need human verification; do not make definitive legal claims.
6. Return PASS, PASS WITH FIXES, or BLOCKED with exact reasons.

## Output contract
Always return these sections in this order:
- Gate status
- Blocking issues
- Non-blocking improvements
- Metadata checklist
- Asset checklist
- Final publish checklist

## Quality gates
- Never claim legal clearance or copyright ownership without evidence.
- Never publish automatically.
- Any unsupported factual claim is a blocker until removed or sourced.

## Interoperability
Works especially well with: `yt-package`, `yt-seo`, `yt-chapters`, `yt-audit`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
