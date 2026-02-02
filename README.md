# mega-itmo-test

This repository serves as a testbed for evaluating the capabilities of an AI agent. It contains a simple Python application with basic development tools configured.

## Project Structure

- `main.py`: The main application file.
- `test_main.py`: Unit tests for the `main.py` application.
- `requirements.txt`: Python dependencies.
- `pyproject.toml`: Project configuration, including `ruff` for linting and formatting.
- `Makefile`: Contains commands for common development tasks.

## Development

### Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Linting and Formatting

This project uses `ruff` for code linting and formatting.

```bash
make lint                  # ruff check + ruff format --check
make format                # auto-fix
```

### Testing

```bash
make test
```

### Running the Application

```bash
make run
```
