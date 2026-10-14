---
name: yt-community
description: >-
  Create a YouTube Community strategy and post set from current videos, audience questions, polls, teasers, follow-ups, and reactivation prompts. Use to keep the audience engaged between uploads.
---

# yt-community

## Mission
Turn the Community tab into a feedback and retention loop instead of random posts.

## Required inputs
- channel topic
- recent or upcoming video(s)
- audience tone

## Optional inputs
- poll results
- comments
- upload calendar
- brand voice

## Workflow
1. Select the post objective: teaser, feedback, proof, poll, discussion, reactivation, or follow-up.
2. Write 5 posts with different objectives, not paraphrases.
3. For polls, provide 3-4 mutually understandable options.
4. Connect each post to a future content decision or existing video when useful.
5. Define recommended timing relative to uploads without pretending a universal best hour exists.
6. Add what signal to observe (comments, votes, click-through proxy, idea demand).

## Output contract
Always return these sections in this order:
- 5 ready-to-post community posts
- Objective per post
- Suggested relative timing
- Signal to watch
- How to use responses in future videos

## Quality gates
- Do not fake audience quotes, poll results, scarcity, or social proof.
- Do not over-post the same call to action.

## Interoperability
Works especially well with: `yt-comment`, `yt-plan`, `yt-idea-engine`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
