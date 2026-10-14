---
name: yt-music-release
description: >-
  Build a YouTube release package for original music: positioning, title, visual concept, description, credits, lyric/video variants, Shorts teasers, playlist placement, and release sequence. Use for artists, producers, DJ channels, music labels, or AI-assisted original music channels.
---

# yt-music-release

## Mission
Turn one finished track into a coherent YouTube release campaign without inventing artist credentials or music rights.

## Required inputs
- track title or working title
- genre/mood
- artist/channel name
- what assets exist (audio, cover, visualizer, lyrics, video)

## Optional inputs
- lyrics
- release date
- distribution links
- credits
- BPM/key
- story behind track
- target region

## Workflow
1. Define the track promise in one line: mood, moment, or listener use-case.
2. Create title formats for official audio, visualizer, lyric video, and live/remix versions when applicable.
3. Create 3 visual directions aligned with genre without copying identifiable artists.
4. Write description structure: opening mood line, credits, links placeholders, rights/credits placeholders, CTA.
5. Create 3 Shorts teaser concepts from distinct moments (hook, drop, lyric/emotion).
6. Choose playlist placement and internal follow-up content.
7. Run a rights-and-claims checklist: samples, vocals, artwork, distributor metadata, collaborators.

## Output contract
Always return these sections in this order:
- Release title variants
- Thumbnail/visual directions
- Description template
- Credits checklist
- 3 Shorts concepts
- Playlist plan
- Release sequence
- Rights verification checklist

## Quality gates
- Never claim ownership/clearance of samples, vocals, artwork, likeness or compositions without evidence.
- Do not imitate a living artist in a way that implies endorsement or authorship.
- Do not invent streaming links or credits.

## Interoperability
Works especially well with: `yt-thumbnail-director`, `yt-localize`, `yt-playlist-architect`, `yt-publish-gate`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
