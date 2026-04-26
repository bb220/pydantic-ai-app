from __future__ import annotations

from pyd_app.calendar_tools import create_calendar_event, fetch_calendar_events


def test_fetch_calendar_events_returns_upcoming_events() -> None:
    events = fetch_calendar_events()

    assert [event.title for event in events] == [
        "Product strategy sync",
        "Design review",
        "Dentist appointment",
        "Coffee with Priya",
    ]


def test_create_calendar_event_returns_mock_event() -> None:
    event = create_calendar_event(
        title="Lunch with Sam",
        start="2026-05-01T12:00:00-04:00",
        end="2026-05-01T13:00:00-04:00",
        attendees=["sam@example.com"],
        location="The Market",
    )

    assert event.id.startswith("evt_mock_")
    assert event.title == "Lunch with Sam"
    assert event.attendees == ["sam@example.com"]
    assert event.location == "The Market"
    assert event.notes == "Mock event created by the personal assistant."
