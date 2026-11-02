# Human Review Decisions
## Change
CR-001
### RF-01
Reviewer severity: MUST FIX
Human decision: REJECTED
Reason: The `results/verification-report.md` doesn't falsely assert that `bash scripts/verify_repo.sh` passed and returned `VERIFY_REPO: PASS`. It was made by a human with a computer, not an AI agent without bash permission.
Required action: None

### RF-02
Reviewer severity: SHOULD FIX
Human decision: MODIFIED
Reason: The pull request has three binary `.pyc` files committed that must be ignored. 
Final severity: MUST FIX
Required action: Untrack all `.pyc` files from git (`git rm -r --cached */__pycache__`), add a standard `.gitignore` file ignoring `__pycache__/`, `*.pyc`, `.pytest_cache/`, and `.ruff_cache/`, and commit the cleanup.

### RF-03
Reviewer severity: SHOULD FIX
Human decision: ACCEPTED
Reason: There are no automated tests in `tests/test_cli.py` or `tests/test_service.py` asserting that queries with leading/trailing whitespace that match records (e.g. `main(["  smith  "])` or `main(["--query", "  jane  "])`) return the expected records and exit with code 0.
Final severity: SHOULD FIX
Required action: Add automated tests in `tests/test_cli.py` verifying that matching queries with leading and trailing whitespace (e.g., `main(["  smith  "])` and `main(["--query", "  smith  "])`) return the expected customer records and exit with code 0.

### RF-04
Reviewer severity: OPTIONAL
Human decision: REJECTED
Reason: Not necessary for this pull request.

### RF-05
Reviewer severity: OPTIONAL
Human decision: REJECTED
Reason: The AI-USAGE-LOG.md is not part of the review.

## Human Gate
[x] Return to coder-agent
[ ] Ready for final re-review
[ ] Stop / escalate
