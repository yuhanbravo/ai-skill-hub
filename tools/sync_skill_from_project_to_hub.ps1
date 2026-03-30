<#
用途：
- 将某个真实项目里的单个 skill 回拷到当前 skill hub，适合把项目内试跑后的 skill 沉淀回母库。

适合什么时候用：
- 你在某个项目的 `.codex/skills/<skill-name>` 中改了内容，想同步回 hub
- 想只同步一个 skill，而不是整个 `.codex/skills`

最短调用示例：
- `\.\tools\sync_skill_from_project_to_hub.ps1 -ProjectPath 'D:\my-project' -SkillHubPath 'D:\dev\ai-skill-hub' -SkillName 'chatgpt-handoff-pilot'`
- `\.\tools\sync_skill_from_project_to_hub.ps1 -ProjectPath 'D:\my-project' -SkillHubPath 'D:\dev\ai-skill-hub' -SkillName 'chatgpt-handoff-pilot' -DryRun`

注意：
- 来源目录固定读取项目下的 `.codex\skills\<SkillName>`，该入口继续作为兼容消费入口保留
- 默认会覆盖 hub 中同名文件；建议先用 `-DryRun`
- 如果 hub 中还没有这个 skill，可加 `-CreateIfMissing`
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,

    [Parameter(Mandatory = $true)]
    [string]$SkillHubPath,

    [Parameter(Mandatory = $true)]
    [string]$SkillName,

    [switch]$DryRun,
    [switch]$CreateIfMissing
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

function Write-WarnMessage {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    Write-Host "[WARN] $Message" -ForegroundColor DarkYellow
}

function Write-Success {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    Write-Host "[SUCCESS] $Message" -ForegroundColor Green
}

function Assert-DirectoryExists {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [string]$Description
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        throw "$Description not found: $Path"
    }
}

function New-DirectoryIfMissing {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (Test-Path -LiteralPath $Path -PathType Container) {
        return
    }

    if ($DryRun) {
        Write-Info "DryRun: would create directory $Path"
        return
    }

    New-Item -ItemType Directory -Path $Path -Force | Out-Null
    Write-Info "Created directory: $Path"
}

function Get-NormalizedRelativePath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RootPath,

        [Parameter(Mandatory = $true)]
        [string]$FullPath
    )

    $normalizedRootPath = [System.IO.Path]::GetFullPath($RootPath)
    $normalizedFullPath = [System.IO.Path]::GetFullPath($FullPath)
    $rootPrefix = if ($normalizedRootPath.EndsWith('\') -or $normalizedRootPath.EndsWith('/')) {
        $normalizedRootPath
    }
    else {
        "$normalizedRootPath\"
    }

    if ([System.IO.Path]::GetPathRoot($normalizedRootPath) -ne [System.IO.Path]::GetPathRoot($normalizedFullPath)) {
        throw "Cannot compute relative path across different drive roots: $normalizedRootPath -> $normalizedFullPath"
    }

    if (-not $normalizedFullPath.StartsWith($rootPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Path is not under root: $normalizedFullPath -> $normalizedRootPath"
    }

    return $normalizedFullPath.Substring($rootPrefix.Length)
}

function Get-SkillFiles {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RootPath
    )

    $excludedDirectoryNames = @('__pycache__', '.git', '.tmp', '.pytest_cache', '.mypy_cache')
    $excludedExtensions = @('.pyc', '.pyo')

    return Get-ChildItem -LiteralPath $RootPath -Recurse -File | Where-Object {
        $file = $_
        if ($excludedExtensions -contains $file.Extension) {
            return $false
        }

        foreach ($segment in $file.FullName.Substring($RootPath.Length).TrimStart('\').Split('\\')) {
            if ($excludedDirectoryNames -contains $segment) {
                return $false
            }
        }

        return $true
    } | Sort-Object FullName
}

function Get-CopyPlan {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SourceRoot,

        [Parameter(Mandatory = $true)]
        [string]$TargetRoot
    )

    $plan = @()
    foreach ($sourceFile in (Get-SkillFiles -RootPath $SourceRoot)) {
        $relativePath = Get-NormalizedRelativePath -RootPath $SourceRoot -FullPath $sourceFile.FullName
        $targetFile = Join-Path $TargetRoot $relativePath
        $status = if (Test-Path -LiteralPath $targetFile -PathType Leaf) { 'overwrite' } else { 'new' }

        $plan += [pscustomobject]@{
            RelativePath = $relativePath
            SourcePath = $sourceFile.FullName
            TargetPath = $targetFile
            Status = $status
        }
    }

    return $plan
}

function Copy-PlannedFiles {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Plan
    )

    $copied = @()
    foreach ($item in $Plan) {
        $targetParent = Split-Path -Parent $item.TargetPath
        New-DirectoryIfMissing -Path $targetParent

        if ($DryRun) {
            Write-Info "DryRun: would copy $($item.RelativePath) [$($item.Status)]"
        }
        else {
            Copy-Item -LiteralPath $item.SourcePath -Destination $item.TargetPath -Force
            Write-Info "Copied $($item.RelativePath) [$($item.Status)]"
        }

        $copied += $item
    }

    return $copied
}

try {
    Write-Step 'Validating paths'
    Assert-DirectoryExists -Path $ProjectPath -Description 'Project path'
    Assert-DirectoryExists -Path $SkillHubPath -Description 'Skill hub path'

    $resolvedProjectPath = (Resolve-Path -LiteralPath $ProjectPath).ProviderPath
    $resolvedSkillHubPath = (Resolve-Path -LiteralPath $SkillHubPath).ProviderPath

    $trimmedSkillName = $SkillName.Trim()
    if ([string]::IsNullOrWhiteSpace($trimmedSkillName)) {
        throw 'SkillName cannot be empty.'
    }

    if ($trimmedSkillName.Contains('\') -or $trimmedSkillName.Contains('/')) {
        throw 'SkillName must be a single skill directory name, not a path.'
    }

    $sourceSkillPath = Join-Path $resolvedProjectPath (Join-Path '.codex\skills' $trimmedSkillName)
    $targetSkillsRoot = Join-Path $resolvedSkillHubPath 'skills'
    $targetSkillPath = Join-Path $targetSkillsRoot $trimmedSkillName

    Assert-DirectoryExists -Path $sourceSkillPath -Description 'Source skill'
    Assert-DirectoryExists -Path $targetSkillsRoot -Description 'Skill hub skills directory'

    if (-not (Test-Path -LiteralPath $targetSkillPath -PathType Container)) {
        if (-not $CreateIfMissing) {
            throw "Target skill not found: $targetSkillPath`nRe-run with -CreateIfMissing to create it."
        }

        Write-WarnMessage "Target skill does not exist and will be created: $targetSkillPath"
        New-DirectoryIfMissing -Path $targetSkillPath
    }

    $copyPlan = @(Get-CopyPlan -SourceRoot $sourceSkillPath -TargetRoot $targetSkillPath)
    if ($copyPlan.Count -eq 0) {
        throw "Source skill contains no eligible files: $sourceSkillPath"
    }

    Write-Step 'Previewing sync plan'
    Write-Info "Source path: $sourceSkillPath"
    Write-Info "Target path: $targetSkillPath"
    Write-Info "Planned file count: $($copyPlan.Count)"
    foreach ($item in $copyPlan) {
        Write-Host ("  [{0}] {1}" -f $item.Status.ToUpperInvariant(), $item.RelativePath)
    }

    Write-Step 'Syncing single skill'
    $copiedFiles = @(Copy-PlannedFiles -Plan $copyPlan)

    $newFiles = @($copiedFiles | Where-Object { $_.Status -eq 'new' })
    $overwrittenFiles = @($copiedFiles | Where-Object { $_.Status -eq 'overwrite' })

    Write-Step 'Summary'
    Write-Info "Actual copied files: $($copiedFiles.Count)"
    foreach ($item in $copiedFiles) {
        Write-Host ("  [{0}] {1}" -f $item.Status.ToUpperInvariant(), $item.RelativePath)
    }

    Write-Info "Has new files: $(if ($newFiles.Count -gt 0) { 'yes' } else { 'no' })"
    Write-Info "Has overwritten files: $(if ($overwrittenFiles.Count -gt 0) { 'yes' } else { 'no' })"

    if ($newFiles.Count -gt 0) {
        Write-Host '  New files:'
        $newFiles | ForEach-Object { Write-Host "    $($_.RelativePath)" }
    }

    if ($overwrittenFiles.Count -gt 0) {
        Write-Host '  Overwritten files:'
        $overwrittenFiles | ForEach-Object { Write-Host "    $($_.RelativePath)" }
    }

    Write-Step 'Suggested next git commands'
    Write-Host ('  git -C "{0}" status' -f $resolvedSkillHubPath)
    Write-Host ('  git -C "{0}" add skills/{1}' -f $resolvedSkillHubPath, $trimmedSkillName)
    Write-Host ('  git -C "{0}" diff --cached' -f $resolvedSkillHubPath)
    Write-Host ('  git -C "{0}" commit -m ''sync skill: {1} from project''' -f $resolvedSkillHubPath, $trimmedSkillName)

    if ($DryRun) {
        Write-Success "DryRun completed for skill: $trimmedSkillName"
    }
    else {
        Write-Success "Skill sync completed for skill: $trimmedSkillName"
    }
}
catch {
    Write-Host ""
    Write-Error "[FAILED] $($_.Exception.Message)"
    exit 1
}

