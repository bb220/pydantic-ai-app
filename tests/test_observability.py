from __future__ import annotations

from pyd_app import observability


def test_setup_logfire_configures_once(monkeypatch) -> None:
    configure_calls: list[dict[str, object]] = []
    instrument_calls = 0

    def fake_configure(**kwargs: object) -> None:
        configure_calls.append(kwargs)

    def fake_instrument_pydantic_ai() -> None:
        nonlocal instrument_calls
        instrument_calls += 1

    monkeypatch.setattr(observability, "_LOGFIRE_CONFIGURED", False)
    monkeypatch.setattr(observability.logfire, "configure", fake_configure)
    monkeypatch.setattr(
        observability.logfire,
        "instrument_pydantic_ai",
        fake_instrument_pydantic_ai,
    )

    observability.setup_logfire()
    observability.setup_logfire()

    assert configure_calls == [
        {"send_to_logfire": "if-token-present", "service_name": "pyd-app"}
    ]
    assert instrument_calls == 1
