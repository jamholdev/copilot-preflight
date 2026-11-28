# Copilot Custom Instructions for ClaimsBot

## About this repository
ClaimsBot is a small Flask API for looking up insurance claims. All data is synthetic. Python 3.12. Run the tests with `pytest -q` from the repository root.

## Protected data (always follow)
1. **PHI (protected health information) and PII (personally identifiable information) never go in code, logs, comments, prompts, test fixtures, or commit messages.**
2. See rule 1.
3. Never hardcode secrets, tokens, or connection strings. Read them from environment variables.

Examples of PHI and PII: names, dates of birth, addresses, phone numbers, email addresses, Social Security numbers, real member IDs, diagnoses, and claim notes about a real person.

- Use only the synthetic records in `app/db.py` (member IDs start with `SYN-`).
- Never generate realistic personal data, even as an example. Use obvious placeholders such as `SYN-1001`.
- If a task seems to need real patient or personal data, stop and say so instead of writing code.

## Coding rules
- **SQL:** always use parameterized queries (`?` placeholders). Never build SQL with f-strings, `%`, `+`, or `.format()`.
- **Input:** treat every `request.args`, `request.form`, and path parameter as untrusted.
- **Errors:** return generic error messages; never echo raw input or stack traces to the client.
- **Logging:** log claim IDs only, never member identifiers, amounts, or request parameters.
- **Tests:** every new endpoint gets a pytest test in `tests/`, including one negative or injection case.

## Style
- Flask blueprints, small functions, type hints welcome.
- Match the existing patterns in `app/claims.py`.

## When unsure
Say so in the pull request description and flag it for human review.
