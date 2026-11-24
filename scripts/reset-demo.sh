#!/usr/bin/env bash
# Reset the demo: recreate the "Small, harmless change" PR with the vulnerable
# search endpoint, so CodeQL flags it and Copilot Autofix proposes a fix.
#
# Requires: git, GitHub CLI (gh) authenticated via `gh auth login`.
# Run from the repo root:  ./scripts/reset-demo.sh
set -euo pipefail

BRANCH="demo/claims-search"
BASE="main"

echo "==> Returning to ${BASE}"
git checkout "${BASE}"
git pull --ff-only origin "${BASE}"

echo "==> Clearing any previous demo PR/branch"
if gh pr view "${BRANCH}" --json state -q .state 2>/dev/null | grep -q OPEN; then
  gh pr close "${BRANCH}" --delete-branch || true
fi
git push origin --delete "${BRANCH}" 2>/dev/null || true
git branch -D "${BRANCH}" 2>/dev/null || true

echo "==> Creating branch with demo payload"
git checkout -b "${BRANCH}"
cp demo/payloads/claims_with_search.py app/claims.py
git add app/claims.py
git commit -m "Add claims search by status"
git push -u origin "${BRANCH}"

echo "==> Opening PR"
gh pr create \
  --base "${BASE}" \
  --head "${BRANCH}" \
  --title "Small, harmless change" \
  --body-file demo/pr-body.md

git checkout "${BASE}"
echo "==> Done. CodeQL takes ~2-4 minutes. Run this at least 10 minutes before the demo."
