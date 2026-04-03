#!/bin/bash
set -e

echo ">>> Lint"
uv run ruff check src/

echo ">>> Tests"
uv run pytest --cov=src --cov-report=term-missing -v
