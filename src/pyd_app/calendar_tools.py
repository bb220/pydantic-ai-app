from __future__ import annotations

from hashlib import sha1

from pydantic import BaseModel, Field


class CalendarEvent(BaseModel):
    id: str
    title: str
    start: str
    end: str
    attendees: list[str] = Field(default_factory=list)
    location: str | None = None
    notes: str | None = None


MOCK_EVENTS = [
    CalendarEvent(
        id="evt_20260427_0900",
        title="Product strategy sync",
        start="2026-04-27T09:00:00-04:00",
        end="2026-04-27T09:45:00-04:00",
        attendees=["alex@example.com", "morgan@example.com"],
        location="Zoom",
        notes="Review roadmap priorities and launch sequencing.",
    ),
    CalendarEvent(
        id="evt_20260427_1330",
        title="Design review",
        start="2026-04-27T13:30:00-04:00",
        end="2026-04-27T14:15:00-04:00",
        attendees=["jamie@example.com"],
        location="Studio 3",
        notes="Finalize dashboard interaction states.",
    ),
    CalendarEvent(
        id="evt_20260428_1100",
        title="Dentist appointment",
        start="2026-04-28T11:00:00-04:00",
        end="2026-04-28T12:00:00-04:00",
        location="Downtown Dental",
    ),
    CalendarEvent(
        id="evt_20260429_1600",
        title="Coffee with Priya",
        start="2026-04-29T16:00:00-04:00",
        end="2026-04-29T16:45:00-04:00",
        attendees=["priya@example.com"],
        location="Blue Bottle",
    ),
]


def fetch_calendar_events() -> list[CalendarEvent]:
    """Fetch the user's upcoming calendar events."""
    return MOCK_EVENTS


def create_calendar_event(
    title: str,
    start: str,
    end: str,
    attendees: list[str] | None = None,
    location: str | None = None,
) -> CalendarEvent:
    """Create a calendar event and return the mocked saved event."""
    event_id = sha1(f"{title}:{start}:{end}".encode()).hexdigest()[:10]

    return CalendarEvent(
        id=f"evt_mock_{event_id}",
        title=title,
        start=start,
        end=end,
        attendees=attendees or [],
        location=location,
        notes="Mock event created by the personal assistant.",
    )
