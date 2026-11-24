# Run of Show: 7 Minute Demo

**Setting:** Fake Health Company. The CISO has paused Copilot expansion over PHI and code-quality concerns. Goal: show how GitHub governs AI-assisted development so the rollout can proceed safely.

**Before you start (10 minutes before)**
- [ ] `.\scripts\reset-demo.ps1` has run and the PR shows a CodeQL alert
- [ ] Tabs open: repo home · `.github/copilot-instructions.md` · the demo PR · Security → Code scanning · Settings → Rules
- [ ] VS Code open on the repo, Copilot Chat signed in
- [ ] Backup screen recording on the desktop
- [ ] Notifications off, font size up (Cmd/Ctrl + `+` twice)

---

## 0:00 Copilot custom instructions (1 min)
**Show:** `.github/copilot-instructions.md`

> "You wouldn't let a new engineer start without onboarding. This file is Copilot's onboarding. Copilot reads it automatically: parameterized SQL only, no secrets in code, and Rule 1: patient data never goes in code. Rule 2 is 'see Rule 1.'"

**Point to land:** Governance starts *before* code is written. 📄

## 1:00 Copilot writes a change (1.5 min)
**Option A, live (uses about 1 Copilot Chat request):** in VS Code Copilot Chat:
> "Add a GET /claims/search endpoint that filters claims by a `status` query parameter."

Either outcome supports the story:
- **Safe code →** "That's the custom instructions doing their job."
- **Unsafe code →** "Even good engineers make mistakes. That's why we don't rely on instructions alone."

**Option B, pre-staged (no Copilot usage):** open the PR titled **"Small, harmless change"**.
> "Here's a developer, human or AI, it doesn't matter, submitting a small change."

> Always move to the pre-staged PR for the next step, so the scan result is guaranteed.

## 2:30 CodeQL catches it (1.5 min)
**Show:** the PR checks → Tests ✅ green, CodeQL ❌ SQL injection in `search_claims`.

> "The unit tests pass. A reviewer skimming this on a Friday afternoon would probably approve it. CodeQL traced user input from the query string straight into a SQL statement. In a claims system, that's a breach."

**Point to land:** Passing tests isn't the same as secure code. Code scanning closes that gap automatically. 📄

## 4:00 Copilot Autofix proposes the fix (1.5 min)
**Show:** the Copilot Autofix suggestion on the alert → the proposed diff (parameterized query).

> "Copilot Autofix proposes the fix and explains it. A human still reviews and approves it. The developer stays accountable."

Commit the suggestion **or** just show it (committing reruns the scans, so only do it if time allows).

## 5:30 Rulesets enforce the policy (1 min)
**Show:** the blocked merge box → Settings → Rules → `main-protection`.

> "Even if someone wanted to merge anyway, they can't. This ruleset requires passing tests and a clean CodeQL scan before anything reaches main. It's policy enforced by the platform, and it's the evidence your auditors will ask for."

## 6:30 Audit trail + template (30 sec)
**Show:** PR timeline (every commit, check, and decision recorded) → repo home → **Use this template**.

> "Everything you just saw is recorded. That's your audit trail. And this kit is a template: the next business unit, or the next CSA, can stand it up in ten minutes."

---

## If things go wrong
| Problem | Recovery line | Action |
|---|---|---|
| Copilot slow / allowance used up | "Here's one I prepared earlier." | Jump to Option B |
| CodeQL still running | "The scan is still running. Here's this morning's result." | Security → Code scanning tab |
| Wi-Fi drops | "Let me switch to the recording." | Play backup video |
| Panel interrupts with a question | Answer it. The demo serves the conversation. | Skip to the step they care about |

## Cut list (if running long)
1. Skip Option A; go straight to the pre-staged PR.
2. Skip the ruleset settings page; just show the blocked merge.
3. Skip the template button; mention it in one sentence.
