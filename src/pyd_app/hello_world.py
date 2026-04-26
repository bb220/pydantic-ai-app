from __future__ import annotations

from pydantic_ai import Agent
from pydantic_ai.models import Model

from pyd_app.config import get_model_name

HELLO_WORLD_PROMPT = "Where does 'hello world' come from?"

agent = Agent(
    instructions="Be concise, accurate, and friendly.",
)


def run_hello_world(model: Model | str | None = None) -> str:
    result = agent.run_sync(HELLO_WORLD_PROMPT, model=model or get_model_name())
    return result.output


def main() -> None:
    print(run_hello_world())
