# 90-Day Pilot Scorecard

**Rule:** capture the baseline *before* licenses go live, and compare pilot teams against a control team. Without a baseline, every number is a vibe.

| Category | Metric | Source | Baseline | Day-90 target | Owner |
|---|---|---|---|---|---|
| **Adoption** | Weekly active Copilot users / licensed | Copilot usage metrics | n/a | ≥ 70% | Eng enablement lead |
| **Adoption** | Developers who've used chat + completions | Copilot usage metrics | n/a | ≥ 60% | Champions |
| **Speed** | PR cycle time (open → merge), median | PR data / API | ___ hrs | -20% | VP Engineering |
| **Speed** | Lead time for changes | DORA tooling | ___ days | -15% | Platform lead |
| **Quality** | Change failure rate | DORA tooling | ___ % | no increase | Platform lead |
| **Security** | New high/critical alerts per 100 PRs | Code scanning | ___ | no increase | AppSec lead |
| **Security** | Median time to remediate code scanning alerts | Security overview | ___ days | -30% | AppSec lead |
| **People** | Developer satisfaction (survey, 1-5) | Pulse survey | ___ | +0.5 | Eng managers |

**Vanity metrics we will NOT report:** seat count, lines of code generated, "suggestions accepted" in isolation.

## Cadence
- **Weekly:** champion standup (15 min): blockers, wins, prompts that worked
- **Day 30:** health check: adoption on track? guardrails noisy?
- **Day 60:** midpoint review: adjust targets, decide expansion candidates
- **Day 90:** EBR with VP Eng, CISO, CFO → **go / adjust / stop** decision

Targets are illustrative starting points; agree real numbers with the customer at kickoff. 🔍
