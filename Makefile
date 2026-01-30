# Run the same lint checks as CI (requires: pip install ruff or pip install -e ".[dev]")
.PHONY: lint format test build run

lint:
	ruff check .
	ruff format --check .

# Auto-fix lint and format
format:
	ruff check . --fix
	ruff format .

test:
	pytest

build:
	pip install -r requirements.txt

run:
	uvicorn main:app --host 0.0.0.0 --port 8000
