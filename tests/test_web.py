from __future__ import annotations

from starlette.applications import Starlette

from pyd_app.assistant import create_assistant_agent
from pyd_app import web


def test_create_app_returns_starlette_app(monkeypatch) -> None:
    setup_calls = 0

    def fake_setup_logfire() -> None:
        nonlocal setup_calls
        setup_calls += 1

    monkeypatch.setattr(web, "setup_logfire", fake_setup_logfire)
    monkeypatch.setattr(web, "create_assistant_agent", lambda: create_test_agent())

    app = web.create_app()

    assert isinstance(app, Starlette)
    assert setup_calls == 1


def create_test_agent():
    return create_assistant_agent("test")
