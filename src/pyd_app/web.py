from __future__ import annotations

from starlette.applications import Starlette

from pyd_app.assistant import create_assistant_agent
from pyd_app.observability import setup_logfire


def create_app() -> Starlette:
    setup_logfire()
    agent = create_assistant_agent()
    return agent.to_web()
