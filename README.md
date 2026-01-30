# mega-itmo-test
Тестовый репозиторий для проверки Агента

## Lint locally (same as CI)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"   # or: pip install ruff
make lint                  # ruff check + ruff format --check
make format                # auto-fix
```
