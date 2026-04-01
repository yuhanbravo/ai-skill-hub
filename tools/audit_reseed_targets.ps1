<#
用途：
- 只读审计一组项目的 skill system 状态，判断是否适合执行 clean re-seed。

定位：
- 这是 rollout 前的预检查工具，不会执行真实同步，不会修改项目内容。

最短调用示例：
- `.\tools\audit_reseed_targets.ps1 -RootPath 'D:\BaiduSyncdisk\Python_Lib'`
- `.\tools\audit_reseed_targets.ps1 -ProjectPaths 'D:\ProjectA','D:\ProjectB' -Format json -OutputPath '.\reports'`
- `.\tools\audit_reseed_targets.ps1 -ProjectsFile '.\projects.txt' -Format csv -OutputPath '.\reports\reseed_audit.csv'`
#>
[CmdletBinding(DefaultParameterSetName = 'RootScan')]
param(
    [Parameter(Mandatory = $true, ParameterSetName = 'RootScan')]
    [string]$RootPath,

    [Parameter(Mandatory = $true, ParameterSetName = 'ExplicitList', ValueFromRemainingArguments = $true)]
    [string[]]$ProjectPaths,

    [Parameter(Mandatory = $true, ParameterSetName = 'ProjectsFile')]
    [string]$ProjectsFile,

    [string]$OutputPath,

    [ValidateSet('table', 'csv', 'json', 'md')]
    [string]$Format = 'table',

    [ValidateRange(1, 10)]
    [int]$RecurseDepth = 1,

    [switch]$IncludeHidden,
    [switch]$VerboseReport
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:BackupDirectoryNames = @(
    '_backup_before_reset',
    'backup',
    'backups',
    'archive',
    'snapshot',
    'old_skills',
    'legacy_skills'
)

function Get-HubRepositorySignals {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath
    )

    $signals = New-Object 'System.Collections.Generic.List[string]'
    $signalChecks = @(
        @{ name = 'skills_root'; path = 'skills'; type = 'Container' }
        @{ name = 'sync_script'; path = 'tools\sync_skills_to_nongit_project.ps1'; type = 'Leaf' }
        @{ name = 'version_file'; path = 'VERSION'; type = 'Leaf' }
        @{ name = 'readme'; path = 'README.md'; type = 'Leaf' }
        @{ name = 'status_doc'; path = 'docs\status\skill-hub-status.md'; type = 'Leaf' }
    )

    foreach ($signalCheck in $signalChecks) {
        $candidatePath = Join-Path $ProjectPath $signalCheck.path
        if (Test-Path -LiteralPath $candidatePath -PathType $signalCheck.type) {
            $signals.Add($signalCheck.name)
        }
    }

    return @($signals)
}

function Test-IsHubRepository {
    param(
        [AllowEmptyCollection()]
        [string[]]$Signals = @()
    )

    $hasSkillsRoot = $Signals -contains 'skills_root'
    $hasSyncScript = $Signals -contains 'sync_script'
    return $hasSkillsRoot -and $hasSyncScript -and $Signals.Count -ge 3
}

function Test-VisibleDirectory {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo]$Directory,

        [switch]$AllowHidden
    )

    if ($AllowHidden) {
        return $true
    }

    if ($Directory.Name.StartsWith('.')) {
        return $false
    }

    return -not [bool]($Directory.Attributes -band [System.IO.FileAttributes]::Hidden)
}

function Get-RelativeDepth {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Root,

        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    $normalizedRoot = $Root.TrimEnd('\', '/')
    $normalizedPath = $Path.TrimEnd('\', '/')

    if ($normalizedPath.Length -le $normalizedRoot.Length) {
        return 0
    }

    $relativePath = $normalizedPath.Substring($normalizedRoot.Length).TrimStart('\', '/')
    if ([string]::IsNullOrWhiteSpace($relativePath)) {
        return 0
    }

    return ($relativePath -split '[\\/]').Count
}

function Get-DiscoveredProjectPaths {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ScanRoot,

        [int]$Depth,
        [switch]$AllowHidden
    )

    if (-not (Test-Path -LiteralPath $ScanRoot -PathType Container)) {
        throw "RootPath not found: $ScanRoot"
    }

    $resolvedRoot = (Resolve-Path -LiteralPath $ScanRoot).ProviderPath
    $candidates = New-Object 'System.Collections.Generic.List[string]'
    $pending = New-Object 'System.Collections.Generic.Queue[System.IO.DirectoryInfo]'
    $pending.Enqueue((Get-Item -LiteralPath $resolvedRoot))

    while ($pending.Count -gt 0) {
        $current = $pending.Dequeue()
        $currentDepth = Get-RelativeDepth -Root $resolvedRoot -Path $current.FullName
        if ($currentDepth -ge $Depth) {
            continue
        }

        $children = @(Get-ChildItem -LiteralPath $current.FullName -Directory -Force -ErrorAction Stop | Where-Object {
            Test-VisibleDirectory -Directory $_ -AllowHidden:$AllowHidden
        } | Sort-Object FullName)

        foreach ($child in $children) {
            $childDepth = Get-RelativeDepth -Root $resolvedRoot -Path $child.FullName
            if ($childDepth -le $Depth) {
                $candidates.Add($child.FullName)
            }

            if ($childDepth -lt $Depth) {
                $pending.Enqueue($child)
            }
        }
    }

    return @($candidates | Sort-Object -Unique)
}

function Get-ProjectPathsFromFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "ProjectsFile not found: $Path"
    }

    $entries = New-Object 'System.Collections.Generic.List[string]'
    foreach ($line in (Get-Content -LiteralPath $Path -ErrorAction Stop)) {
        $trimmed = $line.Trim()
        if ([string]::IsNullOrWhiteSpace($trimmed)) {
            continue
        }

        if ($trimmed.StartsWith('#')) {
            continue
        }

        $entries.Add($trimmed.Trim('"'))
    }

    return @($entries | Sort-Object -Unique)
}

function Get-ResolvedInputProjectPaths {
    switch ($PSCmdlet.ParameterSetName) {
        'RootScan' {
            return Get-DiscoveredProjectPaths -ScanRoot $RootPath -Depth $RecurseDepth -AllowHidden:$IncludeHidden
        }
        'ExplicitList' {
            return @($ProjectPaths | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | ForEach-Object { $_.Trim() } | Sort-Object -Unique)
        }
        'ProjectsFile' {
            return Get-ProjectPathsFromFile -Path $ProjectsFile
        }
        default {
            throw "Unsupported parameter set: $($PSCmdlet.ParameterSetName)"
        }
    }
}

function Get-VersionMetadata {
    param(
        [Parameter(Mandatory = $true)]
        [string]$VersionFilePath
    )

    $metadata = @{
        source_hub = ''
        source_path = ''
        synced_at = ''
        robocopy_exit_code = ''
    }

    if (-not (Test-Path -LiteralPath $VersionFilePath -PathType Leaf)) {
        return $metadata
    }

    foreach ($rawLine in (Get-Content -LiteralPath $VersionFilePath -ErrorAction Stop)) {
        $line = $rawLine.Trim()
        if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith('#')) {
            continue
        }

        $separatorIndex = $line.IndexOf('=')
        if ($separatorIndex -lt 1) {
            continue
        }

        $key = $line.Substring(0, $separatorIndex).Trim().ToLowerInvariant()
        $value = $line.Substring($separatorIndex + 1).Trim()
        if ($metadata.ContainsKey($key)) {
            $metadata[$key] = $value
        }
    }

    return $metadata
}

function Get-SkillEntryInfo {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath
    )

    $codexSkillsRoot = Join-Path $ProjectPath '.codex\skills'
    $agentsSkillsRoot = Join-Path $ProjectPath '.agents\skills'
    $githubSkillsRoot = Join-Path $ProjectPath '.github\skills'

    $codexSkillDirectories = @()
    if (Test-Path -LiteralPath $codexSkillsRoot -PathType Container) {
        $codexSkillDirectories = @(Get-ChildItem -LiteralPath $codexSkillsRoot -Directory -Force -ErrorAction Stop | Where-Object {
            $_.Name -notlike '_*' -and (Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') -PathType Leaf)
        })
    }

    $agentsDirectorySkills = @()
    $agentsSummaryFiles = @()
    if (Test-Path -LiteralPath $agentsSkillsRoot -PathType Container) {
        $agentsDirectorySkills = @(Get-ChildItem -LiteralPath $agentsSkillsRoot -Directory -Force -ErrorAction Stop | Where-Object {
            Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') -PathType Leaf
        })
        $agentsSummaryFiles = @(Get-ChildItem -LiteralPath $agentsSkillsRoot -File -Filter '*.md' -Force -ErrorAction Stop)
    }

    $githubMarkdownSkills = @()
    if (Test-Path -LiteralPath $githubSkillsRoot -PathType Container) {
        $githubMarkdownSkills = @(Get-ChildItem -LiteralPath $githubSkillsRoot -File -Filter '*.md' -Force -ErrorAction Stop)
    }

    return @{
        codex_count = $codexSkillDirectories.Count
        agents_count = ($agentsDirectorySkills.Count + $agentsSummaryFiles.Count)
        github_count = $githubMarkdownSkills.Count
        total_count = ($codexSkillDirectories.Count + $agentsDirectorySkills.Count + $agentsSummaryFiles.Count + $githubMarkdownSkills.Count)
        has_protocol = (Test-Path -LiteralPath (Join-Path $codexSkillsRoot '_protocol') -PathType Container)
    }
}

function Find-BackupDirectories {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath,

        [int]$SearchDepth = 3
    )

    $matches = New-Object 'System.Collections.Generic.List[string]'
    $resolvedProjectPath = (Resolve-Path -LiteralPath $ProjectPath).ProviderPath
    $pending = New-Object 'System.Collections.Generic.Queue[hashtable]'
    $pending.Enqueue(@{
        path = $resolvedProjectPath
        depth = 0
    })

    while ($pending.Count -gt 0) {
        $current = $pending.Dequeue()
        $currentPath = [string]$current.path
        $currentDepth = [int]$current.depth
        if ($currentDepth -ge $SearchDepth) {
            continue
        }

        try {
            $children = @(Get-ChildItem -LiteralPath $currentPath -Directory -Force -ErrorAction Stop)
        }
        catch {
            continue
        }

        foreach ($child in $children) {
            $relativePath = $child.FullName.Substring($resolvedProjectPath.Length).TrimStart('\')
            if ($script:BackupDirectoryNames -contains $child.Name.ToLowerInvariant()) {
                $matches.Add($relativePath)
            }

            $pending.Enqueue(@{
                path = $child.FullName
                depth = ($currentDepth + 1)
            })
        }
    }

    return @($matches | Sort-Object -Unique)
}

function New-InaccessibleAuditRecord {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath,

        [Parameter(Mandatory = $true)]
        [string]$Reason
    )

    return [pscustomobject]@{
        ProjectPath = $ProjectPath
        Exists = $false
        HasCodexSkills = $false
        HasAgentsSkills = $false
        HasGithubSkills = $false
        HasSkillConfig = $false
        IsHubRepository = $false
        HubSignals = ''
        SkillConfigFiles = ''
        HasBackupDir = $false
        BackupDirNames = ''
        HasSkillsetVersion = $false
        SourceHub = ''
        SourcePath = ''
        SyncedAt = ''
        RobocopyExitCode = ''
        SeedStatus = 'inaccessible'
        RiskLevel = 'high'
        RecommendedAction = 'inspect_path_access'
        Notes = $Reason
    }
}

function Get-SeedDecision {
    param(
        [Parameter(Mandatory = $true)]
        [pscustomobject]$Inspection
    )

    $notes = New-Object 'System.Collections.Generic.List[string]'
    if (-not [string]::IsNullOrWhiteSpace($Inspection.Notes)) {
        $notes.Add($Inspection.Notes)
    }

    if ($Inspection.HasBackupDir) {
        $notes.Add("Backup-like directories found: $($Inspection.BackupDirNames)")
    }

    if ($Inspection.HasSkillsetVersion) {
        if (-not [string]::IsNullOrWhiteSpace($Inspection.SourceHub)) {
            $notes.Add("Version metadata source_hub=$($Inspection.SourceHub)")
        }
    }
    elseif ($Inspection.TotalSkillArtifacts -gt 0) {
        $notes.Add('Skill artifacts exist without _skillset_version.txt metadata')
    }

    if (-not $Inspection.HasSkillConfig -and $Inspection.HasAnySkillTrace) {
        $notes.Add('Missing .codex/skill-config')
    }

    if (-not $Inspection.Exists) {
        return @{
            SeedStatus = 'inaccessible'
            RiskLevel = 'high'
            RecommendedAction = 'inspect_path_access'
            Notes = ($notes -join '; ')
        }
    }

    if ($Inspection.IsHubRepository) {
        if (-not [string]::IsNullOrWhiteSpace($Inspection.HubSignals)) {
            $notes.Add("Hub self-detection signals: $($Inspection.HubSignals)")
        }

        return @{
            SeedStatus = 'hub_repository'
            RiskLevel = 'low'
            RecommendedAction = 'skip_hub_repo'
            Notes = ($notes -join '; ')
        }
    }

    if (-not $Inspection.HasAnySkillTrace) {
        $notes.Add('No .codex/.agents/.github skill traces found')
        return @{
            SeedStatus = 'no_skill_structure'
            RiskLevel = 'low'
            RecommendedAction = 'verify_project_first'
            Notes = ($notes -join '; ')
        }
    }

    $isAlreadySeeded = (
        $Inspection.HasCodexSkills -and
        $Inspection.HasSkillsetVersion -and
        $Inspection.SourceHub -eq 'ai-skill-hub' -and
        $Inspection.HasSkillConfig
    )
    if ($isAlreadySeeded) {
        if ($Inspection.HasCodexProtocol) {
            $notes.Add('Detected .codex/skills/_protocol alongside ai-skill-hub metadata')
        }

        return @{
            SeedStatus = 'already_seeded'
            RiskLevel = 'low'
            RecommendedAction = 'no_action'
            Notes = ($notes -join '; ')
        }
    }

    $hasCustomSourceHub = $Inspection.HasSkillsetVersion -and -not [string]::IsNullOrWhiteSpace($Inspection.SourceHub) -and @('ai-skill-hub', 'codex-skill-hub') -notcontains $Inspection.SourceHub
    $hasCodexSkillsWithoutMetadata = $Inspection.HasCodexSkills -and $Inspection.CodexSkillCount -gt 0 -and -not $Inspection.HasSkillsetVersion
    $hasAmbiguousCodexLayout = $Inspection.HasCodexSkills -and $Inspection.CodexSkillCount -eq 0 -and -not $Inspection.HasSkillsetVersion -and $Inspection.TotalSkillArtifacts -gt 0

    if ($Inspection.HasBackupDir -or $hasCustomSourceHub -or $hasCodexSkillsWithoutMetadata -or $hasAmbiguousCodexLayout) {
        if ($hasCustomSourceHub) {
            $notes.Add("Custom distribution source_hub '$($Inspection.SourceHub)' requires inspection")
        }

        if ($hasCodexSkillsWithoutMetadata) {
            $notes.Add('Found .codex/skills content but no trusted version metadata')
        }

        if ($hasAmbiguousCodexLayout) {
            $notes.Add('Found .codex/skills structure with ambiguous contents')
        }

        $recommendedAction = if ($Inspection.HasBackupDir) {
            'manual_review_backup'
        }
        else {
            'inspect_custom_distribution'
        }

        return @{
            SeedStatus = 'risky_manual_review'
            RiskLevel = 'high'
            RecommendedAction = $recommendedAction
            Notes = ($notes -join '; ')
        }
    }

    if (-not $Inspection.HasSkillConfig) {
        return @{
            SeedStatus = 'missing_config'
            RiskLevel = 'medium'
            RecommendedAction = 'restore_or_create_skill_config'
            Notes = ($notes -join '; ')
        }
    }

    $riskLevel = if ($Inspection.HasSkillsetVersion -and $Inspection.SourceHub -eq 'codex-skill-hub') {
        'low'
    }
    else {
        'medium'
    }

    if ($Inspection.HasSkillsetVersion -and $Inspection.SourceHub -eq 'codex-skill-hub') {
        $notes.Add('Legacy source_hub indicates an older hub-managed distribution')
    }

    return @{
        SeedStatus = 'ready_for_reseed'
        RiskLevel = $riskLevel
        RecommendedAction = 'dryrun_then_reseed'
        Notes = ($notes -join '; ')
    }
}

function Get-ProjectAuditRecord {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath
    )

    try {
        if (-not (Test-Path -LiteralPath $ProjectPath)) {
            return New-InaccessibleAuditRecord -ProjectPath $ProjectPath -Reason 'Project path does not exist'
        }

        if (-not (Test-Path -LiteralPath $ProjectPath -PathType Container)) {
            return New-InaccessibleAuditRecord -ProjectPath $ProjectPath -Reason 'Project path is not a directory'
        }

        $resolvedProjectPath = (Resolve-Path -LiteralPath $ProjectPath -ErrorAction Stop).ProviderPath
        $codexSkillsRoot = Join-Path $resolvedProjectPath '.codex\skills'
        $agentsSkillsRoot = Join-Path $resolvedProjectPath '.agents\skills'
        $githubSkillsRoot = Join-Path $resolvedProjectPath '.github\skills'
        $skillConfigRoot = Join-Path $resolvedProjectPath '.codex\skill-config'
        $versionFilePath = Join-Path $codexSkillsRoot '_skillset_version.txt'

        $versionMetadata = Get-VersionMetadata -VersionFilePath $versionFilePath
        $skillEntryInfo = Get-SkillEntryInfo -ProjectPath $resolvedProjectPath
        $backupDirectories = @(Find-BackupDirectories -ProjectPath $resolvedProjectPath)
        $hubSignals = @(Get-HubRepositorySignals -ProjectPath $resolvedProjectPath)
        $skillConfigFiles = @()
        if (Test-Path -LiteralPath $skillConfigRoot -PathType Container) {
            $skillConfigFiles = @(Get-ChildItem -LiteralPath $skillConfigRoot -File -Recurse -Force -ErrorAction Stop | ForEach-Object {
                $_.FullName.Substring($resolvedProjectPath.Length).TrimStart('\')
            } | Sort-Object)
        }

        $hasCodexSkills = Test-Path -LiteralPath $codexSkillsRoot -PathType Container
        $hasAgentsSkills = Test-Path -LiteralPath $agentsSkillsRoot -PathType Container
        $hasGithubSkills = Test-Path -LiteralPath $githubSkillsRoot -PathType Container
        $hasSkillConfig = Test-Path -LiteralPath $skillConfigRoot -PathType Container
        $hasSkillsetVersion = Test-Path -LiteralPath $versionFilePath -PathType Leaf
        $hasAnySkillTrace = (
            $hasSkillsetVersion -or
            $skillEntryInfo.total_count -gt 0 -or
            $hasCodexSkills -or
            $hasAgentsSkills -or
            $hasGithubSkills
        )

        $inspection = [pscustomobject]@{
            ProjectPath = $resolvedProjectPath
            Exists = $true
            HasCodexSkills = [bool]$hasCodexSkills
            HasAgentsSkills = [bool]$hasAgentsSkills
            HasGithubSkills = [bool]$hasGithubSkills
            HasSkillConfig = [bool]$hasSkillConfig
            IsHubRepository = (Test-IsHubRepository -Signals $hubSignals)
            HubSignals = ($hubSignals -join '; ')
            SkillConfigFiles = ($skillConfigFiles -join '; ')
            HasBackupDir = ($backupDirectories.Count -gt 0)
            BackupDirNames = ($backupDirectories -join '; ')
            HasSkillsetVersion = [bool]$hasSkillsetVersion
            SourceHub = [string]$versionMetadata.source_hub
            SourcePath = [string]$versionMetadata.source_path
            SyncedAt = [string]$versionMetadata.synced_at
            RobocopyExitCode = [string]$versionMetadata.robocopy_exit_code
            CodexSkillCount = [int]$skillEntryInfo.codex_count
            AgentsSkillCount = [int]$skillEntryInfo.agents_count
            GithubSkillCount = [int]$skillEntryInfo.github_count
            TotalSkillArtifacts = [int]$skillEntryInfo.total_count
            HasCodexProtocol = [bool]$skillEntryInfo.has_protocol
            HasAnySkillTrace = [bool]$hasAnySkillTrace
            Notes = ''
        }

        $decision = Get-SeedDecision -Inspection $inspection

        return [pscustomobject]@{
            ProjectPath = $inspection.ProjectPath
            Exists = $inspection.Exists
            HasCodexSkills = $inspection.HasCodexSkills
            HasAgentsSkills = $inspection.HasAgentsSkills
            HasGithubSkills = $inspection.HasGithubSkills
            HasSkillConfig = $inspection.HasSkillConfig
            IsHubRepository = $inspection.IsHubRepository
            HubSignals = $inspection.HubSignals
            SkillConfigFiles = $inspection.SkillConfigFiles
            HasBackupDir = $inspection.HasBackupDir
            BackupDirNames = $inspection.BackupDirNames
            HasSkillsetVersion = $inspection.HasSkillsetVersion
            SourceHub = $inspection.SourceHub
            SourcePath = $inspection.SourcePath
            SyncedAt = $inspection.SyncedAt
            RobocopyExitCode = $inspection.RobocopyExitCode
            SeedStatus = $decision.SeedStatus
            RiskLevel = $decision.RiskLevel
            RecommendedAction = $decision.RecommendedAction
            Notes = $decision.Notes
        }
    }
    catch {
        return New-InaccessibleAuditRecord -ProjectPath $ProjectPath -Reason $_.Exception.Message
    }
}

function Get-AuditSummary {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$AuditRecords
    )

    $statusSummary = [ordered]@{}
    foreach ($record in $AuditRecords) {
        if (-not $statusSummary.Contains($record.SeedStatus)) {
            $statusSummary[$record.SeedStatus] = 0
        }

        $statusSummary[$record.SeedStatus] += 1
    }

    return [ordered]@{
        generated_at = (Get-Date).ToString('yyyy-MM-ddTHH:mm:ssK')
        total_projects = $AuditRecords.Count
        status_summary = $statusSummary
    }
}

function ConvertTo-MarkdownTable {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$AuditRecords,

        [Parameter(Mandatory = $true)]
        [hashtable]$Summary
    )

    $statusParts = @()
    foreach ($entry in $Summary.status_summary.GetEnumerator()) {
        $statusParts += "$($entry.Key)=$($entry.Value)"
    }

    $header = @(
        '# Re-seed Audit Report'
        ''
        "- GeneratedAt: $($Summary.generated_at)"
        "- TotalProjects: $($Summary.total_projects)"
        "- StatusSummary: $($statusParts -join ', ')"
        ''
        '| ProjectPath | SeedStatus | RiskLevel | RecommendedAction | SourceHub | HasSkillConfig | HasBackupDir | Notes |'
        '| --- | --- | --- | --- | --- | --- | --- | --- |'
    )

    $rows = foreach ($record in $AuditRecords) {
        $notes = [string]$record.Notes
        $escapedNotes = $notes.Replace('|', '\|')
        "| $($record.ProjectPath.Replace('|', '\|')) | $($record.SeedStatus) | $($record.RiskLevel) | $($record.RecommendedAction) | $($record.SourceHub.Replace('|', '\|')) | $($record.HasSkillConfig) | $($record.HasBackupDir) | $escapedNotes |"
    }

    return (@($header) + @($rows)) -join [Environment]::NewLine
}

function Format-AuditTable {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$AuditRecords,

        [switch]$ShowVerboseColumns
    )

    $selected = if ($ShowVerboseColumns) {
        $AuditRecords | Select-Object ProjectPath, SeedStatus, RiskLevel, RecommendedAction, IsHubRepository, HubSignals, HasCodexSkills, HasAgentsSkills, HasGithubSkills, HasSkillConfig, HasBackupDir, SourceHub, SourcePath, Notes
    }
    else {
        $AuditRecords | Select-Object ProjectPath, SeedStatus, RiskLevel, RecommendedAction, IsHubRepository, HasSkillConfig, HasBackupDir, SourceHub
    }

    return ($selected | Format-Table -AutoSize | Out-String).TrimEnd()
}

function Resolve-ExportPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$BasePath,

        [Parameter(Mandatory = $true)]
        [string]$ChosenFormat
    )

    $extensionMap = @{
        table = 'txt'
        csv = 'csv'
        json = 'json'
        md = 'md'
    }
    $targetExtension = $extensionMap[$ChosenFormat]

    $treatAsDirectory = $false
    if (Test-Path -LiteralPath $BasePath -PathType Container) {
        $treatAsDirectory = $true
    }
    elseif ([string]::IsNullOrWhiteSpace([System.IO.Path]::GetExtension($BasePath))) {
        $treatAsDirectory = $true
    }

    if ($treatAsDirectory) {
        if (-not (Test-Path -LiteralPath $BasePath)) {
            New-Item -ItemType Directory -Path $BasePath -Force | Out-Null
        }

        $fileName = 'reseed_audit_report.{0}' -f $targetExtension
        return Join-Path $BasePath $fileName
    }

    $parentPath = Split-Path -Path $BasePath -Parent
    if (-not [string]::IsNullOrWhiteSpace($parentPath) -and -not (Test-Path -LiteralPath $parentPath)) {
        New-Item -ItemType Directory -Path $parentPath -Force | Out-Null
    }

    return $BasePath
}

function Export-AuditRecords {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$AuditRecords,

        [Parameter(Mandatory = $true)]
        [hashtable]$Summary,

        [Parameter(Mandatory = $true)]
        [string]$DestinationPath,

        [Parameter(Mandatory = $true)]
        [string]$ChosenFormat,

        [switch]$ShowVerboseColumns
    )

    switch ($ChosenFormat) {
        'csv' {
            $csv = $AuditRecords | ConvertTo-Csv -NoTypeInformation
            [System.IO.File]::WriteAllText($DestinationPath, ($csv -join [Environment]::NewLine), [System.Text.UTF8Encoding]::new($false))
        }
        'json' {
            $payload = [ordered]@{
                generated_at = $Summary.generated_at
                total_projects = $Summary.total_projects
                status_summary = $Summary.status_summary
                projects = $AuditRecords
            }
            [System.IO.File]::WriteAllText($DestinationPath, ($payload | ConvertTo-Json -Depth 6), [System.Text.UTF8Encoding]::new($false))
        }
        'md' {
            $markdown = ConvertTo-MarkdownTable -AuditRecords $AuditRecords -Summary $Summary
            [System.IO.File]::WriteAllText($DestinationPath, $markdown, [System.Text.UTF8Encoding]::new($false))
        }
        'table' {
            $table = Format-AuditTable -AuditRecords $AuditRecords -ShowVerboseColumns:$ShowVerboseColumns
            [System.IO.File]::WriteAllText($DestinationPath, $table, [System.Text.UTF8Encoding]::new($false))
        }
        default {
            throw "Unsupported export format: $ChosenFormat"
        }
    }
}

$resolvedProjectPaths = @(Get-ResolvedInputProjectPaths)
$auditRecords = foreach ($projectPath in $resolvedProjectPaths) {
    Get-ProjectAuditRecord -ProjectPath $projectPath
}
$auditRecords = @($auditRecords | Sort-Object ProjectPath)
$summary = Get-AuditSummary -AuditRecords $auditRecords

if ($OutputPath) {
    $resolvedExportPath = Resolve-ExportPath -BasePath $OutputPath -ChosenFormat $Format
    Export-AuditRecords -AuditRecords $auditRecords -Summary $summary -DestinationPath $resolvedExportPath -ChosenFormat $Format -ShowVerboseColumns:$VerboseReport
    Write-Host "Exported audit report: $resolvedExportPath" -ForegroundColor Green
}

switch ($Format) {
    'json' {
        if (-not $OutputPath) {
            [ordered]@{
                generated_at = $summary.generated_at
                total_projects = $summary.total_projects
                status_summary = $summary.status_summary
                projects = $auditRecords
            } | ConvertTo-Json -Depth 6
        }
        else {
            Write-Host "Status summary: $((($summary.status_summary.GetEnumerator() | ForEach-Object { '{0}={1}' -f $_.Key, $_.Value }) -join ', '))"
        }
    }
    'csv' {
        if (-not $OutputPath) {
            $auditRecords | ConvertTo-Csv -NoTypeInformation
        }
        else {
            Write-Host "Status summary: $((($summary.status_summary.GetEnumerator() | ForEach-Object { '{0}={1}' -f $_.Key, $_.Value }) -join ', '))"
        }
    }
    'md' {
        $markdownOutput = ConvertTo-MarkdownTable -AuditRecords $auditRecords -Summary $summary
        if (-not $OutputPath) {
            $markdownOutput
        }
        else {
            Write-Host "Status summary: $((($summary.status_summary.GetEnumerator() | ForEach-Object { '{0}={1}' -f $_.Key, $_.Value }) -join ', '))"
        }
    }
    default {
        Write-Host ""
        Write-Host "Re-seed audit summary" -ForegroundColor Cyan
        Write-Host "GeneratedAt: $($summary.generated_at)"
        Write-Host "TotalProjects: $($summary.total_projects)"
        Write-Host "StatusSummary: $((($summary.status_summary.GetEnumerator() | ForEach-Object { '{0}={1}' -f $_.Key, $_.Value }) -join ', '))"
        Write-Host ""
        Write-Host (Format-AuditTable -AuditRecords $auditRecords -ShowVerboseColumns:$VerboseReport)
    }
}
