# Run the same lint checks as CI (requires: pip install ruff or pip install -e ".[dev]")
.PHONY: lint format
lint:
	ruff check .
	ruff format --check .

# Auto-fix lint and format
format:
	ruff check . --fix
	ruff format .
