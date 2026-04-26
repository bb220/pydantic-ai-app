from __future__ import annotations

from pydantic_ai.models.test import TestModel

from pyd_app.hello_world import run_hello_world


def test_run_hello_world_uses_test_model() -> None:
    output = run_hello_world(TestModel(custom_output_text="Hello from TestModel."))

    assert output == "Hello from TestModel."
