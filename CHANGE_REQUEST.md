# Change Request

**Change ID:** CR-001

## Goal

Fix inconsistent query formatting in the CLI's no-results notification.

Currently, the Customer Service normalizes search queries using `strip().lower()`, but the CLI displays the original, untrimmed query when no customers are found.

For example:

```bash
python -m customer_search "  nonexistent  "
```

Currently produces:

```text
No customers found matching '  nonexistent  '
```

The change should ensure that leading and trailing whitespace is removed from the query displayed in the no-results notification, while preserving the existing case-insensitive search behavior.

Expected output:

```text
No customers found matching 'nonexistent'
```

The change should be limited to the CLI presentation layer and its corresponding tests.

## Requirements Covered

- FR-05
- AC-05

## Constraints

- Follow `AGENTS.md`.
- Use `REQUIREMENTS.md` and `SPEC.md` as the source of truth.
- Preserve architecture boundaries.
- Do not weaken existing tests.
- Do not modify the search algorithm or storage implementation.
- Preserve existing positional and `--query` argument compatibility.
- Do not introduce additional dependencies.
- Keep the existing exit code behavior unchanged.

## Verification

The change is considered complete when:

1. A search with a normal, unmatched query displays the expected no-results notification.
2. A search with leading and trailing whitespace displays the notification using the trimmed query.
3. Existing matching queries continue to return the same customer records.
4. The no-results scenario continues returning exit code `0`.
5. A new automated CLI test verifies the whitespace-trimming behavior.
6. All existing tests continue passing.
7. `python -m pytest -v` completes successfully.
8. `python -m ruff check src tests` reports no new lint violations.
9. `bash scripts/verify_repo.sh` completes successfully.

## Human Approval

**Approved to implement:** YES
**Approved by:** Alexandra Saavedra Sánchez
**Date:** 2026-11-01