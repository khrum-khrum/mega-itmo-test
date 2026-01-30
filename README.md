# mega-itmo-test
Тестовый репозиторий для проверки Агента

## Usage

First, install dependencies:

```bash
make install
```

### Linting

To check for linting issues (same as CI):

```bash
make lint
```

To auto-fix linting and formatting issues:

```bash
make format
```

### Testing

To run tests:

```bash
make test
```

### Running the application

To build (install dependencies) and run the application:

```bash
make build
make run
```

Alternatively, you can run directly after installing dependencies:

```bash
make install
python main.py
```

### Cleaning

To clean up temporary files and caches:

```bash
make clean
```
