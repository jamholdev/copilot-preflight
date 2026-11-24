# Copilot Custom Instructions for ClaimsBot

These rules apply to every suggestion and change in this repository.

## Protected data (non-negotiable)
1. **Patient data never goes in code, logs, comments, prompts, or test fixtures.** Use the synthetic records in `app/db.py` (member IDs start with `SYN-`).
2. See rule 1.
3. Never hardcode secrets, tokens, or connection strings. Read them from environment variables.

## Coding rules for this codebase
- **SQL:** always use parameterized queries (`?` placeholders). Never build SQL with f-strings, `%`, `+`, or `.format()`.
- **Input:** treat every `request.args`, `request.form`, and path parameter as untrusted.
- **Errors:** return generic error messages; never echo raw input or stack traces to the client.
- **Logging:** log claim IDs only, never member identifiers or amounts.
- **Tests:** every new endpoint gets a pytest test in `tests/`, including one negative/injection case.

## Style
- Python 3.12, Flask blueprints, small functions, type hints welcome.
- Match the existing patterns in `app/claims.py`.

## When unsure
Say so in the PR description and flag it for human review.
