from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RuntimeSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DROPHAWK_", extra="ignore")

    config_path: Path = Path("config/config.yaml")
    data_dir: Path = Path("data")


class AppConfig(BaseModel):
    name: str = "DropHawk"
    environment: str = "local"


class DatabaseConfig(BaseModel):
    path: Path = Path("data/drophawk.sqlite3")


class ScoringConfig(BaseModel):
    threshold: int = 60
    weights: dict[str, int] = Field(default_factory=dict)


class RdapConfig(BaseModel):
    qps: int = 8
    registered_cache_days: int = 7


class SchedulerConfig(BaseModel):
    daily_drop_cron: str = "0 2 * * *"
    backup_cron: str = "0 4 * * *"


class Settings(BaseModel):
    app: AppConfig = Field(default_factory=AppConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    scoring: ScoringConfig = Field(default_factory=ScoringConfig)
    rdap: RdapConfig = Field(default_factory=RdapConfig)
    scheduler: SchedulerConfig = Field(default_factory=SchedulerConfig)
    runtime: RuntimeSettings = Field(default_factory=RuntimeSettings)

    @property
    def database_path(self) -> Path:
        path = self.database.path
        if path.is_absolute():
            return path
        return Path.cwd() / path


def _read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Config file must contain a YAML mapping: {path}")
    return data


@lru_cache
def get_settings() -> Settings:
    runtime = RuntimeSettings()
    raw = _read_yaml(runtime.config_path)
    return Settings(**raw, runtime=runtime)
