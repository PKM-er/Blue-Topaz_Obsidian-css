$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$cssPath = Join-Path $root 'theme.css'
$css = Get-Content -Raw -LiteralPath $cssPath

function Assert-True {
    param(
        [Parameter(Mandatory = $true)]
        [bool]$Condition,

        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    if (-not $Condition) {
        throw $Message
    }
}

function Assert-Throws {
    param(
        [Parameter(Mandatory = $true)]
        [scriptblock]$Action,

        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    try {
        & $Action
    }
    catch {
        return
    }

    throw $Message
}

function Assert-SpeechSelectorIsolation {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Section
    )

    $rules = [regex]::Matches($Section, '(?s)([^{}]+)\{([^{}]*)\}')
    foreach ($rule in $rules) {
        $selector = $rule.Groups[1].Value
        if ($selector -notmatch '\[data-task') {
            continue
        }

        Assert-True ($selector -match 'li\.task-list-item|\.HyperMD-task-line') `
            "speech selector must name an allowed task container: $($selector.Trim())"
        Assert-True ($selector -notmatch 'input[^\s,{>+~]*\[data-task') `
            "speech selector must not target a checkbox input: $($selector.Trim())"

        $taskStates = [regex]::Matches($selector, '\[data-task(?:="([^"]+)")?\]')
        Assert-True ($taskStates.Count -gt 0) `
            "speech selector contains an unsupported data-task expression: $($selector.Trim())"

        foreach ($taskState in $taskStates) {
            $value = $taskState.Groups[1].Value
            Assert-True ($value -match '^[0-9]$') `
                "speech selector contains a nonnumeric or bare task state: $($selector.Trim())"
        }
    }
}

Assert-True ($css -notmatch '(?s)\.cm-s-obsidian \.cm-inline-code\.cm-strong\s*\{[^}]*--sb-c') `
    'speech engine must not be scoped to inline code'
Assert-True ([regex]::Matches($css, '--sb-h0\s*:').Count -eq 1) `
    'shared engine must define exactly one base hue'
Assert-True ($css -match '--sb-h0\s*:\s*calc\(var\(--accent-h,\s*350\)\s*\*\s*1deg\)') `
    'base hue must follow accent-h'

1..9 | ForEach-Object {
    $previous = $_ - 1
    Assert-True ($css -match "--sb-h$_\s*:\s*calc\(var\(--sb-h$previous\)\s*\+\s*36deg\)") `
        "hue $_ must advance from hue $previous by 36deg"
}

$speechSectionStart = $css.IndexOf('/*=== Speech Bubble (ported from AnuPpuccin) ===*/')
Assert-True ($speechSectionStart -ge 0) 'speech component section must exist'
$speechSection = $css.Substring($speechSectionStart)
Assert-SpeechSelectorIsolation $speechSection

Assert-Throws { Assert-SpeechSelectorIsolation 'body.bt-speech-bubble [data-task="0"] { background: red; }' } `
    'selector guard must reject a bare numeric data-task target'
Assert-Throws { Assert-SpeechSelectorIsolation 'body.bt-speech-bubble .HyperMD-task-line input[data-task="0"] { padding: 2px; }' } `
    'selector guard must reject numeric checkbox input targets'
Assert-Throws { Assert-SpeechSelectorIsolation 'body.bt-speech-bubble .HyperMD-task-line input.task-list-item-checkbox[type="checkbox"][data-task="0"] { background: red; }' } `
    'selector guard must reject decorated numeric checkbox input targets'
Assert-Throws { Assert-SpeechSelectorIsolation 'body.bt-speech-bubble .HyperMD-task-line[data-task] { margin-block: 2px; }' } `
    'selector guard must reject unrestricted task states'
Assert-Throws { Assert-SpeechSelectorIsolation 'body.bt-speech-bubble .HyperMD-task-line[data-task="x"] { margin-block: 2px; }' } `
    'selector guard must reject alternative checkbox states'

Assert-True ($css -match 'body\.bt-speech-bubble :is\(li\.task-list-item, \.HyperMD-task-line\)') `
    'bubble rules must target reading and live-preview containers explicitly'
Assert-True ($css -match '(?s)color-scheme-options-monochrome-topaz[^}]*--sb-c\s*:\s*0') `
    'Monochrome must use zero chroma'

0..9 | ForEach-Object {
    $next = ($_ + 1) % 10
    $taskSelector = [regex]::Escape("[data-task=`"$_`"]")
    $mapping = $taskSelector + '[^{]*\{[^}]*linear-gradient\(var\(--sb-angle\),\s*var\(--bt-speech-' + $_ + '\),\s*var\(--bt-speech-' + $next + '\)\)'
    Assert-True ($css -match $mapping) "bubble $_ must map to $next"
}

$speechSettings = [regex]::Match($css, '(?s)id:\s*bt-speech-bubble.*?default:\s*false').Value
$englishDescription = [regex]::Match($speechSettings, '(?m)^\s*description:\s*(.+)$').Groups[1].Value
$chineseDescription = [regex]::Match($speechSettings, '(?m)^\s*description\.zh:\s*(.+)$').Groups[1].Value
Assert-True ($englishDescription.Contains('- [0]') -and $englishDescription.Contains('- [9]')) `
    'Style Settings English description must use literal task syntax'
Assert-True ($chineseDescription.Contains('- [0]') -and $chineseDescription.Contains('- [9]')) `
    'Style Settings Chinese description must use literal task syntax'

$documentation = Get-ChildItem -LiteralPath (Join-Path $root 'docs\superpowers') -File -Recurse |
    ForEach-Object { Get-Content -Raw -LiteralPath $_.FullName }
Assert-True (($documentation -join "`n") -notmatch '[A-Z]:\\') `
    'documentation must not contain machine-specific Windows paths'

Write-Output 'speech-bubble-css: PASS'
