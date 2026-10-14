# Build one all-in-one Claude.ai Custom Skill ZIP from the 12 community skills.
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceSkills = Join-Path $Root "skills"
$Router = Join-Path $Root "claude-ai\youtube-agent\SKILL.md"
$Build = Join-Path $Root ".build-claude-ai"
$SkillDir = Join-Path $Build "youtube-agent"
$ModulesDir = Join-Path $SkillDir "modules"
$Zip = Join-Path $Root "youtube-agent-all-in-one.zip"

if (-not (Test-Path $Router)) { throw "Missing router: $Router" }
if (-not (Test-Path $SourceSkills)) { throw "Missing skills directory: $SourceSkills" }

if (Test-Path $Build) { Remove-Item -Recurse -Force $Build }
if (Test-Path $Zip) { Remove-Item -Force $Zip }
New-Item -ItemType Directory -Force -Path $ModulesDir | Out-Null
Copy-Item $Router (Join-Path $SkillDir "SKILL.md")

$Skills = Get-ChildItem $SourceSkills -Directory | Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") }
foreach ($Skill in $Skills) {
    $Target = Join-Path $ModulesDir ($Skill.Name + ".md")
    Copy-Item (Join-Path $Skill.FullName "SKILL.md") $Target
    Write-Host " + $($Skill.Name)"
}

Compress-Archive -Path $SkillDir -DestinationPath $Zip -CompressionLevel Optimal
Write-Host ""
Write-Host "READY: $Zip" -ForegroundColor Green
Write-Host "Import this ZIP in Claude.ai as one Custom Skill named youtube-agent."
