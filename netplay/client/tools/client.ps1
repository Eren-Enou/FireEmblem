# FE9 two-army co-op: Netplay client launcher (Player 2).
# Built into the client ZIP by tools/netplay_package.py. ASCII only (Windows PowerShell 5.1 reads it as ANSI).
#
# Start-FE9-Coop.bat   first run: finds Dolphin.exe and your game folder, then starts Dolphin with the
#                      private user folder in this package (your own Dolphin settings, saves and memory
#                      cards are never read or changed)
# Check-Setup.bat      the validation checklist only (nothing is started)
#
# Parameters (optional): -Dolphin <path to Dolphin.exe>  -Games <folder with the game>  -Check  -NoLaunch
#                        -PrintFingerprint <GFEE01.ini>   (prints the code fingerprint and exits)

param(
    [Parameter(Position = 0)][string]$Dolphin = "",
    [string]$Games = "",
    [switch]$Check,
    [switch]$NoLaunch,
    [string]$PrintFingerprint = ""
)

$ErrorActionPreference = "Stop"
$Here = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$User = Join-Path $Here "User"
$Ini = Join-Path $User "Config\Dolphin.ini"
$Codes = Join-Path $User "GameSettings\GFEE01.ini"
$Manifest = Join-Path $Here "MANIFEST.txt"
$SavedDolphin = Join-Path $Here "dolphin_path.txt"

# The code fingerprint: SHA-256 over the enabled codes, the same rule as tools/netplay_package.py.
function Get-CodeFingerprint([string]$Path) {
    $sections = @{}
    $order = New-Object System.Collections.ArrayList
    $cur = $null
    foreach ($raw in [IO.File]::ReadAllLines($Path)) {
        $s = $raw.Trim()
        if (-not $s -or $s.StartsWith("#")) { continue }
        if ($s.StartsWith("[") -and $s.EndsWith("]")) {
            $cur = $s.Substring(1, $s.Length - 2)
            if (-not $sections.ContainsKey($cur)) { $sections[$cur] = New-Object System.Collections.ArrayList }
            continue
        }
        if ($cur) { [void]$sections[$cur].Add($s) }
    }
    $out = New-Object System.Collections.ArrayList
    $names = New-Object System.Collections.ArrayList
    foreach ($kind in @("ActionReplay", "Gecko")) {
        if (-not $sections.ContainsKey($kind)) { continue }
        $enabled = New-Object 'System.Collections.Generic.HashSet[string]'
        if ($sections.ContainsKey($kind + "_Enabled")) {
            foreach ($l in $sections[$kind + "_Enabled"]) { if ($l.StartsWith('$')) { [void]$enabled.Add($l.Substring(1).Trim()) } }
        }
        $take = $false
        foreach ($l in $sections[$kind]) {
            if ($l.StartsWith('$')) {
                $name = $l.Substring(1).Trim()
                $take = $enabled.Contains($name)
                if ($take) { [void]$out.Add($kind + ':$' + $name); [void]$names.Add($name) }
                continue
            }
            if ($take -and -not $l.StartsWith("*")) { [void]$out.Add((($l -split '\s+') -join " ").ToUpperInvariant()) }
        }
    }
    $text = ($out -join "`n") + "`n"
    $sha = [System.Security.Cryptography.SHA256]::Create()
    $hash = $sha.ComputeHash([Text.Encoding]::UTF8.GetBytes($text))
    $hex = -join ($hash | ForEach-Object { $_.ToString("x2") })
    return @{ Fingerprint = $hex.Substring(0, 16); Names = $names }
}

function Get-IniValue([string]$Text, [string]$Section, [string]$Key) {
    $in = $false
    foreach ($line in ($Text -split "`r?`n")) {
        $t = $line.Trim()
        if ($t.StartsWith("[")) { $in = ($t -eq "[$Section]"); continue }
        if ($in -and $t -match "^([^=]+?)\s*=\s*(.*)$" -and $Matches[1] -eq $Key) { return $Matches[2] }
    }
    return $null
}

function Set-IniValues([string]$Text, [string]$Section, [hashtable]$Items) {
    $lines = New-Object System.Collections.ArrayList
    foreach ($l in ($Text -split "`r?`n")) { [void]$lines.Add($l) }
    while ($lines.Count -gt 0 -and $lines[$lines.Count - 1] -eq "") { $lines.RemoveAt($lines.Count - 1) }
    $start = $lines.IndexOf("[$Section]")
    if ($start -lt 0) { [void]$lines.Add("[$Section]"); $start = $lines.Count - 1 }
    $end = $start + 1
    while ($end -lt $lines.Count -and -not $lines[$end].StartsWith("[")) { $end++ }
    foreach ($k in $Items.Keys) {
        $found = $false
        for ($i = $start + 1; $i -lt $end; $i++) {
            if ($lines[$i] -match "^([^=]+?)\s*=" -and $Matches[1] -eq $k) { $lines[$i] = "$k = $($Items[$k])"; $found = $true }
        }
        if (-not $found) { $lines.Insert($end, "$k = $($Items[$k])"); $end++ }
    }
    return ($lines -join "`r`n") + "`r`n"
}

function Read-Manifest {
    $m = @{}
    foreach ($l in [IO.File]::ReadAllLines($Manifest)) { if ($l -match "^([a-z_]+)=(.*)$") { $m[$Matches[1]] = $Matches[2] } }
    return $m
}

function Find-Dolphin {
    if ($Dolphin) { return $Dolphin }
    if (Test-Path $SavedDolphin) {
        $p = ([IO.File]::ReadAllText($SavedDolphin)).Trim()
        if (Test-Path $p) { return $p }
    }
    $candidates = @(
        (Join-Path (Split-Path -Parent $Here) "Dolphin.exe"),
        (Join-Path (Split-Path -Parent $Here) "Dolphin-x64\Dolphin.exe"),
        (Join-Path $env:ProgramFiles "Dolphin\Dolphin.exe"),
        (Join-Path $env:ProgramFiles "Dolphin-x64\Dolphin.exe")
    )
    foreach ($c in $candidates) { if (Test-Path $c) { return $c } }
    if ($Check) { return $null }
    Add-Type -AssemblyName System.Windows.Forms
    $dlg = New-Object System.Windows.Forms.OpenFileDialog
    $dlg.Title = "Select Dolphin.exe (Dolphin version shown in README.txt)"
    $dlg.Filter = "Dolphin.exe|Dolphin.exe"
    if ($dlg.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) { return $dlg.FileName }
    return $null
}

function Find-Games([string]$Current) {
    if ($Games) { return $Games }
    if ($Current -and (Test-Path $Current)) { return $Current }
    if ($Check) { return $null }
    Add-Type -AssemblyName System.Windows.Forms
    $dlg = New-Object System.Windows.Forms.FolderBrowserDialog
    $dlg.Description = "Select the folder that contains your Fire Emblem: Path of Radiance (USA) disc image"
    if ($dlg.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) { return $dlg.SelectedPath }
    return $null
}

function Test-DolphinVersion([string]$Exe, [string]$Version) {
    # Dolphin embeds its version as the NUL-terminated string "Dolphin <version>"; Netplay itself also
    # refuses a different version.
    $bytes = [IO.File]::ReadAllBytes($Exe)
    $text = [Text.Encoding]::GetEncoding(28591).GetString($bytes)
    return $text.Contains("Dolphin $Version" + [char]0)
}

if ($PrintFingerprint) {
    $r = Get-CodeFingerprint $PrintFingerprint
    Write-Output $r.Fingerprint
    exit 0
}

if (-not (Test-Path $Ini) -or -not (Test-Path $Manifest)) {
    Write-Host "This folder is incomplete. Extract the whole ZIP first (right-click > Extract All), then run Start-FE9-Coop.bat from the extracted folder."
    exit 1
}

$m = Read-Manifest
$problems = New-Object System.Collections.ArrayList
$text = [IO.File]::ReadAllText($Ini)

Write-Host "FE9 co-op Netplay client - package $($m['package_version']), codes $($m['codes'])"
Write-Host ""

# 1. Dolphin
$exe = Find-Dolphin
if (-not $exe -or -not (Test-Path $exe)) {
    [void]$problems.Add("Dolphin.exe not found. Drag Dolphin.exe onto Start-FE9-Coop.bat, or put this folder next to Dolphin.exe.")
} else {
    $exe = (Resolve-Path $exe).Path
    if (-not $Check) { [IO.File]::WriteAllText($SavedDolphin, $exe) }
    if (Test-DolphinVersion $exe $m["dolphin_version"]) {
        Write-Host "[OK]   Dolphin $($m['dolphin_version']): $exe"
    } else {
        [void]$problems.Add("Dolphin at $exe is not version $($m['dolphin_version']). Install exactly that version (README.txt).")
    }
}

# 2. Game folder
$gamesNow = Get-IniValue $text "General" "ISOPath0"
$g = Find-Games $gamesNow
if (-not $g -or -not (Test-Path $g)) {
    [void]$problems.Add("No game folder set. Run Start-FE9-Coop.bat and choose the folder with your game.")
} else {
    $g = (Resolve-Path $g).Path
    if (-not $Check -and $g -ne $gamesNow) { $text = Set-IniValues $text "General" @{ "ISOPaths" = "1"; "ISOPath0" = $g } }
    $images = @(Get-ChildItem -LiteralPath $g -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -match '^\.(iso|gcm|ciso|gcz|rvz|wia|nkit)$' })
    if ($images.Count -gt 0) {
        Write-Host "[OK]   Game folder: $g ($($images.Count) disc image(s); Dolphin must list GFEE01, revision 0)"
    } else {
        [void]$problems.Add("No disc image (.iso/.rvz/.ciso/.gcz/.gcm) found directly in $g.")
    }
}

# 3. Settings this package relies on
$expect = [ordered]@{
    "Core/EnableCheats" = "True"; "Core/SIDevice0" = "6"; "NetPlay/TraversalChoice" = "traversal";
    "NetPlay/TraversalServer" = $m["traversal_server"]; "NetPlay/TraversalPort" = $m["traversal_port"]
}
foreach ($k in $expect.Keys) {
    $sec, $key = $k.Split("/")
    $v = Get-IniValue $text $sec $key
    if ($v -eq $expect[$k]) { Write-Host "[OK]   $sec $key = $v" }
    else { [void]$problems.Add("Dolphin.ini [$sec] $key is '$v', expected '$($expect[$k])' (re-extract the ZIP to reset it).") }
}
$nick = Get-IniValue $text "NetPlay" "Nickname"
Write-Host "[OK]   Netplay nickname: $nick"

# 4. Codes
$fp = Get-CodeFingerprint $Codes
if ($fp.Fingerprint -eq $m["codes_fingerprint"]) {
    Write-Host "[OK]   Code fingerprint $($fp.Fingerprint) (enabled: $($fp.Names -join ' + '))"
} else {
    [void]$problems.Add("Code fingerprint is $($fp.Fingerprint), expected $($m['codes_fingerprint']). Re-extract the ZIP.")
}

# 5. Controller
$pads = Join-Path $User "Config\GCPadNew.ini"
if ((Test-Path $pads) -and (Get-IniValue ([IO.File]::ReadAllText($pads)) "GCPad1" "Device")) {
    Write-Host "[OK]   Controller 1 configured (keyboard; change it in Controllers > Port 1 > Configure)"
} else {
    [void]$problems.Add("Controller 1 has no configuration (Config\GCPadNew.ini).")
}

# Keep what was found (Dolphin path, game folder) even when something else still needs fixing.
if (-not $Check) { [IO.File]::WriteAllText($Ini, $text) }
Write-Host ""
if ($problems.Count -gt 0) {
    foreach ($p in $problems) { Write-Host "[FIX]  $p" }
    Write-Host ""
    Write-Host "Not ready: fix the items marked [FIX]."
    exit 1
}

Write-Host "Ready. Tell the host this fingerprint: $($fp.Fingerprint)"
if ($Check -or $NoLaunch) { exit 0 }

Write-Host "Starting Dolphin with this package's user folder..."
Start-Process -FilePath $exe -ArgumentList @("--user", "`"$User`"")
exit 0
