from __future__ import annotations

import os

from dotenv import load_dotenv

DEFAULT_MODEL = "anthropic:claude-sonnet-4-6"


def get_model_name() -> str:
    load_dotenv()
    return os.getenv("PYDANTIC_AI_MODEL", DEFAULT_MODEL)
