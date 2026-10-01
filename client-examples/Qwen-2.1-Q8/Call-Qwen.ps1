param(
    [Parameter(Mandatory=$true)][string]$Prompt,
    [string]$EndpointId = 'ojli7psn8voa05'
)
$ErrorActionPreference = 'Stop'
if (-not $env:RUNPOD_API_KEY) { throw 'Set RUNPOD_API_KEY in this terminal before calling.' }
$workflow = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'workflow-api.json') -Raw | ConvertFrom-Json
$workflow.'452'.inputs.prompt = $Prompt
$body = @{input = @{workflow = $workflow}} | ConvertTo-Json -Depth 50 -Compress
$headers = @{Authorization = "Bearer $env:RUNPOD_API_KEY"}
$job = Invoke-RestMethod -Uri "https://api.runpod.ai/v2/$EndpointId/run" -Method Post -Headers $headers -ContentType 'application/json' -Body $body
Write-Output $job
Write-Output "Status URL: https://api.runpod.ai/v2/$EndpointId/status/$($job.id)"
