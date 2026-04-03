# CLAUDE.md

## ⚠️ Never run python, pytest or ruff directly in local — always via Docker

## Initial setup

```bash
docker compose build   # first time, or after changing pyproject.toml
docker compose up      # starts the server with hot-reload
```
## Run tests
```
docker compose run --rm app uv run pytest
```

## Structure
```
src/app/main.py   # FastAPI app (in-memory tasks CRUD)
tests/            # pytest + httpx TestClient
```

## Adding dependencies
- use uv
