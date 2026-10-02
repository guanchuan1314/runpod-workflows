param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[a-z0-9][a-z0-9_-]+$')]
    [string]$DockerHubUsername,
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[A-Za-z0-9_][A-Za-z0-9_.-]{0,127}$')]
    [string]$Version,
    [ValidatePattern('^[a-z0-9][a-z0-9_.-]+$')]
    [string]$RepositoryName = 'runpod-comfyui',
    [ValidateSet('Qwen-2.1-Q4', 'Qwen-2.1-Q8', 'Minimax-H3-INT8', 'Minimax-H3-BF16')]
    [string[]]$Variants = @('Qwen-2.1-Q4', 'Qwen-2.1-Q8', 'Minimax-H3-INT8', 'Minimax-H3-BF16')
)

$ErrorActionPreference = 'Stop'
Get-Command docker -ErrorAction Stop | Out-Null
# Authenticate separately with docker login; never pass secrets as script arguments.
foreach ($Variant in $Variants) {
    $ImageRef = "docker.io/$DockerHubUsername/${RepositoryName}:$($Variant.ToLowerInvariant())-$Version"
    $DockerfilePath = Join-Path (Join-Path $PSScriptRoot $Variant) 'Dockerfile'
    Write-Host "Building $ImageRef"
    & docker build --platform linux/amd64 --file $DockerfilePath --tag $ImageRef $PSScriptRoot
    if ($LASTEXITCODE -ne 0) { throw "Build failed for $Variant; image was not pushed." }
    & docker push $ImageRef
    if ($LASTEXITCODE -ne 0) { throw "Push failed for $Variant." }
    Write-Host "Published $ImageRef"
}
