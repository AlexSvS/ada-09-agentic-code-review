#!/usr/bin/env bash
set -euo pipefail

echo "[1/3] Running test suite"
python -m pytest -q

echo "[2/3] Running Ruff lint checks"
python -m ruff check src tests

echo "[3/3] Checking CLI smoke test"
output="$(PYTHONPATH=src python -m customer_search "smith")"
grep -qi "smith" <<< "$output"

echo "VERIFY_REPO: PASS"