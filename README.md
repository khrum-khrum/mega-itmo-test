# mega-itmo-test
Тестовый репозиторий для проверки Агента

## Development

### Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Linting and Formatting

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
