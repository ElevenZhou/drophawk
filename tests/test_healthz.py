from fastapi.testclient import TestClient

from app.main import app


def test_healthz_initializes_database(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("DROPHAWK_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("DROPHAWK_CONFIG_PATH", "missing.yaml")

    from app.config import get_settings

    get_settings.cache_clear()

    with TestClient(app) as client:
        response = client.get("/healthz")

    assert response.status_code == 200
    payload = response.json()
    assert payload["ok"] is True
    assert payload["service"] == "DropHawk"
