[CmdletBinding()]
param(
    [string]$RepoPath = 'D:\dev\codex-skill-hub',
    [string]$OutputDir = 'D:\BaiduSyncdisk\Python_Lib\Git_Bundle'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Step {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    Write-Host ""
    Write-Host "[STEP] $Message" -ForegroundColor Cyan
}

function Write-Info {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    Write-Host "[INFO] $Message" -ForegroundColor Yellow
}

function Write-Success {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    Write-Host "[SUCCESS] $Message" -ForegroundColor Green
}

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,

        [switch]$CaptureOutput
    )

    if ($CaptureOutput) {
        $output = & git @Arguments 2>&1
        $exitCode = $LASTEXITCODE
        if ($exitCode -ne 0) {
            throw "git $($Arguments -join ' ') failed with exit code $exitCode.`n$($output -join [Environment]::NewLine)"
        }
        return $output
    }

    & git @Arguments
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        throw "git $($Arguments -join ' ') failed with exit code $exitCode."
    }
}

try {
    Write-Step 'Checking git availability'
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        throw 'git was not found in PATH.'
    }

    Write-Step 'Checking repository'
    if (-not (Test-Path -LiteralPath $RepoPath -PathType Container)) {
        throw "Repository path not found: $RepoPath"
    }

    $resolvedRepoPath = (Resolve-Path -LiteralPath $RepoPath).ProviderPath
    $isWorkTree = @(Invoke-Git -Arguments @('-C', $resolvedRepoPath, 'rev-parse', '--is-inside-work-tree') -CaptureOutput)
    if ($isWorkTree.Count -eq 0 -or $isWorkTree[0].Trim() -ne 'true') {
        throw "Target path is not a git repository: $resolvedRepoPath"
    }

    Write-Step 'Checking working tree status'
    $statusLines = @(Invoke-Git -Arguments @('-C', $resolvedRepoPath, 'status', '--porcelain=v1') -CaptureOutput)
    if ($statusLines.Count -gt 0) {
        Invoke-Git -Arguments @('-C', $resolvedRepoPath, 'status')
        throw 'Working tree is dirty. Export aborted.'
    }

    $currentBranch = @(Invoke-Git -Arguments @('-C', $resolvedRepoPath, 'branch', '--show-current') -CaptureOutput)
    $branchName = if ($currentBranch.Count -gt 0 -and -not [string]::IsNullOrWhiteSpace($currentBranch[0])) {
        $currentBranch[0].Trim()
    }
    else {
        'main'
    }

    if (-not (Test-Path -LiteralPath $OutputDir -PathType Container)) {
        New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
    }

    $resolvedOutputDir = (Resolve-Path -LiteralPath $OutputDir).ProviderPath
    $dateStamp = Get-Date -Format 'yyyy-MM-dd'
    $latestBundlePath = Join-Path $resolvedOutputDir 'codex-skill-hub_latest.bundle'
    $versionedBundlePath = Join-Path $resolvedOutputDir ("codex-skill-hub_{0}_v1.bundle" -f $dateStamp)

    Write-Step 'Creating latest bundle'
    Invoke-Git -Arguments @('-C', $resolvedRepoPath, 'bundle', 'create', $latestBundlePath, '--all')

    Write-Step 'Creating versioned bundle'
    Invoke-Git -Arguments @('-C', $resolvedRepoPath, 'bundle', 'create', $versionedBundlePath, '--all')

    Write-Step 'Verifying bundle'
    Invoke-Git -Arguments @('-C', $resolvedRepoPath, 'bundle', 'verify', $latestBundlePath)
    Invoke-Git -Arguments @('-C', $resolvedRepoPath, 'bundle', 'verify', $versionedBundlePath)

    Write-Info "Current branch: $branchName"
    Write-Info "Latest bundle: $latestBundlePath"
    Write-Info "Versioned bundle: $versionedBundlePath"
    Write-Success 'Bundle export completed'
}
catch {
    Write-Host ""
    Write-Error "[FAILED] $($_.Exception.Message)"
    exit 1
}
