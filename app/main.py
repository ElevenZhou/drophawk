from contextlib import asynccontextmanager
from datetime import UTC, datetime

from fastapi import FastAPI

from app.config import Settings, get_settings
from app.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    init_db(settings.database_path)
    app.state.settings = settings
    app.state.started_at = datetime.now(UTC)
    yield


app = FastAPI(title="DropHawk", version="0.1.0", lifespan=lifespan)


@app.get("/healthz")
def healthz() -> dict[str, object]:
    settings: Settings = app.state.settings
    return {
        "ok": True,
        "service": settings.app.name,
        "environment": settings.app.environment,
        "database": str(settings.database_path),
        "started_at": app.state.started_at.isoformat(),
    }

