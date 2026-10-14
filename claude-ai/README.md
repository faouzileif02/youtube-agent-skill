# Claude.ai all-in-one package

This directory contains the router used to package all community YouTube skills as one Claude.ai Custom Skill.

## Build on Windows

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\build-claude-ai.ps1
```

The command creates:

```text
youtube-agent-all-in-one.zip
```

Import that ZIP into Claude.ai Custom Skills. The installed skill is named `youtube-agent` and automatically routes a request to the relevant internal module.

The ZIP contains one root folder:

```text
youtube-agent/
├── SKILL.md
└── modules/
    ├── yt-positioning.md
    ├── yt-idea-engine.md
    └── ...
```
