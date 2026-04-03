<#
用途：
- 将仓库内版本化的 `.githooks/` 安装为当前 clone 的 Git hook 入口。

适合什么时候用：
- 第一次 clone `ai-skill-hub` 后，需要启用 commit message 校验。
- 新机器、新 worktree 或新的独立本地副本需要重新配置 hook。

最短调用示例：
- `powershell.exe -NoProfile -ExecutionPolicy Bypass -File tools\install_git_hooks.ps1`
- `powershell.exe -NoProfile -ExecutionPolicy Bypass -File tools\install_git_hooks.ps1 -RepoPath 'D:\dev\ai-skill-hub'`

安装后效果：
- 当前 clone 会执行 `git config core.hooksPath .githooks`
- 后续 `git commit` 会自动调用 `.githooks/commit-msg`
- `commit-msg` 会进一步调用 `skills/skill-governance/scripts/commit_convention_check.py`

注意：
- `.git/hooks/` 是 Git 本地目录，不作为仓库版本化资产维护。
- 仓库真正版本化的是 `.githooks/` 和本安装脚本。
- 每个新的 clone / worktree 都需要单独执行一次本脚本。
#>
[CmdletBinding()]
param(
    [string]$RepoPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoPath)) {
    $scriptDirectory = Split-Path -Path $PSCommandPath -Parent
    $RepoPath = (Resolve-Path -LiteralPath (Join-Path $scriptDirectory '..')).ProviderPath
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'git was not found in PATH.'
}

$resolvedRepoPath = (Resolve-Path -LiteralPath $RepoPath).ProviderPath
$hooksDirectory = Join-Path $resolvedRepoPath '.githooks'
$commitMsgHook = Join-Path $hooksDirectory 'commit-msg'
$isWorkTree = & git -C $resolvedRepoPath rev-parse --is-inside-work-tree 2>$null
if ($LASTEXITCODE -ne 0 -or $isWorkTree.Trim() -ne 'true') {
    throw "Target path is not a git repository: $resolvedRepoPath"
}

if (-not (Test-Path -LiteralPath $hooksDirectory -PathType Container)) {
    throw "Versioned hooks directory not found: $hooksDirectory"
}

if (-not (Test-Path -LiteralPath $commitMsgHook -PathType Leaf)) {
    throw "commit-msg hook not found: $commitMsgHook"
}

git -C $resolvedRepoPath config core.hooksPath .githooks
if ($LASTEXITCODE -ne 0) {
    throw "Failed to set core.hooksPath for $resolvedRepoPath."
}

Write-Host "[INFO] core.hooksPath => .githooks" -ForegroundColor Yellow
Write-Host "[INFO] This affects the current clone only. Run this script once for each new clone or worktree." -ForegroundColor Yellow
Write-Host "[SUCCESS] Installed repository hooks from .githooks" -ForegroundColor Green
