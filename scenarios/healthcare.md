# Scenario: Health Company Inc.

**Regional health insurer · ~400 developers · Java/.NET/Python · GitHub Enterprise Cloud (assumed, to confirm)**

## The situation
- The board wants "AI productivity" this fiscal year.
- A 50-seat Copilot pilot launched six months ago. Usage is patchy, and nobody can say whether it worked.
- The CISO has paused expansion: worried about PHI exposure and AI writing insecure code.

## Stakeholders
| Persona | Wants | Fears | What wins them |
|---|---|---|---|
| **VP Engineering** | Ship faster, retain developers | Another tool nobody uses | Cycle-time data from *her* teams |
| **CISO** | No headlines, clean audits | AI as a new breach path | Guardrails enforced by the platform, audit evidence |
| **CFO** | Return on spend | Paying for shelfware | Baseline vs. day-90 numbers, a go/no-go gate |

## Objective
Move from a stalled pilot to **safe, measured scale**: 2 volunteer teams → 1 business unit → org-wide, gated by agreed metrics.

## Discovery questions
**Platform**
1. Are you on GHEC, GHE.com (data residency), or GHES?
2. Which repos could ever contain PHI or production data extracts?

**Compliance**
3. Does policy require a BAA from every vendor that touches source code, or only those touching PHI?
4. Which frameworks are in scope for the SDLC: HIPAA, SOC 2, HITRUST, state regs?
5. Who signs off on new AI tooling: security, legal, an AI governance board?

**Value**
6. Do you have baseline data for PR cycle time, lead time, change failure rate?
7. What would "worth it" look like to the CFO at day 90?

**Adoption**
8. Why did the first pilot stall: access, training, trust, or no one owning it?
9. Who are your natural champions?

## Recommendation (summary)
**Phased rollout with guardrails first.** Turn on CodeQL + Autofix, rulesets, secret scanning, content exclusion, and Copilot instructions *before* expanding seats. Two volunteer teams, baseline captured, day-90 EBR decides the next phase.

**Alternatives considered**
- *Ban AI tools* → developers use shadow AI anyway; zero visibility.
- *Big-bang licensing* → seat-count vanity metric, CISO revolts, no proof of value.

**Trade-off:** slower in month one so you can go faster in month six.
