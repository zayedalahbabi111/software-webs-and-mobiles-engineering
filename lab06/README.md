# Lab 06: Late fee checks

The campus library charges a fee when a laptop comes back late. A teammate's coding
agent wrote `late_fee` in `fees.py`. In Terminal, you set up the Codex of the ChatGPT
desktop app with project rules and two personas, each with limits that Codex enforces: a
tester that writes tests from `REQUIREMENTS.md` and cannot see `fees.py`, and a reviewer
that reads `fees.py` against `REQUIREMENTS.md` and changes nothing.

## Files

- `REQUIREMENTS.md`: acceptance criteria; unchanged.
- `fees.py`: teammate code; unchanged.
- `AGENTS.md`: project-wide agent rules.
- `.codex/agents/tester.toml`: tester persona.
- `.codex/agents/reviewer.toml`: reviewer persona.
- `.codex/config.toml`: enforced permission profiles.
- `tests/test_fees.py`: requirement-derived unittest examples.
- `evidence/sandbox-checks.txt`: local sandbox evidence.
- `DECISION.md`: acceptance decision and evidence.

Run tests from `lab06` with:

`python3 -m unittest discover -s tests`
