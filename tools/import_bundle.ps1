<#
用途：
- 从 `.bundle` 文件导入或更新 skill hub Git 仓库。

适合什么时候用：
- 在新机器上从 bundle 恢复仓库
- 用 bundle 给现有本地仓库补最新提交

最短调用示例：
- `.\tools\import_bundle.ps1`
- `.\tools\import_bundle.ps1 -RepoPath 'D:\dev\codex-skill-hub' -BundlePath 'D:\backup\codex-skill-hub_latest.bundle'`

注意：
- 如果目标仓库已存在，脚本会先检查工作区是否干净；有未提交改动时会中止导入。
- 默认 bundle 路径为 `D:\BaiduSyncdisk\Python_Lib\Git_Bundle\codex-skill-hub_latest.bundle`。
#>
[CmdletBinding()]
param(
    [string]$RepoPath,
    [string]$BundlePath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoPath)) {
    $scriptDirectory = Split-Path -Path $PSCommandPath -Parent
    $RepoPath = Join-Path (Split-Path -Path $scriptDirectory -Parent) 'codex-skill-hub'
    if (Test-Path -LiteralPath $RepoPath -PathType Container) {
        $RepoPath = (Resolve-Path -LiteralPath $RepoPath).ProviderPath
    }
}

if ([string]::IsNullOrWhiteSpace($BundlePath)) {
    $BundlePath = 'D:\BaiduSyncdisk\Python_Lib\Git_Bundle\codex-skill-hub_latest.bundle'
}

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
