# Run the same lint checks as CI (requires: pip install ruff or pip install -e ".[dev]")
.PHONY: lint format test build run install clean

install:
	pip install -r requirements.txt
	pip install ruff pytest

lint:
	ruff check .
	ruff format --check .

format:
	ruff check . --fix
	ruff format .

test:
	pytest

build: install

run:
	uvicorn main:app --host 0.0.0.0 --port 8000

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf .venv
