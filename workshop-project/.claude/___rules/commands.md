# Project commands (always run via Docker)

- Run single file:  `docker compose run --rm app uv run pytest tests/test_tasks.py`
- Lint:             `docker compose run --rm app uv run ruff check src/`
- Format:           `docker compose run --rm app uv run ruff format src/`
- Ready:            `docker compose run --rm app bash scripts/ready.sh`      
- Start server:     `docker compose up`
- Mutation testing: `docker compose run --rm app uv run mutmut run`
- Mutation browse:  `docker compose run --rm app uv run mutmut browse`
- Apply mutant:     `docker compose run --rm app uv run mutmut apply <mutant>`
