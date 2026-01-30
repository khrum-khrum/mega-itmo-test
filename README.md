# mega-itmo-test
Тестовый репозиторий для проверки Агента

## Setup

First, create a virtual environment and install dependencies:

```bash
python3 -m venv .venv && source .venv/bin/activate
make install
```

## Linting and Formatting

To check linting and formatting (same as CI):

```bash
make lint
```

To auto-fix linting and formatting issues:

```bash
make format
```

## Testing

To run tests:

```bash
make test
```

## Running the Application

To run the application locally:

```bash
make run
```

## Building

To build the project (installs dependencies):

```bash
make build
```
