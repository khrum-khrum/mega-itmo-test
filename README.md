# mega-itmo-test
Тестовый репозиторий для проверки Агента

## Getting Started

First, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then, install the development dependencies:

```bash
pip install -e ".[dev]"
```

## Makefile Commands

This project uses a `Makefile` to streamline common development tasks.

- **`make lint`**: Runs lint checks using `ruff` (same as CI).

  ```bash
  make lint
  ```

- **`make format`**: Auto-fixes linting and formatting issues using `ruff`.

  ```bash
  make format
  ```

- **`make test`**: Runs all tests using `pytest`.

  ```bash
  make test
  ```

- **`make run`**: Starts the FastAPI application using `uvicorn`.

  ```bash
  make run
  ```

- **`make build`**: Installs project dependencies from `requirements.txt`.

  ```bash
  make build
  ```
