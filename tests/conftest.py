from __future__ import annotations

import os

import pydantic_ai.models

os.environ["LOGFIRE_SEND_TO_LOGFIRE"] = "false"
pydantic_ai.models.ALLOW_MODEL_REQUESTS = False
