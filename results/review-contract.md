# Review Contract
## Change
CR-001 — Trim leading and trailing whitespace from the query displayed in the CLI no-results notification.

## Requirements / Acceptance Criteria
- FR-05
- AC-05

## Architecture Constraints
- Expected dependency flow:
    - CLI (cli.py) → Customer Service (service.py) → JSON Storage (storage.py).
    - The CLI is responsible for presentation and formatting user-facing messages.
    - The Customer Service owns search logic and query validation.
    - JSON Storage owns file access, JSON parsing, and record integrity.
    - No circular dependencies or unnecessary new dependencies.
- Business-rule location:
    - Search normalization and matching rules belong in CustomerService.
    - The CLI may normalize the query for presentation purposes.
    - The no-results notification formatting belongs in cli.py, specifically in main().
- Protected boundaries:
    - Do not move search logic into the CLI.
    - Do not modify the storage layer or domain model for this change.
    - Preserve the CustomerService.search(query) interface.
    - Preserve existing exception handling and exit-code behavior.
    - Maintain Python 3.11+ compatibility.
    - Preserve offline execution and the zero-external-runtime-dependency constraint.

## Review Rules
- Verify requirement coverage.
- Verify every called API/dependency exists.
- Check architecture boundaries.
- Inspect tests for masking / false confidence.
- Check regression behavior.
- Identify unnecessary technical debt.
- Cite evidence for every finding.

## Severity
MUST FIX:
Requirement violation, regression, security/integrity risk,
hallucinated API/dependency, broken architecture constraint,
or defect that makes the change unsafe to approve.

SHOULD FIX:
Significant maintainability, coverage, design, or clarity issue
that does not block the requested behavior.

OPTIONAL:
Non-blocking improvement outside the minimum acceptance threshold.