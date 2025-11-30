install:
	uv sync

check:
	uv run ruff check

fix:
	uv run ruff check --fix

test:
	uv run pytest

coverage:
	uv run pytest --cov