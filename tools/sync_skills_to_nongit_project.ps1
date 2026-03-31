<#
用途：
- 将 skill hub 中的全部或单个 skill 同步到一个非 Git 项目的 `.codex\skills` 目录下。

适合什么时候用：
- 给业务项目下发最新 skills
- 目标项目不是独立 Git 仓库，或你只想做文件级同步

最短调用示例：
- `.\tools\sync_skills_to_nongit_project.ps1 -ProjectPath 'D:\my-project'`
- `.\tools\sync_skills_to_nongit_project.ps1 -ProjectPath 'D:\my-project' -SkillName 'project-takeover' -DryRun`
- `\.\tools\sync_skills_to_nongit_project.ps1 -ProjectPath 'D:\my-project' -Targets codex`

注意：
- 不传 `-SkillName` 时会同步全部 skills
- 不传 `-Targets` 时默认同步 `codex + agents + github`
- `.codex\skills` 仍作为项目消费侧兼容入口保留，不随 hub 改名而调整
- 会在目标项目的 `.codex\skills` 下写入版本说明文件
- 使用 `robocopy /MIR`，建议先用 `-DryRun` 预览同步结果
#>
[CmdletBinding()]
param(
    [string]$SkillHubPath,

    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,

    [string]$SkillName,
    [string[]]$Targets = @('codex', 'agents', 'github'),
    [string]$VersionFileName = '_skillset_version.txt',
    [string]$HubVersionFile = 'VERSION',
    [string]$HubName = 'ai-skill-hub',
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$IsDryRun = [bool]$DryRun

if ([string]::IsNullOrWhiteSpace($SkillHubPath)) {
    $scriptFilePath = if (-not [string]::IsNullOrWhiteSpace($PSCommandPath)) {
        $PSCommandPath
    }
    elseif ($MyInvocation.MyCommand.Path) {
        $MyInvocation.MyCommand.Path
    }
    else {
        $null
    }

    if ([string]::IsNullOrWhiteSpace($scriptFilePath)) {
        throw 'SkillHubPath was not provided and the script location could not be determined. Please pass -SkillHubPath explicitly.'
    }

    $scriptDirectory = Split-Path -Path $scriptFilePath -Parent
    $SkillHubPath = (Resolve-Path -LiteralPath (Join-Path $scriptDirectory '..')).ProviderPath
}

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

function Write-WarningMessage {
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

function Write-Plan {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    Write-Host "[PLAN] $Message" -ForegroundColor Magenta
}

function Confirm-DirectoryExists {
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

function Get-NormalizedTargets {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$RequestedTargets
    )

    $normalizedTargets = New-Object 'System.Collections.Generic.List[string]'
    $allowedTargets = @('codex', 'agents', 'github')

    foreach ($requestedTarget in $RequestedTargets) {
        if ($null -eq $requestedTarget) {
            continue
        }

        foreach ($targetPart in ($requestedTarget -split ',')) {
            $normalizedTarget = $targetPart.Trim().ToLowerInvariant()
            if ([string]::IsNullOrWhiteSpace($normalizedTarget)) {
                continue
            }

            if ($allowedTargets -notcontains $normalizedTarget) {
                throw "Unsupported target '$normalizedTarget'. Allowed targets: codex, agents, github."
            }

            if (-not $normalizedTargets.Contains($normalizedTarget)) {
                $normalizedTargets.Add($normalizedTarget)
            }
        }
    }

    if ($normalizedTargets.Count -eq 0) {
        throw 'Targets must contain at least one of: codex, agents, github.'
    }

    return @($normalizedTargets)
}

function Initialize-Directory {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (Test-Path -LiteralPath $Path -PathType Container) {
        return
    }

    if ($IsDryRun) {
        Write-Plan "Create directory: $Path"
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

function Get-SyncableEntries {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SkillsRoot
    )

    return Get-ChildItem -LiteralPath $SkillsRoot -Directory | Where-Object {
        $_.Name -eq '_protocol' -or (Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') -PathType Leaf)
    } | Sort-Object Name
}

function Get-SkillEntries {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SkillsRoot
    )

    return Get-ChildItem -LiteralPath $SkillsRoot -Directory | Where-Object {
        Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') -PathType Leaf
    } | Sort-Object Name
}

function Normalize-FrontmatterValue {
    param(
        [AllowEmptyString()]
        [string]$Value
    )

    $trimmedValue = $Value.Trim()
    if ($trimmedValue.Length -ge 2) {
        $firstCharacter = $trimmedValue[0]
        $lastCharacter = $trimmedValue[$trimmedValue.Length - 1]
        if (($firstCharacter -eq '"' -and $lastCharacter -eq '"') -or ($firstCharacter -eq "'" -and $lastCharacter -eq "'")) {
            return $trimmedValue.Substring(1, $trimmedValue.Length - 2)
        }
    }

    return $trimmedValue
}

function Get-SkillMetadata {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SkillFilePath
    )

    if (-not (Test-Path -LiteralPath $SkillFilePath -PathType Leaf)) {
        throw "Skill file not found: $SkillFilePath"
    }

    $content = Get-Content -LiteralPath $SkillFilePath -Raw
    $frontmatterMatch = [regex]::Match($content, '(?s)^---\r?\n(.*?)\r?\n---\r?\n')
    if (-not $frontmatterMatch.Success) {
        throw "Missing or invalid frontmatter in skill file: $SkillFilePath"
    }

    $name = ''
    $description = ''
    $triggers = New-Object 'System.Collections.Generic.List[string]'
    $sideEffects = New-Object 'System.Collections.Generic.List[string]'
    $inMetadata = $false
    $activeListName = $null

    foreach ($rawLine in ($frontmatterMatch.Groups[1].Value -split "`r?`n")) {
        if ([string]::IsNullOrWhiteSpace($rawLine)) {
            continue
        }

        $trimmedLine = $rawLine.Trim()
        $indentation = $rawLine.Length - $rawLine.TrimStart().Length

        if ($indentation -eq 0) {
            if ($trimmedLine -eq 'metadata:') {
                $inMetadata = $true
                $activeListName = $null
                continue
            }

            $inMetadata = $false
            $activeListName = $null

            if ($trimmedLine -match '^name:\s*(.+)$') {
                $name = Normalize-FrontmatterValue -Value $matches[1]
                continue
            }

            if ($trimmedLine -match '^description:\s*(.+)$') {
                $description = Normalize-FrontmatterValue -Value $matches[1]
            }

            continue
        }

        if (-not $inMetadata) {
            continue
        }

        if ($trimmedLine -match '^([A-Za-z0-9_-]+):$') {
            $activeListName = $matches[1]
            continue
        }

        if ($trimmedLine -match '^-\s+(.+)$') {
            $listValue = Normalize-FrontmatterValue -Value $matches[1]
            switch ($activeListName) {
                'triggers' {
                    $triggers.Add($listValue)
                }
                'side_effects' {
                    $sideEffects.Add($listValue)
                }
            }
        }
    }

    if ([string]::IsNullOrWhiteSpace($name)) {
        $name = Split-Path -Path (Split-Path -Path $SkillFilePath -Parent) -Leaf
    }

    return [pscustomobject]@{
        Name = $name
        Description = $description
        Triggers = @($triggers)
        SideEffects = @($sideEffects)
    }
}

function ConvertTo-YamlDoubleQuoted {
    param(
        [AllowEmptyString()]
        [string]$Value
    )

    $escapedValue = $Value.Replace('\', '\\').Replace('"', '\"').Replace("`r", ' ').Replace("`n", ' ')
    return '"' + $escapedValue + '"'
}

function Write-GeneratedFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [string]$Content
    )

    $parentPath = Split-Path -Path $Path -Parent
    if (-not [string]::IsNullOrWhiteSpace($parentPath)) {
        Initialize-Directory -Path $parentPath
    }

    if ($IsDryRun) {
        Write-Plan "Write file: $Path"
        return
    }

    Set-Content -LiteralPath $Path -Value $Content -Encoding utf8
    Write-Info "Wrote generated file: $Path"
}

function Remove-GeneratedEntry {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if ($IsDryRun) {
        Write-Plan "Remove generated adapter entry: $Path"
        return
    }

    Remove-Item -LiteralPath $Path -Recurse -Force
    Write-Info "Removed generated adapter entry: $Path"
}

function Test-ProjectGeneratedAgentsWrapper {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $false
    }

    $content = Get-Content -LiteralPath $Path -Raw
    return $content.Contains('canonical_path: ../../../.codex/skills/') -and $content.Contains('Read the project-local skill before execution.')
}

function Test-ProjectGeneratedAgentsSummary {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $false
    }

    $content = Get-Content -LiteralPath $Path -Raw
    return $content.Contains('- path: `.codex/skills/') -and $content.Contains('Read the project-local SKILL.md before execution.')
}

function Test-ProjectGeneratedGithubEntry {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $false
    }

    $content = Get-Content -LiteralPath $Path -Raw
    return $content.Contains('Canonical skill path: `../../.codex/skills/') -and $content.Contains('This compatibility entry is generated from the project-local .codex skill copy.')
}

function Remove-StaleProjectAgentsEntries {
    param(
        [Parameter(Mandatory = $true)]
        [string]$TargetRoot,

        [Parameter(Mandatory = $true)]
        [string[]]$AllowedSkillNames
    )

    if (-not (Test-Path -LiteralPath $TargetRoot -PathType Container)) {
        return
    }

    $allowedFileNames = @($AllowedSkillNames | ForEach-Object { "$_.md" }) + @('README.md', 'skills_index.md')
    foreach ($entry in (Get-ChildItem -LiteralPath $TargetRoot -Force)) {
        if ($entry.PSIsContainer) {
            if ($AllowedSkillNames -contains $entry.Name) {
                continue
            }

            $wrapperPath = Join-Path $entry.FullName 'SKILL.md'
            if (Test-ProjectGeneratedAgentsWrapper -Path $wrapperPath) {
                Remove-GeneratedEntry -Path $entry.FullName
            }

            continue
        }

        if ($allowedFileNames -contains $entry.Name -or $entry.Extension -ne '.md') {
            continue
        }

        if (Test-ProjectGeneratedAgentsSummary -Path $entry.FullName) {
            Remove-GeneratedEntry -Path $entry.FullName
        }
    }
}

function Remove-StaleProjectGithubEntries {
    param(
        [Parameter(Mandatory = $true)]
        [string]$TargetRoot,

        [Parameter(Mandatory = $true)]
        [string[]]$AllowedSkillNames
    )

    if (-not (Test-Path -LiteralPath $TargetRoot -PathType Container)) {
        return
    }

    $allowedFileNames = @($AllowedSkillNames | ForEach-Object { "$_.md" })
    foreach ($entry in (Get-ChildItem -LiteralPath $TargetRoot -File -Force)) {
        if ($allowedFileNames -contains $entry.Name -or $entry.Extension -ne '.md') {
            continue
        }

        if (Test-ProjectGeneratedGithubEntry -Path $entry.FullName) {
            Remove-GeneratedEntry -Path $entry.FullName
        }
    }
}

function Emit-ProjectAgentsAdapter {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPathValue,

        [Parameter(Mandatory = $true)]
        [object]$SkillMetadata
    )

    $agentsRoot = Join-Path $ProjectPathValue '.agents\skills'
    $wrapperDirectory = Join-Path $agentsRoot $SkillMetadata.Name
    $wrapperPath = Join-Path $wrapperDirectory 'SKILL.md'
    $summaryPath = Join-Path $agentsRoot ("{0}.md" -f $SkillMetadata.Name)
    $projectLocalSkillPath = ".codex/skills/$($SkillMetadata.Name)"
    $relativeCanonicalPath = "../../../$projectLocalSkillPath"
    $triggerValues = @($SkillMetadata.Triggers)
    $sideEffectValues = @($SkillMetadata.SideEffects)
    $triggerLines = @($triggerValues | ForEach-Object { "    - $_" })
    $sideEffectLines = @($sideEffectValues | ForEach-Object { "    - $_" })
    $summaryTriggers = if ($triggerValues.Count -gt 0) {
        $triggerValues -join ', '
    }
    else {
        ''
    }

    $wrapperContent = @(
        '---'
        "name: $($SkillMetadata.Name)"
        "description: $(ConvertTo-YamlDoubleQuoted -Value $SkillMetadata.Description)"
        'metadata:'
        '  triggers:'
        $triggerLines
        '  side_effects:'
        $sideEffectLines
        "  canonical_path: $relativeCanonicalPath"
        '  adapter_type: thin-wrapper'
        '---'
        ''
        "# $($SkillMetadata.Name)"
        ''
        ('- Project-local skill directory: `{0}`' -f $relativeCanonicalPath)
        ('- Project-local skill definition: `{0}/SKILL.md`' -f $relativeCanonicalPath)
        '- This wrapper is generated for project-local discovery only.'
        '- Read the project-local skill before execution.'
        ''
    ) -join [Environment]::NewLine

    $summaryContent = @(
        "# $($SkillMetadata.Name)"
        ''
        ('- name: `{0}`' -f $SkillMetadata.Name)
        ('- description: `{0}`' -f $SkillMetadata.Description)
        ('- triggers: `{0}`' -f $summaryTriggers)
        ('- path: `{0}`' -f $projectLocalSkillPath)
        ''
        'Read the project-local SKILL.md before execution.'
        ''
    ) -join [Environment]::NewLine

    Write-GeneratedFile -Path $wrapperPath -Content $wrapperContent
    Write-GeneratedFile -Path $summaryPath -Content $summaryContent
}

function Emit-ProjectGithubAdapter {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPathValue,

        [Parameter(Mandatory = $true)]
        [object]$SkillMetadata
    )

    $githubSkillsRoot = Join-Path $ProjectPathValue '.github\skills'
    $entryPath = Join-Path $githubSkillsRoot ("{0}.md" -f $SkillMetadata.Name)
    $relativeCanonicalPath = "../../.codex/skills/$($SkillMetadata.Name)"
    $entryContent = @(
        '---'
        "name: $($SkillMetadata.Name)"
        "description: $(ConvertTo-YamlDoubleQuoted -Value $SkillMetadata.Description)"
        '---'
        ''
        "# $($SkillMetadata.Name)"
        ''
        ('- Canonical skill path: `{0}`' -f $relativeCanonicalPath)
        ('- Canonical skill definition: `{0}/SKILL.md`' -f $relativeCanonicalPath)
        '- This compatibility entry is generated from the project-local .codex skill copy.'
        '- Read the project-local SKILL.md before execution.'
        ''
    ) -join [Environment]::NewLine

    Write-GeneratedFile -Path $entryPath -Content $entryContent
}

function Remove-StaleTargetEntries {
    param(
        [Parameter(Mandatory = $true)]
        [string]$TargetRoot,

        [Parameter(Mandatory = $true)]
        [string[]]$AllowedNames,

        [Parameter(Mandatory = $true)]
        [string]$PreserveFileName
    )

    if (-not (Test-Path -LiteralPath $TargetRoot -PathType Container)) {
        return
    }

    $preservedNames = @($AllowedNames + $PreserveFileName)
    foreach ($entry in (Get-ChildItem -LiteralPath $TargetRoot -Force)) {
        if ($preservedNames -contains $entry.Name) {
            continue
        }

        if ($IsDryRun) {
            Write-Plan "Remove stale entry: $($entry.FullName)"
        }
        else {
            Remove-Item -LiteralPath $entry.FullName -Recurse -Force
            Write-Info "Removed stale entry: $($entry.FullName)"
        }
    }
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

    if ($IsDryRun) {
        Write-Plan ("Sync directory tree: {0} -> {1}" -f $SourcePath, $TargetPath)
        Write-Plan ("Skip robocopy execution during DryRun: robocopy {0}" -f ($robocopyArguments -join ' '))
        return 0
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

function Get-RecursiveFileCount {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Paths
    )

    $total = 0
    foreach ($path in $Paths) {
        if (-not (Test-Path -LiteralPath $path)) {
            continue
        }

        $total += @(Get-ChildItem -LiteralPath $path -Recurse -File -Force).Count
    }

    return $total
}

function Write-DryRunPlanSummary {
    param(
        [Parameter(Mandatory = $true)]
        [int]$SkillCount,

        [Parameter(Mandatory = $true)]
        [string]$CanonicalTargetPath,

        [Parameter(Mandatory = $true)]
        [string]$AgentsTargetPath,

        [Parameter(Mandatory = $true)]
        [string]$GithubTargetPath,

        [Parameter(Mandatory = $true)]
        [int]$CanonicalFileCount,

        [Parameter(Mandatory = $true)]
        [int]$AdapterFileCount,

        [Parameter(Mandatory = $true)]
        [string[]]$SelectedTargets,

        [Parameter(Mandatory = $true)]
        [string]$Scope
    )

    $selectedTargetText = $SelectedTargets -join ', '
    $versionFileWrites = if ($SelectedTargets -contains 'codex') { 1 } else { 0 }

    Write-Step 'DryRun plan summary'
    Write-Plan "Scope: $Scope"
    Write-Plan "Selected targets: $selectedTargetText"
    Write-Plan "Skill count: $SkillCount"
    if ($SelectedTargets -contains 'codex') {
        Write-Plan "Canonical target: $CanonicalTargetPath"
    }
    if ($SelectedTargets -contains 'agents' -or $SelectedTargets -contains 'github') {
        $adapterTargets = @()
        if ($SelectedTargets -contains 'agents') {
            $adapterTargets += $AgentsTargetPath
        }
        if ($SelectedTargets -contains 'github') {
            $adapterTargets += $GithubTargetPath
        }
        Write-Plan ("Adapter targets: {0}" -f ($adapterTargets -join ' ; '))
    }
    Write-Plan "Estimated canonical files to copy or update: $CanonicalFileCount"
    Write-Plan "Estimated adapter files to write or update: $AdapterFileCount"
    Write-Plan ("Estimated total file writes: {0}" -f ($CanonicalFileCount + $AdapterFileCount + $versionFileWrites))
    Write-Plan 'DryRun will not create directories, write files, remove entries, or execute robocopy.'
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

$selectedTargets = @(Get-NormalizedTargets -RequestedTargets $Targets)
$syncCodex = $selectedTargets -contains 'codex'
$syncAgents = $selectedTargets -contains 'agents'
$syncGithub = $selectedTargets -contains 'github'

try {
    Write-Step 'Checking required commands'
    if (-not (Get-Command robocopy -ErrorAction SilentlyContinue)) {
        throw 'robocopy was not found in PATH.'
    }

    Write-Step 'Validating paths'
    Confirm-DirectoryExists -Path $SkillHubPath -Description 'Skill hub path'
    Confirm-DirectoryExists -Path $ProjectPath -Description 'Project path'

    $resolvedSkillHubPath = (Resolve-Path -LiteralPath $SkillHubPath).ProviderPath
    $resolvedProjectPath = (Resolve-Path -LiteralPath $ProjectPath).ProviderPath
    $sourceSkillsRoot = Join-Path $resolvedSkillHubPath 'skills'
    Confirm-DirectoryExists -Path $sourceSkillsRoot -Description 'Skill hub skills directory'

    $hubVersionPath = Join-Path $resolvedSkillHubPath $HubVersionFile
    $skillsetVersion = Get-HubVersion -FilePath $hubVersionPath

    $projectCodexPath = Join-Path $resolvedProjectPath '.codex'
    $targetSkillsRoot = Join-Path $projectCodexPath 'skills'
    $projectAgentsRoot = Join-Path $resolvedProjectPath '.agents\skills'
    $projectGithubRoot = Join-Path $resolvedProjectPath '.github\skills'

    Write-Info "Skill hub path: $resolvedSkillHubPath"
    Write-Info "Project path: $resolvedProjectPath"
    Write-Info "Target skills path: $targetSkillsRoot"
    Write-Info "Skillset version: $skillsetVersion"
    Write-Info "Selected targets: $($selectedTargets -join ', ')"

    if ([string]::IsNullOrWhiteSpace($SkillName)) {
        $syncedScope = 'all'
        $sourcePath = $sourceSkillsRoot
        $targetPath = $targetSkillsRoot
        $syncableEntries = @(Get-SyncableEntries -SkillsRoot $sourceSkillsRoot)
        if ($syncableEntries.Count -eq 0) {
            throw "No syncable skill directories found under: $sourceSkillsRoot"
        }

        $allowedEntryNames = @($syncableEntries | ForEach-Object { $_.Name })
        if ($syncCodex) {
            Write-Step 'Cleaning stale target entries'
            Remove-StaleTargetEntries -TargetRoot $targetSkillsRoot -AllowedNames $allowedEntryNames -PreserveFileName $VersionFileName
        }

        $plannedSkillEntries = @(Get-SkillEntries -SkillsRoot $sourceSkillsRoot)
        $estimatedCanonicalFileCount = if ($syncCodex) {
            Get-RecursiveFileCount -Paths @($syncableEntries | ForEach-Object { $_.FullName })
        }
        else {
            0
        }

        if ($syncCodex) {
            Write-Step 'Syncing all canonical skill entries'
            Write-Info "Entries: $($allowedEntryNames -join ', ')"
        }
    }
    else {
        $syncedScope = $SkillName.Trim()
        $sourcePath = Join-Path $sourceSkillsRoot $syncedScope
        Confirm-DirectoryExists -Path $sourcePath -Description 'Source skill'
        $targetPath = Join-Path $targetSkillsRoot $syncedScope
        $plannedSkillEntries = @()
        if (Test-Path -LiteralPath (Join-Path $sourcePath 'SKILL.md') -PathType Leaf) {
            $plannedSkillEntries = @([pscustomobject]@{
                Name     = $syncedScope
                FullName = $sourcePath
            })
        }
        $estimatedCanonicalFileCount = if ($syncCodex) {
            Get-RecursiveFileCount -Paths @($sourcePath)
        }
        else {
            0
        }

        if ($syncCodex) {
            Write-Step "Syncing single skill: $syncedScope"
        }
    }

    if ($IsDryRun) {
        $adapterFilesPerSkill = 0
        if ($syncAgents) {
            $adapterFilesPerSkill += 2
        }
        if ($syncGithub) {
            $adapterFilesPerSkill += 1
        }
        $estimatedAdapterFileCount = $plannedSkillEntries.Count * $adapterFilesPerSkill
        Write-DryRunPlanSummary `
            -SkillCount $plannedSkillEntries.Count `
            -CanonicalTargetPath $targetSkillsRoot `
            -AgentsTargetPath $projectAgentsRoot `
            -GithubTargetPath $projectGithubRoot `
            -CanonicalFileCount $estimatedCanonicalFileCount `
            -AdapterFileCount $estimatedAdapterFileCount `
            -SelectedTargets $selectedTargets `
            -Scope $syncedScope
    }

    if ($syncCodex) {
        Write-Step 'Preparing target directories'
        Initialize-Directory -Path $projectCodexPath
        Initialize-Directory -Path $targetSkillsRoot

        if (-not [string]::IsNullOrWhiteSpace($SkillName)) {
            Initialize-Directory -Path $targetPath
        }
    }

    if ($syncCodex -and [string]::IsNullOrWhiteSpace($SkillName)) {
        $robocopyExitCodes = @()
        foreach ($entry in $syncableEntries) {
            $entryTargetPath = Join-Path $targetSkillsRoot $entry.Name
            Initialize-Directory -Path $entryTargetPath
            Write-Info "Syncing entry: $($entry.Name)"
            $robocopyExitCodes += Invoke-RobocopySync -SourcePath $entry.FullName -TargetPath $entryTargetPath
        }
        $robocopyExitCode = @($robocopyExitCodes | Measure-Object -Maximum).Maximum
    }
    elseif ($syncCodex) {
        $robocopyExitCode = Invoke-RobocopySync -SourcePath $sourcePath -TargetPath $targetPath
    }
    else {
        $robocopyExitCode = 0
        Write-Info 'Skipped canonical sync because Targets excludes codex.'
    }

    Write-Info "robocopy exit code: $robocopyExitCode"

    $projectSkillEntries = @(
        if ($IsDryRun -or -not $syncCodex) {
            $plannedSkillEntries
        }
        else {
            Get-SkillEntries -SkillsRoot $targetSkillsRoot
        }
    )

    if ($syncAgents -or $syncGithub) {
        if ([string]::IsNullOrWhiteSpace($SkillName)) {
            $projectSkillNames = @($projectSkillEntries | ForEach-Object { $_.Name })
            Write-Step 'Cleaning stale project-local adapter entries'
            if ($syncAgents) {
                Remove-StaleProjectAgentsEntries -TargetRoot $projectAgentsRoot -AllowedSkillNames $projectSkillNames
            }
            if ($syncGithub) {
                Remove-StaleProjectGithubEntries -TargetRoot $projectGithubRoot -AllowedSkillNames $projectSkillNames
            }
        }

        if ($projectSkillEntries.Count -gt 0) {
            Write-Step 'Emitting project-local adapter entries'
            foreach ($entry in $projectSkillEntries) {
                Write-Info "Generating project-local adapters for skill: $($entry.Name)"
                $skillMetadata = Get-SkillMetadata -SkillFilePath (Join-Path $entry.FullName 'SKILL.md')
                if ($syncAgents) {
                    Emit-ProjectAgentsAdapter -ProjectPathValue $resolvedProjectPath -SkillMetadata $skillMetadata
                }
                if ($syncGithub) {
                    Emit-ProjectGithubAdapter -ProjectPathValue $resolvedProjectPath -SkillMetadata $skillMetadata
                }
            }
        }
        else {
            Write-Info "Skipped project-local adapter emit for non-skill entry: $syncedScope"
        }
    }
    else {
        Write-Info 'Skipped adapter emit because Targets excludes agents and github.'
    }

    if ($syncCodex) {
        $versionFilePath = Join-Path $targetSkillsRoot $VersionFileName
        $note = if ($DryRun) {
            'DryRun preview only; version file was not written. No project-side git command was executed.'
        }
        else {
            'Synced by sync_skills_to_nongit_project.ps1. No project-side git command was executed.'
        }

        $versionFileParameters = @{
            SourceHub        = $HubName
            SourcePath       = $sourcePath
            SkillsetVersion  = $skillsetVersion
            SyncedScope      = $syncedScope
            RobocopyExitCode = $robocopyExitCode
            ProjectPathValue = $resolvedProjectPath
            Note             = $note
        }
        $versionFileContent = New-VersionFileContent @versionFileParameters

        Write-Step 'Writing sync metadata'
        if ($IsDryRun) {
            Write-Plan "Write version file: $versionFilePath"
            Write-Host $versionFileContent
        }
        else {
            Set-Content -LiteralPath $versionFilePath -Value $versionFileContent -Encoding utf8
            Write-Info "Version file written: $versionFilePath"
        }
    }
    else {
        Write-Info 'Skipped sync metadata write because Targets excludes codex.'
    }

    Write-Success "Skill sync completed for scope: $syncedScope"
}
catch {
    Write-Host ""
    Write-Error "[FAILED] $($_.Exception.Message)"
    exit 1
}
