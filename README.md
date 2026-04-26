# pyd-app

A minimal Pydantic AI application scaffold managed with `uv`.

## Setup

```sh
uv sync
cp .env.example .env
```

Add an API key to `.env` for the provider selected by `PYDANTIC_AI_MODEL`.

## Run

```sh
uv run python -m pyd_app
```

## Test

```sh
uv run pytest
uv run ruff check .
uv run ruff format .
uv run pyright
```
