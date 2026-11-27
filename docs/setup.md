# Setup (Windows)

Total time: ~30 minutes the first time. All commands are for **PowerShell** (Start → type "PowerShell"). macOS/Linux users: see the note at the end.

## 0. Prerequisites
Install with `winget` (built into Windows 10/11), then **close and reopen PowerShell** so the new commands are found:

```powershell
winget install --id Git.Git -e
winget install --id GitHub.cli -e
winget install --id Python.Python.3.12 -e        # optional: to run the app/tests locally
winget install --id Microsoft.VisualStudioCode -e
```

Check they're installed:
```powershell
git --version
gh --version
py --version
```

Tell git who you are (one time):
```powershell
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

In VS Code, install the **GitHub Copilot** extension and sign in.

---

## 1. Push the repo

### Option A: PowerShell (recommended; also needed for the reset script)

```powershell
# 1. Unzip and enter the folder (run from the folder containing the zip, e.g. Downloads)
cd $HOME\Downloads
Expand-Archive .\copilot-preflight.zip -DestinationPath .
cd .\copilot-preflight

# 2. Sign in to GitHub from PowerShell (one time)
gh auth login
#    choose: GitHub.com -> HTTPS -> Yes (authenticate Git) -> Login with a web browser

# 3. Initialise git and make the first commit
git init -b main
git add .
git commit -m "Initial commit: Copilot Pre-Flight demo kit"

# 4. Keep the Mac/Linux script executable for other template users
git update-index --chmod=+x scripts/reset-demo.sh
git commit -m "Mark reset-demo.sh executable"

# 5. Create a PUBLIC repo on GitHub and push in one step
gh repo create copilot-preflight --public --source . --push
```

> **Why public?** CodeQL code scanning and Copilot Autofix are free on public repos. The repo only contains synthetic data.

> If `Expand-Archive` creates a nested folder (`copilot-preflight\copilot-preflight`), `cd` into the inner one. It's the one containing `README.md`.

**Without `gh`** (plain git): create an empty public repo named `copilot-preflight` on github.com (no README/license), then:

```powershell
git init -b main
git add .
git commit -m "Initial commit: Copilot Pre-Flight demo kit"
git remote add origin https://github.com/<your-username>/copilot-preflight.git
git push -u origin main
```
Git for Windows includes Git Credential Manager, which opens a browser window to sign you in on first push.

### Option B: Manual upload in the browser
1. On github.com: **+** → **New repository** → name `copilot-preflight` → **Public** → don't add a README → **Create repository**.
2. Click **uploading an existing file**.
3. In File Explorer, open the unzipped folder and turn on **View → Show → Hidden items** (Windows 11) or **View → Hidden items** (Windows 10) so you can see `.github`, `.gitignore`, and `.gitattributes`.
4. Select **everything inside** the folder (Ctrl + A) and drag it onto the upload page, not the folder itself.
5. Commit directly to `main`.
6. Check the repo shows a `.github` folder. If not, upload it again. Without it there's no CodeQL, no custom instructions, no ruleset file.

> With Option B you'll still need git + `gh` locally to use the reset script, or create the demo PR by hand (step 5 below). To get a local copy afterwards: `gh repo clone <your-username>/copilot-preflight`.

---

## 2. Repo settings
1. **Settings → General → Template repository** ✔️
2. **Actions tab:** confirm the `CodeQL` and `Tests` workflows ran green on `main`. If CodeQL fails on action versions, update the `@v4`/`@v5` tags to the current major versions listed on each action's GitHub page.
3. **Settings → Advanced Security:** confirm:
   - Secret scanning + **Push protection**: enabled
   - Code scanning shows the CodeQL workflow (advanced setup). Leave *default setup* off because it conflicts with the workflow file.
   - Copilot Autofix: on (it's on by default for CodeQL alerts on public repos)

## 3. Import the ruleset
1. **Settings → Rules → Rulesets → New ruleset → Import a ruleset**
2. Choose `.github\rulesets\main-protection.json` from your local copy.
3. Review → **Create**.

It requires: a PR to change `main`, the `pytest` check passing, and no high/critical CodeQL alerts. Approvals are set to 0 because you're a solo account and can't approve your own PR.

🔍 If import errors on a rule, create the ruleset by hand with the same rules, and note what failed in your rehearsal log.

## 4. Copilot in VS Code
```powershell
code .
```
Copilot automatically applies the custom instructions in `.github/copilot-instructions.md` in this workspace. 📄

Check your Copilot plan/allowance at github.com → Settings → Copilot. Rehearse the live prompt **sparingly**.

## 5. Stage the demo PR
From the repo folder:
```powershell
.\scripts\reset-demo.ps1
```
If PowerShell says running scripts is disabled:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\reset-demo.ps1
```
Wait ~3 minutes, then open the PR: Tests should be green, CodeQL should fail with a **SQL injection** alert, and Copilot Autofix should offer a fix.

**Manual alternative:** create branch `demo/claims-search`, replace `app\claims.py` with `demo\payloads\claims_with_search.py`, commit, push, and open a PR titled "Small, harmless change".

## 6. Run the app locally (optional)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1        # if blocked: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
pip install -r requirements.txt
pytest -q
flask --app app run                 # then open http://127.0.0.1:5000/health
```

## 7. Rehearsal checklist
- [ ] Full run under 7 minutes, twice
- [ ] Record a backup video of a clean run (Win + Alt + R with Xbox Game Bar, or Snipping Tool's screen recorder)
- [ ] Flip legend tags in README/docs from 📄 to ✅ for what you've personally verified
- [ ] Run `.\scripts\reset-demo.ps1` the morning of the interview

---

**macOS/Linux:** same steps, using `unzip`, `./scripts/reset-demo.sh`, `python3 -m venv .venv && source .venv/bin/activate`, and `brew install gh` for the GitHub CLI.
