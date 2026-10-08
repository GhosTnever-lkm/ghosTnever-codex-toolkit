param(
    [Parameter(Position = 0, Mandatory = $true)]
    [ValidateSet('list', 'enable', 'disable', 'reset')]
    [string]$Command,

    [Parameter(Position = 1)]
    [string]$Name
)

$skillNames = @(
    'accessibility-audit', 'api-design', 'archive-hardening', 'browser-automation',
    'bug-hunting', 'change-review', 'ci-failure-triage', 'configuration-management',
    'conflict-resolution', 'data-validation', 'database-migrations', 'database-performance',
    'dependency-audit', 'docs-from-code', 'feature-planning', 'flaky-test-triage',
    'game-mod-support', 'git-workflow', 'github-actions', 'implementation-workflow',
    'incident-postmortem', 'incident-response', 'integration-test-design', 'localization-qa',
    'logging-observability', 'mod-compatibility', 'performance-analysis',
    'product-usability-review', 'pull-request-prep', 'python-engineering', 'refactoring-plan',
    'release-packaging', 'release-readiness', 'repo-tour', 'secret-redaction',
    'secure-code-review', 'seo-audit', 'shell-scripting', 'sql-query-review',
    'test-engineering', 'typescript-node'
)

$codexRoot = $env:CODEX_HOME
if (-not $codexRoot) {
    $codexRoot = Join-Path $env:USERPROFILE '.codex'
}
$settingsDirectory = Join-Path $codexRoot 'ghostnever-mega-toolkit'
$settingsPath = Join-Path $settingsDirectory 'settings.json'
$disabledSkills = @()

if (Test-Path -LiteralPath $settingsPath) {
    try {
        $existingSettings = Get-Content -LiteralPath $settingsPath -Raw | ConvertFrom-Json -ErrorAction Stop
        if ($null -ne $existingSettings.disabled) {
            $disabledSkills = @($existingSettings.disabled)
        }
    }
    catch {
        throw "Cannot read toolkit settings at ${settingsPath}: $($_.Exception.Message)"
    }
    $unknownSkills = @($disabledSkills | Where-Object { $_ -notin $skillNames })
    if ($unknownSkills.Count -gt 0) {
        throw "Unknown skill names in settings: $($unknownSkills -join ', ')"
    }
}

switch ($Command) {
    'list' {
        foreach ($skillName in $skillNames) {
            $state = if ($skillName -in $disabledSkills) { 'OFF' } else { 'ON ' }
            '{0}  {1}' -f $state, $skillName
        }
        "`nSettings: $settingsPath"
        return
    }
    'reset' {
        $disabledSkills = @()
    }
    { $_ -in @('enable', 'disable') } {
        if (-not $Name) {
            throw "Provide a skill name. Run '$PSCommandPath list' to see available names."
        }
        if ($Name -eq 'all' -and $Command -eq 'enable') {
            $disabledSkills = @()
        }
        elseif ($Name -notin $skillNames) {
            throw "Unknown skill '$Name'. Run '$PSCommandPath list' to see available names."
        }
        elseif ($Command -eq 'enable') {
            $disabledSkills = @($disabledSkills | Where-Object { $_ -ne $Name })
        }
        else {
            $disabledSkills = @($disabledSkills + $Name | Sort-Object -Unique)
        }
    }
}

New-Item -ItemType Directory -Path $settingsDirectory -Force | Out-Null
$newSettings = [ordered]@{
    version = 1
    disabled = @($disabledSkills | Sort-Object -Unique)
}
$json = $newSettings | ConvertTo-Json -Depth 4
$temporaryPath = Join-Path $settingsDirectory ('.settings-' + [guid]::NewGuid().ToString('N') + '.tmp')
[System.IO.File]::WriteAllText($temporaryPath, $json + [Environment]::NewLine, [System.Text.UTF8Encoding]::new($false))
Move-Item -LiteralPath $temporaryPath -Destination $settingsPath -Force

if ($Command -eq 'reset' -or ($Command -eq 'enable' -and $Name -eq 'all')) {
    'All 41 task skills are enabled.'
}
else {
    '{0} skill: {1}' -f $(if ($Command -eq 'enable') { 'Enabled' } else { 'Disabled' }), $Name
}
"Saved: $settingsPath"
