# YouTube Agent Skill - Windows installer for Claude Code
# Repository: https://github.com/faouzileif02/youtube-agent-skill

$ErrorActionPreference = "Stop"

$RepoUrl = "https://github.com/faouzileif02/youtube-agent-skill.git"
$RepoDir = Join-Path $HOME "youtube-agent-skill"
$ClaudeSkillsDir = Join-Path $HOME ".claude\skills"
$SourceSkillsDir = Join-Path $RepoDir "skills"

function Write-Step($Message) {
    Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Fail($Message) {
    Write-Host "`nERROR: $Message" -ForegroundColor Red
    exit 1
}

Write-Host "YouTube Agent Skill V1.1 - Claude Code Installer" -ForegroundColor Green
Write-Host "Installing community skills into: $ClaudeSkillsDir"

Write-Step "Checking Git"
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Fail "Git is not installed or not available in PATH. Install Git for Windows, reopen PowerShell, then run this installer again."
}

Write-Step "Preparing repository"
if (Test-Path (Join-Path $RepoDir ".git")) {
    Write-Host "Existing clone found. Updating it..."
    git -C $RepoDir pull --ff-only
    if ($LASTEXITCODE -ne 0) {
        Fail "Could not update the existing repository. Resolve local Git changes in $RepoDir and run the installer again."
    }
}
elseif (Test-Path $RepoDir) {
    Fail "$RepoDir already exists but is not a Git clone. Rename or remove that folder, then run the installer again."
}
else {
    git clone $RepoUrl $RepoDir
    if ($LASTEXITCODE -ne 0) {
        Fail "Could not clone $RepoUrl"
    }
}

if (-not (Test-Path $SourceSkillsDir)) {
    Fail "The repository does not contain a skills directory: $SourceSkillsDir"
}

Write-Step "Creating Claude skills directory"
New-Item -ItemType Directory -Force -Path $ClaudeSkillsDir | Out-Null

Write-Step "Installing YouTube skills"
$SkillDirs = Get-ChildItem -Path $SourceSkillsDir -Directory | Where-Object {
    Test-Path (Join-Path $_.FullName "SKILL.md")
}

if (-not $SkillDirs -or $SkillDirs.Count -eq 0) {
    Fail "No valid skills containing SKILL.md were found in $SourceSkillsDir"
}

$Installed = 0
foreach ($Skill in $SkillDirs) {
    $Destination = Join-Path $ClaudeSkillsDir $Skill.Name

    if (Test-Path $Destination) {
        Remove-Item -Recurse -Force $Destination
    }

    Copy-Item -Recurse -Force $Skill.FullName $Destination
    $Installed++
    Write-Host "  + $($Skill.Name)" -ForegroundColor DarkGreen
}

Write-Step "Verifying installation"
$Invalid = @()
foreach ($Skill in $SkillDirs) {
    $InstalledSkillFile = Join-Path (Join-Path $ClaudeSkillsDir $Skill.Name) "SKILL.md"
    if (-not (Test-Path $InstalledSkillFile)) {
        $Invalid += $Skill.Name
    }
}

if ($Invalid.Count -gt 0) {
    Fail "Verification failed for: $($Invalid -join ', ')"
}

Write-Host "`nSUCCESS" -ForegroundColor Green
Write-Host "$Installed YouTube Agent skills installed in $ClaudeSkillsDir"
Write-Host ""
Write-Host "Restart Claude Code, then try:" -ForegroundColor Yellow
Write-Host "  /yt-positioning"
Write-Host "  /yt-idea-engine"
Write-Host "  /yt-thumbnail-director"
Write-Host ""
Write-Host "To update later, simply run this install.ps1 again."
