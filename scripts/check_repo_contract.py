from pathlib import Path
import sys

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "REQUIREMENTS.md",
    "SPEC.md",
    "ARQUITECTURE.md",
    "TASKS.md",
    "docs/traceability.md",
    "pyproject.toml",
]

missing = [path for path in REQUIRED_FILES if not Path(path).is_file()]

if missing:
    print("REPO_CONTRACT: FAIL")
    for path in missing:
        print(f"Missing: {path}")
    sys.exit(1)

print("REPO_CONTRACT: PASS")
sys.exit(0)
