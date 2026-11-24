# Reset the demo (Windows PowerShell): recreate the "Small, harmless change" PR
# with the vulnerable search endpoint, so CodeQL flags it and Copilot Autofix
# proposes a fix.
#
# Requires: Git for Windows, GitHub CLI (gh) signed in via `gh auth login`.
# Run from the repo root:
#   .\scripts\reset-demo.ps1
# If PowerShell blocks the script:
#   powershell -ExecutionPolicy Bypass -File .\scripts\reset-demo.ps1

$ErrorActionPreference = 'Continue'
$Branch = 'demo/claims-search'
$Base   = 'main'

function Invoke-Step {
    param([string]$Exe, [string[]]$ArgList)
    & $Exe @ArgList
    if ($LASTEXITCODE -ne 0) {
        throw "Failed: $Exe $($ArgList -join ' ')"
    }
}

Write-Host "==> Returning to $Base"
Invoke-Step git @('checkout', $Base)
Invoke-Step git @('pull', '--ff-only', 'origin', $Base)

Write-Host "==> Clearing any previous demo PR/branch"
$state = gh pr view $Branch --json state -q .state 2>$null
if ($LASTEXITCODE -eq 0 -and $state -eq 'OPEN') {
    gh pr close $Branch --delete-branch
}
git push origin --delete $Branch 2>$null | Out-Null
git branch -D $Branch 2>$null | Out-Null

Write-Host "==> Creating branch with demo payload"
Invoke-Step git @('checkout', '-b', $Branch)
Copy-Item -Path 'demo\payloads\claims_with_search.py' -Destination 'app\claims.py' -Force
Invoke-Step git @('add', 'app/claims.py')
Invoke-Step git @('commit', '-m', 'Add claims search by status')
Invoke-Step git @('push', '-u', 'origin', $Branch)

Write-Host "==> Opening PR"
Invoke-Step gh @('pr', 'create', '--base', $Base, '--head', $Branch,
                 '--title', 'Small, harmless change',
                 '--body-file', 'demo/pr-body.md')

Invoke-Step git @('checkout', $Base)
Write-Host "==> Done. CodeQL takes ~2-4 minutes. Run this at least 10 minutes before the demo."
