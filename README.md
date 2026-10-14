# YouTube Agent Skill — Community V1.1

A community-driven collection of modular AI skills for YouTube creators, channel operators, strategists, artists, and autonomous content agents.

## V1.1 goals

This repository extends the classic YouTube-agent pattern with narrowly scoped, composable skills that each define:

- a precise mission
- required and optional inputs
- a deterministic workflow
- a strict output contract
- quality gates and anti-hallucination rules
- interoperability with other skills
- explicit failure handling
- a contribution contract

## Included community skills

| Skill | Purpose |
| --- | --- |
| `/yt-positioning` | Define channel positioning, audience, promise and content pillars. |
| `/yt-idea-engine` | Generate, filter and rank video ideas with clear selection logic. |
| `/yt-series-builder` | Turn a promising topic or video into a repeatable content series. |
| `/yt-thumbnail-director` | Produce a precise visual brief for a thumbnail designer or image model. |
| `/yt-publish-gate` | Run a final pre-publish QA gate across packaging, metadata and claims. |
| `/yt-community` | Build Community posts, polls and engagement loops. |
| `/yt-localize` | Adapt YouTube content across languages and markets without literal translation. |
| `/yt-playlist-architect` | Design playlists, viewing paths and channel-home structure. |
| `/yt-monetization` | Build revenue options matched to audience fit and channel maturity. |
| `/yt-sponsor-fit` | Evaluate sponsor fit and prepare a safe, relevant integration. |
| `/yt-experiment` | Design controlled YouTube experiments and define success criteria. |
| `/yt-music-release` | Plan a YouTube music release, supporting assets and distribution flow. |

See [CATALOG.md](CATALOG.md) for the generated catalog.

## Install

Copy any skill directory into your agent or Claude-style skills directory, or install the complete repository in a project-local skills folder.

Each skill is self-contained in:

```text
skills/<skill-name>/SKILL.md
```

A shared channel profile template is available at:

```text
templates/channel-profile.md
```

## Quality system

V1.1 includes an executable validation layer:

```bash
python tools/validate_skills.py --min-score 85
python -m unittest discover -s tests -p "test_*.py" -v
python tools/build_catalog.py --check
```

GitHub Actions runs the same checks automatically on relevant pushes and pull requests.

## Create a new skill

```bash
python tools/new_skill.py yt-my-skill
```

Then complete the generated `SKILL.md`, validate it, and update the manifest/catalog as described in [CONTRIBUTING.md](CONTRIBUTING.md).

## Contribution principles

Community contributions should be narrow, testable and composable. A skill should not invent analytics, results, facts or sources. Missing required information must be surfaced rather than guessed.

Before opening a pull request, run the local validation suite and follow [CONTRIBUTING.md](CONTRIBUTING.md).

## Version

Current community pack: **1.1.0**

## License

MIT recommended for open community distribution.
