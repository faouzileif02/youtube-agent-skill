---
name: youtube-agent
description: >-
  All-in-one YouTube strategy and creator operations skill. Automatically route requests to the right internal module for channel positioning, ideas, series, thumbnails, publish QA, Community posts, localization, playlists, monetization, sponsor fit, experiments, or music releases. Use whenever the user asks for YouTube strategy, planning, packaging, growth operations, audience engagement, monetization, or release support.
---

# youtube-agent

One entry point for the full YouTube Agent Community skill pack.

## Core behavior

1. Infer the user's primary intent.
2. Select the smallest internal module that fully covers the task.
3. Read the matching file in `modules/` before answering.
4. If two modules are genuinely required, use at most two and follow the natural execution order.
5. Preserve every module's required inputs, output contract, quality gates, and failure handling.
6. Never invent analytics, performance numbers, claims, sources, rights, sponsorship results, or revenue forecasts.
7. Never publish, upload, schedule, or modify a YouTube channel automatically unless the user explicitly asks and the environment actually provides an authorized action tool.

## Router

| User intent | Module |
| --- | --- |
| define niche, audience, promise, pillars | `modules/yt-positioning.md` |
| generate or rank video ideas | `modules/yt-idea-engine.md` |
| turn a concept into a repeatable series | `modules/yt-series-builder.md` |
| create thumbnail direction or image brief | `modules/yt-thumbnail-director.md` |
| final QA before upload/publish | `modules/yt-publish-gate.md` |
| Community posts, polls, engagement | `modules/yt-community.md` |
| translate/localize YouTube copy | `modules/yt-localize.md` |
| playlists, binge paths, homepage sections | `modules/yt-playlist-architect.md` |
| monetization strategy | `modules/yt-monetization.md` |
| sponsor evaluation/integration | `modules/yt-sponsor-fit.md` |
| controlled YouTube experiment | `modules/yt-experiment.md` |
| package/release original music | `modules/yt-music-release.md` |

## Explicit commands

Route these directly to the matching module:
`/yt-positioning`, `/yt-idea-engine`, `/yt-series-builder`, `/yt-thumbnail-director`, `/yt-publish-gate`, `/yt-community`, `/yt-localize`, `/yt-playlist-architect`, `/yt-monetization`, `/yt-sponsor-fit`, `/yt-experiment`, `/yt-music-release`.

The user may also say `/youtube-agent` followed by a normal request; infer the module automatically.

## Multi-module routing

Use two modules only when outputs are naturally sequential. Typical chains:
- `yt-positioning` -> `yt-idea-engine`
- `yt-idea-engine` -> `yt-series-builder`
- `yt-thumbnail-director` -> `yt-experiment`
- `yt-monetization` -> `yt-sponsor-fit`
- `yt-music-release` -> `yt-publish-gate`
- `yt-localize` -> `yt-publish-gate`

## Missing information

- If missing data does not materially affect the result, make a clearly labeled provisional assumption and continue.
- If it would materially change the recommendation, request only that information.
- Separate user-provided facts, known facts, and inference when the distinction matters.

## Final answer discipline

Follow the selected module's output contract. Prefer ranked recommendations, one strong default plus alternatives, clearly labeled uncertainty, and explicit rights/copyright uncertainty when relevant.
