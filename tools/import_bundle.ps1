[CmdletBinding()]
param(
    [string]$RepoPath = 'D:\dev\codex-skill-hub',
    [string]$BundlePath = 'D:\BaiduSyncdisk\Python_Lib\Git_Bundle\codex-skill-hub_latest.bundle'
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

    Write-Step 'Validating bundle file'
    if (-not (Test-Path -LiteralPath $BundlePath -PathType Leaf)) {
        throw "Bundle file not found: $BundlePath"
    }

    $resolvedBundlePath = (Resolve-Path -LiteralPath $BundlePath).ProviderPath
    Invoke-Git -Arguments @('bundle', 'verify', $resolvedBundlePath)

    if (-not (Test-Path -LiteralPath $RepoPath)) {
        Write-Step 'Target repository does not exist; cloning from bundle'
        $parentPath = Split-Path -Parent $RepoPath
        if ([string]::IsNullOrWhiteSpace($parentPath)) {
            throw "Cannot determine parent directory for repo path: $RepoPath"
        }

        if (-not (Test-Path -LiteralPath $parentPath)) {
            New-Item -ItemType Directory -Path $parentPath -Force | Out-Null
        }

        Invoke-Git -Arguments @('clone', $resolvedBundlePath, $RepoPath)
    }
    else {
        Write-Step 'Target repository exists; validating repository metadata'
        $gitDirPath = Join-Path $RepoPath '.git'
        if (-not (Test-Path -LiteralPath $gitDirPath)) {
            throw "Target path exists but is not a git repository: $RepoPath"
        }

        Write-Step 'Checking working tree status'
        $statusLines = @(Invoke-Git -Arguments @('-C', $RepoPath, 'status', '--porcelain=v1') -CaptureOutput)
        if ($statusLines.Count -gt 0) {
            Write-Host 'Repository has uncommitted changes:' -ForegroundColor Yellow
            $statusLines | ForEach-Object { Write-Host "  $_" -ForegroundColor Yellow }
            throw 'Working tree is dirty. Import aborted.'
        }

        Write-Step 'Fetching updates from bundle'
        Invoke-Git -Arguments @('-C', $RepoPath, 'fetch', $resolvedBundlePath)

        Write-Step 'Merging FETCH_HEAD'
        Invoke-Git -Arguments @('-C', $RepoPath, 'merge', '--no-edit', 'FETCH_HEAD')
    }

    Write-Step 'Showing final git status'
    Invoke-Git -Arguments @('-C', $RepoPath, 'status')

    Write-Step 'Showing latest 3 commits'
    Invoke-Git -Arguments @('-C', $RepoPath, 'log', '--oneline', '--decorate', '-3')
}
catch {
    Write-Host "" 
    Write-Error "[FAILED] $($_.Exception.Message)"
    exit 1
}
