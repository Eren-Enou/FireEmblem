param(
    [switch]$List,
    [string]$Scenario,
    [switch]$Check,
    [switch]$FreshBoot,
    [string]$Capture,
    [string]$Label,
    [switch]$Review,
    [switch]$Collect,
    [string[]]$Passed,
    [string[]]$Failed,
    [string]$Notes,
    [string]$Trial = 'human_v1'
)
$ErrorActionPreference = 'Stop'
if (($Check -or $FreshBoot) -and ($Capture -or $Collect -or $Review -or $Passed -or $Failed -or $Notes)) {
    throw 'Use -Check/-FreshBoot separately from evidence collection or observations.'
}
if (($Capture -or $Review) -and ($Passed -or $Failed -or $Notes)) {
    throw 'Use -Collect with observations, or submit observations in a separate command.'
}
$py = Join-Path $PSScriptRoot '../FireEmblemTwoHouses/.venv/Scripts/python.exe'
if (!(Test-Path -LiteralPath $py)) { throw "Python missing: $py" }
$argsList = @('-B', '-m', 'tools.test_scenario', '--trial', $Trial)
if ($List) { $argsList += 'list' }
else {
    if (!$Scenario) { throw 'Use -List or -Scenario NAME. Add -Check for offline validation only.' }
    if ($Capture) {
        if (!$Label) { throw '-Capture requires -Label before/after (or another declared capture label).' }
        $argsList += @('capture', $Scenario, $Label, $Capture)
    }
    elseif ($Collect) {
        $argsList += @('collect', $Scenario)
        foreach ($item in $Passed) { $argsList += @('--passed', $item) }
        foreach ($item in $Failed) { $argsList += @('--failed', $item) }
        if ($Notes) { $argsList += @('--notes', $Notes) }
    }
    elseif ($Review) { $argsList += @('review', $Scenario) }
    elseif ($Passed -or $Failed -or $Notes) {
        $argsList += @('observe', $Scenario)
        foreach ($item in $Passed) { $argsList += @('--passed', $item) }
        foreach ($item in $Failed) { $argsList += @('--failed', $item) }
        if ($Notes) { $argsList += @('--notes', $Notes) }
    }
    else { $argsList += @('check', $Scenario); if ($FreshBoot) { $argsList += '--fresh-boot' } }
}
Push-Location $PSScriptRoot
try {
    $result = & $py @argsList
    if ($LASTEXITCODE -ne 0) { $result | Write-Host; throw 'Scenario refused; Dolphin was not launched.' }
    if ($List -or $Capture -or $Collect -or $Review -or $Passed -or $Failed -or $Notes) { $result | Write-Host; return }
    $plan = ($result -join "`n") | ConvertFrom-Json
    Write-Host $plan.title
    Write-Host "Readiness: $($plan.readiness); Gecko: $($plan.gecko_bytes)/3248 bytes"
    foreach ($step in $plan.steps) { Write-Host " - $step" }
    Write-Host "Evidence folder: $($plan.evidence_directory)"
    if ($Check) { Write-Host 'Offline checks passed. No emulator launched.'; return }
    if ($FreshBoot -and !$plan.changed_card_files.Count) {
        throw 'No native card write detected. Perform original Suspend/Save in this scenario and close Dolphin before fresh native boot. The card was not changed.'
    }
    if (Get-Process -Name Dolphin -ErrorAction SilentlyContinue) { throw 'Close Dolphin completely first; no existing process was changed.' }
    # The owner explicitly invokes this script. Python never launches or drives Dolphin.
    & $plan.executable @($plan.arguments)
}
finally { Pop-Location }
