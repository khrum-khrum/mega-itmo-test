# Run the same lint checks as CI (requires: pip install ruff or pip install -e ".[dev]")
.PHONY: lint format install test run build

install:
	pip install -r requirements.txt

lint:
	ruff check .
	ruff format --check .

# Auto-fix lint and format
format:
	ruff check . --fix
	ruff format .

test:
	pytest

run:
	uvicorn main:app --reload

build: install
