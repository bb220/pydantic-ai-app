from __future__ import annotations

from dotenv import load_dotenv

import logfire

_LOGFIRE_CONFIGURED = False


def setup_logfire() -> None:
    global _LOGFIRE_CONFIGURED

    if _LOGFIRE_CONFIGURED:
        return

    load_dotenv()
    logfire.configure(send_to_logfire="if-token-present", service_name="pyd-app")
    logfire.instrument_pydantic_ai()
    _LOGFIRE_CONFIGURED = True
