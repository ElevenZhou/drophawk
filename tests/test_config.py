from pathlib import Path

from app.config import Settings


def test_settings_resolves_relative_database_path() -> None:
    settings = Settings(database={"path": "data/test.sqlite3"})

    assert settings.database_path == Path.cwd() / "data/test.sqlite3"

