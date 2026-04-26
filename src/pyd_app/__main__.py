def main() -> None:
    raise SystemExit(
        "This app runs through the Pydantic AI web UI. Start it with:\n"
        "uv run uvicorn pyd_app.web:create_app --factory --host 127.0.0.1 --port 7932"
    )


if __name__ == "__main__":
    main()
