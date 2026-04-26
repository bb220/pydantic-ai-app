from __future__ import annotations

from pyd_app.assistant import create_assistant_agent


def test_assistant_registers_calendar_tools() -> None:
    agent = create_assistant_agent("test")

    assert set(agent._function_toolset.tools) == {
        "create_calendar_event",
        "fetch_calendar_events",
    }
