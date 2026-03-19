.PHONY: generate install test lint fmt typecheck docs clean help

PYTHON ?= python3.10

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

generate:  ## Regenerate client code from OpenAPI specs
	bash generate.sh

install:  ## Install the package in editable mode with dev extras
	$(PYTHON) -m pip install -e ".[dev]"

test:  ## Run tests
	pytest tests/ -v --tb=short

lint:  ## Check code formatting (black --check)
	black --check src/kb_cloud_client/*.py tests/ examples/

fmt:  ## Auto-format code with black
	black src/kb_cloud_client/*.py tests/ examples/

typecheck:  ## Run mypy type checks
	mypy src/kb_cloud_client/ --ignore-missing-imports

docs:  ## Build API reference docs locally (open site/kb_cloud_client/index.html)
	pdoc --output-directory site --no-show-source kb_cloud_client
	@echo "Docs built → open site/kb_cloud_client/index.html"

clean:  ## Remove build artifacts and caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info/ src/*.egg-info/ .mypy_cache/ .pytest_cache/ htmlcov/ .coverage site/
