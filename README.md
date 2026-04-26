# pyd-app

A Pydantic AI personal assistant scaffold served through the built-in web chat UI.

## Setup

```sh
uv sync
cp .env.example .env
```

Add an API key to `.env` for the provider selected by `PYDANTIC_AI_MODEL`.

The assistant currently uses mocked calendar tools for fetching and creating
events. Conversation history is retained by the local web chat flow, but it is
not persisted to a database or across server restarts yet.

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

## Run Web UI

```sh
uv run uvicorn pyd_app.web:create_app --factory --host 127.0.0.1 --port 7932
```

## Test

```sh
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run pyright
```
