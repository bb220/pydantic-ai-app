# pyd-app

A minimal Pydantic AI application scaffold managed with `uv`.

## Setup

```sh
uv sync
cp .env.example .env
```

Add an API key to `.env` for the provider selected by `PYDANTIC_AI_MODEL`.

## Logfire

The app instruments Pydantic AI with Pydantic Logfire when it runs. For local
development, authenticate and select a project:

```sh
uv run logfire auth
uv run logfire projects new
# or: uv run logfire projects use
```

For non-interactive environments, set `LOGFIRE_TOKEN` in `.env` instead. The app
uses `send_to_logfire="if-token-present"`, so it runs without sending traces
until a Logfire token or local project config exists.

## Run

```sh
uv run python -m pyd_app
```

## Test

```sh
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run pyright
```
