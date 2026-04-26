from __future__ import annotations

from pydantic_ai import Agent, Tool
from pydantic_ai.models import Model

from pyd_app.calendar_tools import create_calendar_event, fetch_calendar_events
from pyd_app.config import get_model_name

ASSISTANT_INSTRUCTIONS = """
You are a helpful personal assistant. Be concise, practical, and friendly.
Use the calendar tools for scheduling questions, availability checks, and event
creation. The calendar fetch tool returns the user's upcoming mocked calendar.
When the user asks to schedule something but omits required details like title,
start time, end time, or date, ask a clarifying question before creating an
event. Treat all calendar tool responses as mocked data for now.
"""


def create_assistant_agent(model: Model | str | None = None) -> Agent[None, str]:
    return Agent(
        model or get_model_name(),
        instructions=ASSISTANT_INSTRUCTIONS,
        tools=[
            Tool(fetch_calendar_events),
            Tool(create_calendar_event),
        ],
    )
