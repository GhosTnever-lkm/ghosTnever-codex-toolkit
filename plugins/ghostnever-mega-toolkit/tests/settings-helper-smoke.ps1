$ErrorActionPreference = 'Stop'

$helperPath = Join-Path $PSScriptRoot '..\scripts\mega_toolkit_settings.ps1'
$testRoot = Join-Path $env:TEMP ('ghostnever-toolkit-smoke-' + [guid]::NewGuid().ToString('N'))
$previousCodexHome = $env:CODEX_HOME

try {
    $env:CODEX_HOME = $testRoot
    $settingsDirectory = Join-Path $testRoot 'ghostnever-mega-toolkit'
    New-Item -ItemType Directory -Path $settingsDirectory -Force | Out-Null
    $settingsPath = Join-Path $settingsDirectory 'settings.json'
    $initialSettings = [ordered]@{
        version = 7
        disabled = @('docs-from-code')
        appearance = @{ theme = 'dark'; keep = $true }
    }
    $initialJson = $initialSettings | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText(
        $settingsPath,
        $initialJson,
        [System.Text.UTF8Encoding]::new($false)
    )

    & $helperPath -Command enable -Name docs-from-code | Out-Null
    & $helperPath -Command disable -Name api-design | Out-Null
    $saved = Get-Content -LiteralPath $settingsPath -Raw | ConvertFrom-Json
    if ($saved.disabled.Count -ne 1 -or $saved.disabled[0] -ne 'api-design') {
        throw 'Enable/disable did not update the disabled-skill list.'
    }
    if (-not $saved.appearance.keep -or $saved.appearance.theme -ne 'dark') {
        throw 'Unrelated settings were not preserved.'
    }

    $listOutput = @(& $helperPath -Command list)
    $listedSkillNames = @(
        foreach ($line in $listOutput) {
            $match = [regex]::Match($line, '^(?:ON|OFF)\s+(?<name>[a-z0-9-]+)$')
            if ($match.Success) {
                $match.Groups['name'].Value
            }
        }
    )
    $skillRoot = Join-Path $PSScriptRoot '..\skills'
    $actualSkillNames = @(
        Get-ChildItem -LiteralPath $skillRoot -Directory |
            Where-Object { $_.Name -ne 'toolkit-settings' } |
            ForEach-Object { $_.Name } |
            Sort-Object
    )
    $listedNormalized = (@($listedSkillNames | Sort-Object)) -join ','
    $actualNormalized = (@($actualSkillNames | Sort-Object)) -join ','
    if ($listedNormalized -cne $actualNormalized) {
        throw "PowerShell helper skill names do not match the task-skill directories. Listed: $($listedSkillNames -join ','); actual: $($actualSkillNames -join ',')."
    }
    if ($listedSkillNames.Count -ne 41) {
        throw "Expected 41 listed task skills, got $($listedSkillNames.Count)."
    }

    & $helperPath -Command reset | Out-Null
    $saved = Get-Content -LiteralPath $settingsPath -Raw | ConvertFrom-Json
    if ($saved.disabled.Count -ne 0) {
        throw 'Reset did not enable all task skills.'
    }
    if (-not $saved.appearance.keep -or $saved.appearance.theme -ne 'dark') {
        throw 'Reset did not preserve unrelated settings.'
    }

    'PowerShell settings helper smoke test passed.'
}
finally {
    if ($null -eq $previousCodexHome) {
        Remove-Item Env:CODEX_HOME -ErrorAction SilentlyContinue
    }
    else {
        $env:CODEX_HOME = $previousCodexHome
    }
    if (Test-Path -LiteralPath $testRoot) {
        Remove-Item -LiteralPath $testRoot -Recurse -Force
    }
}
