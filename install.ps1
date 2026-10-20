# Installs the Code Monkey AMOLED theme into Equicord's themes folder.
# Resolves the folder the same way Equicord does:
#   EQUICORD_USER_DATA_DIR, else DISCORD_USER_DATA_DIR\..\EquicordData, else %APPDATA%\Equicord

$ErrorActionPreference = 'Stop'

$themeFile = Join-Path $PSScriptRoot 'code-monkey-amoled.theme.css'
if (-not (Test-Path $themeFile)) {
    throw "Theme file not found: $themeFile"
}

if ($env:EQUICORD_USER_DATA_DIR) {
    $dataDir = $env:EQUICORD_USER_DATA_DIR
} elseif ($env:DISCORD_USER_DATA_DIR) {
    $dataDir = Join-Path $env:DISCORD_USER_DATA_DIR '..\EquicordData'
} else {
    $dataDir = Join-Path $env:APPDATA 'Equicord'
}

if (-not (Test-Path $dataDir)) {
    throw "Equicord data folder not found at $dataDir. Install Equicord and start Discord once, then run this again."
}

$themesDir = Join-Path $dataDir 'themes'
New-Item -ItemType Directory -Force -Path $themesDir | Out-Null

$target = Join-Path $themesDir (Split-Path $themeFile -Leaf)
Copy-Item -Path $themeFile -Destination $target -Force

Write-Host "Installed to $((Resolve-Path $target).Path)"
Write-Host 'Enable it in Discord: Settings > Equicord > Themes.'
