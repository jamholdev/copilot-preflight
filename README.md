# Copilot Pre-Flight

> Demo kit, work in progress. Synthetic data only. Not official GitHub content.

**A reusable demo kit for helping regulated customers adopt GitHub Copilot with guardrails.**

This repo is a **template**. Click **Use this template**, pick a scenario, run the reset script, and you have a 7-minute demo showing how AI-written code gets caught, fixed, and governed before it reaches production.

---

## What the demo shows

| Step | What happens | GitHub feature |
|---|---|---|
| 1 | Copilot gets house rules for this codebase | Copilot custom instructions (`.github/copilot-instructions.md`) |
| 2 | A "small, harmless" PR adds a search endpoint | Copilot Chat / pull request |
| 3 | A SQL injection is flagged on the PR, even though unit tests pass | Code scanning with CodeQL |
| 4 | A fix is proposed; a human reviews and approves it | Copilot Autofix |
| 5 | Merge is blocked until tests and the security scan pass | Repository rulesets |
| 6 | Every commit, check, and decision is recorded | PR history / audit log |

**The point:** Copilot speeds up development, CodeQL and Copilot Autofix catch and fix what slips through, rulesets enforce the policy, and a human stays accountable throughout.

---

## Repo layout

```
app/                         ClaimsBot, a tiny Flask claims API (synthetic data only)
tests/                       pytest suite, including an injection test
demo/payloads/               the deliberately vulnerable version used by the demo PR
demo/pr-body.md              PR description for the demo
scripts/reset-demo.ps1       recreates the demo PR so every run starts clean (Windows)
scripts/reset-demo.sh        same, for macOS/Linux
.github/copilot-instructions.md   Copilot custom instructions
.github/workflows/codeql.yml      CodeQL on every PR (Copilot Autofix builds on this)
.github/workflows/tests.yml       pytest on every PR
.github/rulesets/main-protection.json  importable ruleset protecting main
scenarios/                   customer stories: healthcare (full), banking & public sector (stubs)
docs/run-of-show.md          7-minute demo script, talking points, fallbacks
docs/risk-register.md        HIPAA/BAA, GHES vs GHEC, data residency, and how to pivot
docs/pilot-scorecard.md      baseline + target metrics for a 90-day pilot
docs/setup.md                push this repo, enable settings, rehearse
```

## Quick start

1. Push this repo to GitHub as **public** (see [`docs/setup.md`](docs/setup.md)).
2. Settings → General → tick **Template repository**.
3. Import the ruleset from `.github/rulesets/main-protection.json`.
4. Run `.\scripts\reset-demo.ps1` (Windows) or `./scripts/reset-demo.sh` (macOS/Linux) at least 10 minutes before you present.
5. Follow [`docs/run-of-show.md`](docs/run-of-show.md).

Run the app locally (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
flask --app app run      # http://127.0.0.1:5000/health
```

---

## Confidence legend

Every claim in this kit is tagged so presenters know what's proven:

- ✅ **Tested:** personally run end to end in this repo
- 📄 **Documented:** verified in GitHub Docs / changelog, not yet run here
- 🔍 **Validate:** must be confirmed in the customer's environment or with legal/trust teams

> Update tags after each rehearsal. Never present a 📄 as a ✅.

---

## Ground rules

- **Synthetic data only.** No real customer names, code, or data. Generic fictional companies only.
- **Not official GitHub content.** A field-built demo kit; validate product details against current docs.
- **Not legal advice.** Compliance items are framed as questions for the customer's counsel and GitHub's trust team.
