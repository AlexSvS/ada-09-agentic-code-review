# Repository Map
## Entry Points
- src/customer_search/__main__.py — enables running the package with python -m customer_search.
- src/customer_search/cli.py — CLI arguments, output formatting, error messages, and exit codes.
- src/customer_search/service.py — search behavior and query validation.
- src/customer_search/models.py — Customer domain model.
- src/customer_search/storage.py — local JSON loading, validation, and saving.
- customers.json — default local customer dataset.

## Tests
- tests/test_cli.py — command-line arguments, output, errors, and exit codes.
- tests/test_service.py — search and business logic.
- tests/test_storage.py — JSON persistence and invalid/missing data.
- tests/test_setup.py — package/setup checks.
- tests/conftest.py — shared pytest fixtures.

## Change Guide
If changing CLI arguments or user-visible output:
1. Check REQUIREMENTS.md and SPEC.md.
2. Update src/customer_search/cli.py.
3. Update or add tests in tests/test_cli.py.

If changing search or validation behavior:
1. Check REQUIREMENTS.md, SPEC.md, and ARQUITECTURE.md.
2. Update src/customer_search/service.py (and models.py only if the domain model changes).
3. Update or add tests in tests/test_service.py; check CLI tests if behavior is exposed to users.
4. Review docs/traceability.md and TASKS.md if acceptance criteria or coverage change.

If changing JSON format, file handling, or persistence:
1. Check SPEC.md and ARQUITECTURE.md.
2. Update src/customer_search/storage.py.
3. Update or add tests in tests/test_storage.py; check CLI error handling if error behavior changes.

If changing package setup or test configuration:
1. Check pyproject.toml and tests/test_setup.py.
2. Verify with python -m pytest -v.

## Do Not Edit Directly
- src/customer_search/__pycache__/, tests/__pycache__/ — generated Python bytecode; do not hand-edit.
- .env or other local secrets/configuration, if introduced — do not commit secrets.
- Do not weaken or delete tests, or change REQUIREMENTS.md / SPEC.md merely to make an implementation pass. Follow AGENTS.md.