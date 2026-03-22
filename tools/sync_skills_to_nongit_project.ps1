<#
用途：
- 将 skill hub 中的全部或单个 skill 同步到一个非 Git 项目的 `.codex\skills` 目录下。

适合什么时候用：
- 给业务项目下发最新 skills
- 目标项目不是独立 Git 仓库，或你只想做文件级同步

最短调用示例：
- `.\tools\sync_skills_to_nongit_project.ps1 -SkillHubPath 'D:\dev\codex-skill-hub' -ProjectPath 'D:\my-project'`
- `.\tools\sync_skills_to_nongit_project.ps1 -SkillHubPath 'D:\dev\codex-skill-hub' -ProjectPath 'D:\my-project' -SkillName 'project-takeover' -DryRun`

注意：
- 不传 `-SkillName` 时会同步全部 skills
- 会在目标项目的 `.codex\skills` 下写入版本说明文件
- 使用 `robocopy /MIR`，建议先用 `-DryRun` 预览同步结果
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$SkillHubPath,

    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,

    [string]$SkillName,
    [string]$VersionFileName = '_skillset_version.txt',
    [string]$HubVersionFile = 'VERSION',
    [string]$HubName = 'CODEX-SKILL-HUB',
    [switch]$DryRun
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

function Ensure-Directory {
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

function Get-HubVersion {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath
    )

    if (-not (Test-Path -LiteralPath $FilePath -PathType Leaf)) {
        throw "Hub version file not found: $FilePath"
    }

    $version = (Get-Content -LiteralPath $FilePath -Raw).Trim()
    if ([string]::IsNullOrWhiteSpace($version)) {
        throw "Hub version file is empty: $FilePath"
    }

    return $version
}

function Invoke-RobocopySync {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SourcePath,

        [Parameter(Mandatory = $true)]
        [string]$TargetPath
    )

    $robocopyArguments = @(
        $SourcePath,
        $TargetPath,
        '/MIR',
        '/R:2',
        '/W:1',
        '/XD', '__pycache__', '.git', '.tmp', '.pytest_cache', '.mypy_cache',
        '/XF', '*.pyc', '*.pyo'
    )

    if ($DryRun) {
        $robocopyArguments += '/L'
    }

    Write-Info ("Robocopy command: robocopy {0}" -f ($robocopyArguments -join ' '))
    $robocopyOutput = & robocopy @robocopyArguments
    $exitCode = $LASTEXITCODE

    if ($null -ne $robocopyOutput) {
        $robocopyOutput | ForEach-Object { Write-Host $_ }
    }

    if ($exitCode -ge 8) {
        throw "robocopy failed with exit code $exitCode."
    }

    return [int]$exitCode
}

function New-VersionFileContent {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SourceHub,

        [Parameter(Mandatory = $true)]
        [string]$SourcePath,

        [Parameter(Mandatory = $true)]
        [string]$SkillsetVersion,

        [Parameter(Mandatory = $true)]
        [string]$SyncedScope,

        [Parameter(Mandatory = $true)]
        [int]$RobocopyExitCode,

        [Parameter(Mandatory = $true)]
        [string]$ProjectPathValue,

        [Parameter(Mandatory = $true)]
        [string]$Note
    )

    $syncedAt = (Get-Date).ToString('yyyy-MM-ddTHH:mm:ssK')

    return @(
        "source_hub=$SourceHub"
        "source_path=$SourcePath"
        "skillset_version=$SkillsetVersion"
        "synced_scope=$SyncedScope"
        "synced_at=$syncedAt"
        "robocopy_exit_code=$RobocopyExitCode"
        "project_path=$ProjectPathValue"
        "note=$Note"
    ) -join [Environment]::NewLine
}

try {
    Write-Step 'Checking required commands'
    if (-not (Get-Command robocopy -ErrorAction SilentlyContinue)) {
        throw 'robocopy was not found in PATH.'
    }

    Write-Step 'Validating paths'
    Assert-DirectoryExists -Path $SkillHubPath -Description 'Skill hub path'
    Assert-DirectoryExists -Path $ProjectPath -Description 'Project path'

    $resolvedSkillHubPath = (Resolve-Path -LiteralPath $SkillHubPath).ProviderPath
    $resolvedProjectPath = (Resolve-Path -LiteralPath $ProjectPath).ProviderPath
    $sourceSkillsRoot = Join-Path $resolvedSkillHubPath 'skills'
    Assert-DirectoryExists -Path $sourceSkillsRoot -Description 'Skill hub skills directory'

    $hubVersionPath = Join-Path $resolvedSkillHubPath $HubVersionFile
    $skillsetVersion = Get-HubVersion -FilePath $hubVersionPath

    $projectCodexPath = Join-Path $resolvedProjectPath '.codex'
    $targetSkillsRoot = Join-Path $projectCodexPath 'skills'

    Write-Info "Skill hub path: $resolvedSkillHubPath"
    Write-Info "Project path: $resolvedProjectPath"
    Write-Info "Target skills path: $targetSkillsRoot"
    Write-Info "Skillset version: $skillsetVersion"

    Write-Step 'Preparing target directories'
    Ensure-Directory -Path $projectCodexPath
    Ensure-Directory -Path $targetSkillsRoot

    if ([string]::IsNullOrWhiteSpace($SkillName)) {
        $syncedScope = 'all'
        $sourcePath = $sourceSkillsRoot
        $targetPath = $targetSkillsRoot
        Write-Step 'Syncing all skills'
    }
    else {
        $syncedScope = $SkillName.Trim()
        $sourcePath = Join-Path $sourceSkillsRoot $syncedScope
        Assert-DirectoryExists -Path $sourcePath -Description 'Source skill'
        $targetPath = Join-Path $targetSkillsRoot $syncedScope
        Ensure-Directory -Path $targetPath
        Write-Step "Syncing single skill: $syncedScope"
    }

    $robocopyExitCode = Invoke-RobocopySync -SourcePath $sourcePath -TargetPath $targetPath
    Write-Info "robocopy exit code: $robocopyExitCode"

    $versionFilePath = Join-Path $targetSkillsRoot $VersionFileName
    $note = if ($DryRun) {
        'DryRun preview only; version file was not written. No project-side git command was executed.'
    }
    else {
        'Synced by sync_skills_to_nongit_project.ps1. No project-side git command was executed.'
    }

    $versionFileContent = New-VersionFileContent `
        -SourceHub $HubName `
        -SourcePath $sourcePath `
        -SkillsetVersion $skillsetVersion `
        -SyncedScope $syncedScope `
        -RobocopyExitCode $robocopyExitCode `
        -ProjectPathValue $resolvedProjectPath `
        -Note $note

    Write-Step 'Writing sync metadata'
    if ($DryRun) {
        Write-WarnMessage "DryRun: would write version file to $versionFilePath"
        Write-Host $versionFileContent
    }
    else {
        Set-Content -LiteralPath $versionFilePath -Value $versionFileContent -Encoding utf8
        Write-Info "Version file written: $versionFilePath"
    }

    Write-Success "Skill sync completed for scope: $syncedScope"
}
catch {
    Write-Host ""
    Write-Error "[FAILED] $($_.Exception.Message)"
    exit 1
}
