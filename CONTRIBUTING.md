# Contributing

Thank you for your interest in contributing to `kb-cloud-client-python`!

## Development setup

```bash
# Clone the repository
git clone https://github.com/apecloud/kb-cloud-client-python.git
cd kb-cloud-client-python

# Install the package in editable mode with dev extras
python3.10 -m pip install -e ".[dev]"
```

## Regenerating the client

The code under `src/kb_cloud_client/kbcloud/` is **auto-generated**. Do not edit
it directly. Instead, update the OpenAPI schemas in `.generator/schemas/` or the
Jinja2 templates in `.generator/src/generator/templates/`, then regenerate:

```bash
./generate.sh
```

Generator dependencies are installed automatically by the script.

## Running tests

```bash
pytest tests/
```

## Code style

This project uses [Black](https://black.readthedocs.io/) for formatting and
[mypy](https://mypy.readthedocs.io/) for type checking:

```bash
black src/ tests/ examples/
mypy src/
```

## Pull requests

1. Fork the repository and create a feature branch.
2. Run the linter and tests before opening a PR.
3. Keep commits focused; one logical change per commit.
4. PR titles follow the `chore:` / `feat:` / `fix:` convention.

## Reporting issues

Please open a GitHub issue with a minimal reproducible example. Include the
client version (`import kb_cloud_client; print(kb_cloud_client.__version__)`
once versioning is wired up) and the Python version.
