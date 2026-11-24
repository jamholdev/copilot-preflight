# Risk Register

> **Framing:** HIPAA compliance isn't a property of a tool. It depends on how PHI flows. Our design goal is that **PHI never enters the software development lifecycle**: not in code, prompts, test data, or logs. The contract questions below still need answers, but they're questions for counsel, not blockers to a well-designed pilot.
>
> *Not legal advice. This is how I'd structure the conversation with the customer's counsel and GitHub's legal/trust teams.*

Legend: ✅ tested · 📄 documented · 🔍 validate with customer / legal

---

## R1: BAA coverage for GitHub and Copilot
| | |
|---|---|
| **Risk** | Customer's compliance policy may require a signed Business Associate Agreement from any vendor that could receive PHI. |
| **What we know** | Public third-party analyses conflict on whether a BAA is available for GitHub Enterprise Cloud / Copilot, and some report that GitHub's DPA restricts submitting PHI without GitHub's prior written consent. GitHub does not appear to publish a HIPAA/BAA page of its own. |
| **Status** | 🔍 Validate with GitHub legal/trust team and the customer's counsel. Do **not** state a position as fact. |
| **Mitigation** | Design PHI out of the SDLC (see controls below) so the pilot can proceed on non-PHI repos while the contract question is resolved. |
| **Discovery question** | "Does your policy require a BAA from every vendor that touches source code, or only vendors that touch PHI?" |

## R2: Customer is on GitHub Enterprise Server (GHES)
| | |
|---|---|
| **Risk** | Copilot is delivered from GitHub's cloud platforms (GitHub.com / GHE.com); most features require a cloud presence. |
| **What we know** | 📄 A GitHub Enterprise license includes an enterprise account on GitHub.com or GHE.com, enabling a hybrid model. 🔍 Recent Copilot app support for GHES accounts (reported Nov 2026); confirm on the GitHub changelog before citing. |
| **Pivot** | Hybrid: code stays on GHES; Copilot licensing and policy run from the cloud enterprise account. Validate which features work in that topology. |
| **Discovery question** | "Are you on GHEC, GHE.com, or GHES today, and is moving any repos to cloud on the table?" |

## R3: Data residency / sovereignty
| | |
|---|---|
| **Risk** | Policy requires code and prompts to stay in-country. |
| **What we know** | 📄 GHE.com with data residency can route Copilot inference to in-region model endpoints; admins can restrict to data-resident or FedRAMP-compliant models via policy. |
| **Pivot** | Recommend GHE.com (US region) + "restrict to data-residency-compliant models" policy. Note: some features may differ on GHE.com, so check the feature overview. |

## R4: AI-generated code introduces vulnerabilities
| | |
|---|---|
| **Risk** | Faster code, faster bugs. |
| **Mitigation** | ✅/📄 CodeQL on every PR + Copilot Autofix + ruleset requiring a clean scan. (Mark ✅ after rehearsal.) Track "vulns introduced per PR" in the scorecard. |

## R5: Secrets or PHI committed to repos
| | |
|---|---|
| **Mitigation** | 📄 Secret scanning + push protection; 🔍 custom patterns for member-ID / record formats; 📄 Copilot content exclusion for sensitive paths (Business/Enterprise). |

## R6: Adoption stalls (pilot purgatory)
| | |
|---|---|
| **Risk** | Licenses bought, nobody uses them, no one can prove value. |
| **Mitigation** | Volunteer pilot teams, named champions, baseline metrics before go-live, day-90 EBR with go/no-go criteria. See `pilot-scorecard.md`. |

---

## Controls that keep PHI out of the development workflow
1. Synthetic / de-identified test data only (enforced by convention + review)
2. Copilot custom instructions (`.github/copilot-instructions.md`) protected-data rules
3. Secret scanning push protection (+ custom patterns)
4. Copilot content exclusion for sensitive directories
5. Audit log streaming to the customer's SIEM
6. Data residency / FedRAMP model policy where required

## Sources to re-check before presenting
- GitHub Docs: About Copilot on GHES; Copilot with data residency; Copilot plans
- GitHub changelog: Copilot data residency + FedRAMP (Apr 2026); Copilot app GHES support (Nov 2026)
- GitHub customer terms: Data Protection Agreement
- Microsoft HIPAA/HITECH offering page (in-scope services list)
