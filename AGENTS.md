# AGENTS.md

## Read First

Before making any changes, read these documents in order:

1. `REQUIREMENTS.md` — authoritative business and functional requirements.
2. `SPEC.md` — verifiable behavior and acceptance criteria.
3. `ARQUITECTURE.md` — system architecture, component responsibilities, and boundaries.
4. `TASKS.md` — task scope, implementation steps, and expected deliverables.
5. `docs/REPO_MAP.md` — repository structure and navigation, **if this file exists**.

Also inspect `README.md` for installation, execution, and testing instructions. Review relevant tests and implementation files before editing them.

If a required document is missing, contradictory, or insufficient to define the requested behavior, stop and request human clarification instead of inventing instructions.

## Sources of Truth

- `REQUIREMENTS.md` is the source of truth for business and functional requirements.
- `SPEC.md` defines expected, verifiable system behavior and acceptance criteria.
- `ARQUITECTURE.md` defines architectural responsibilities, component boundaries, and data flow.
- `TASKS.md` defines the authorized task scope and planned work.
- Automated tests provide evidence of implemented behavior; they do not override documented requirements or specifications.
- `README.md` documents user-facing usage and operational commands.
- `docs/traceability.md`, when present, links requirements, specifications, implementation tasks, and tests.

When sources conflict, do not silently choose one or modify a requirement to make the implementation or tests pass. Identify the conflict and request a human decision.

## Repository Map

- `src/customer_search/` — application source code.
  - `cli.py` — command-line parsing, output formatting, and exit codes.
  - `service.py` — query validation and customer search business logic.
  - `storage.py` — JSON file access, parsing, and storage error handling.
- `tests/` — automated tests for application behavior.
- `docs/` — supporting documentation and traceability, where present.
- `results/` — result or evidence artifacts; inspect existing files before changing anything.
- `REQUIREMENTS.md` — functional and business requirements.
- `SPEC.md` — behavioral specification.
- `ARQUITECTURE.md` — architecture documentation.
- `TASKS.md` — task definitions and implementation guidance.
- `TASK_UNDER_TEST.md` — task-specific testing context, when relevant.
- `customers.json` — sample customer dataset.
- `pyproject.toml` — Python package metadata and pytest configuration.
- `README.md` — installation, usage, and testing instructions.
- `AI-USAGE-LOG.md` — AI usage records, if the task requires updating them.
- `AGENTS.md` — instructions for coding agents.

This map reflects the repository structure observed during the audit. Do not assume that optional files, directories, or scripts exist without checking them.

## Standard Commands

Run commands from the repository root using Python 3.11 or newer.

### Installation

Install the package in editable mode:

    python -m pip install -e .

Install pytest if it is not already available:

    python -m pip install pytest

Do not install additional packages without a clear justification and authorization when required.

### Execution

Search for a customer by name or email:

    python -m customer_search "smith"

Use a named query:

    python -m customer_search --query "jane"

Use a custom dataset:

    python -m customer_search --file path/to/customers.json "smith"

Use the commands documented in `README.md` when other supported options are needed.

### Testing

Run the complete test suite:

    python -m pytest -v

Run a specific test module when relevant:

    python -m pytest tests/test_service.py -v

    python -m pytest tests/test_storage.py -v

    python -m pytest tests/test_cli.py -v

Run the baseline suite before implementation and again after changes. Add or update tests for new or modified behavior without weakening existing assertions.

### Linting
Install Ruff:
    python -m pip install ruff

Run lint checks without modifying files:
    python -m ruff check .

Lint the application and tests only:
    python -m ruff check src tests

Do not automatically fix lint violations. Review each finding and make only task-related changes. Report lint failures separately from test failures.

### Validation

The required validation command is:

```bash
bash scripts/verify_repo.sh
```

Before declaring a task `DONE`:
1. Run the verification script from the repository root.
2. Confirm that all checks pass and the command exits successfully.
3. Review the output and report the actual results. Do not claim successful verification if any check fails or cannot run.
4. If the script is missing or its checks are incompatible with the environment, report the limitation and run the documented pytest suite with `python -m pytest -v` when possible.
5. Execute additional checks only when they are supported by the repository and relevant to the task.

Passing verification does not replace reviewing the applicable requirements, acceptance criteria, and documentation. Report any remaining limitations before declaring `DONE`.

## Change Rules

### Allowed

- Modify implementation files under `src/customer_search/` when required by the authorized task.
- Add or update relevant tests under `tests/`.
- Update documentation when necessary to reflect approved behavior.
- Make small, focused changes that preserve the existing architecture.
- Add justified error handling and edge-case coverage consistent with the specification.

### Not allowed without explicit authorization

- Modify `REQUIREMENTS.md` or `SPEC.md` to make an implementation or test pass.
- Delete, skip, weaken, or rewrite existing tests merely to obtain a passing result.
- Change architectural boundaries or component responsibilities without human approval.
- Add dependencies without justification and any required approval.
- Modify secrets, credentials, or environment-specific configuration unnecessarily.
- Hand-edit generated files or overwrite existing evidence without determining how it is produced and whether the task permits the change.
- Perform destructive operations, unrelated refactoring, or broad formatting changes outside the requested scope.
- Claim that commands passed when they were not executed or their results are unknown.

Preserve existing user changes. Before editing, inspect the Git working tree and avoid overwriting uncommitted work.

## Stop Conditions

Stop work and request a human decision when:

- Requirements, specifications, acceptance criteria, or task instructions conflict.
- A required document is missing and its contents are necessary to proceed safely.
- The requested change requires modifying protected requirements or specifications.
- An architectural boundary, public interface, or data contract must change beyond the authorized scope.
- A destructive or irreversible action is required.
- A new dependency, security-sensitive change, or external-system interaction requires approval.
- Required credentials, permissions, external services, or test infrastructure are unavailable.
- Existing tests fail for reasons that cannot be confidently attributed to the requested change.
- The correct behavior cannot be determined from the available evidence.

When stopping, report the issue, the evidence gathered, the decision needed, and any safe work completed. Do not guess or silently bypass the blocker.

## Definition of Done

A task is complete only when all applicable conditions are satisfied:

1. The implementation matches `REQUIREMENTS.md` and `SPEC.md`.
2. Relevant acceptance criteria are covered by implementation and tests.
3. The existing architecture and component boundaries remain intact unless an approved change states otherwise.
4. Relevant tests have been executed, and their actual results are reported.
5. New behavior has appropriate regression and edge-case coverage.
6. Applicable validation and lint checks have been run when available; unavailable checks are explicitly disclosed.
7. Documentation reflects approved behavior and remains consistent with the implementation.
8. No unrelated files, protected files, or generated evidence have been changed without authorization.
9. The final report identifies changed files, commands executed, test and validation results, unresolved issues, and any required human decisions.

Never report full completion when required checks remain unexecuted or acceptance criteria remain unverified. Distinguish passing checks from skipped, unavailable, and failing checks.