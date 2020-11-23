from pydantic import BaseSettings, PostgresDsn, validator
from typing import Optional


class Settings(BaseSettings):
    DEBUGGING_ENABLED: bool = False
    # Log resolution
    LOG_LEVEL: str = 'INFO'
    # Log output
    LOG_RENDERER: str = "PRETTY"
    # Primary database for this app
    DATABASE_URL: Optional[PostgresDsn] = None
    # Migration timeout in milliseconds
    DATABASE_MIGRATION_TIMEOUT: int = 5000
    # New Relic Insights event namespace
    NEW_RELIC_EVENT_NAMESPACE: str

    CELERY_BROKER: str
    CELERY_BACKEND: str
    CELERY_TASK_ALWAYS_EAGER: bool = False

    NEW_YEAR_CRON: str = "* * * * 1 1"

    NEW_RELIC_DEVELOPER_MODE: bool = True
    NEW_RELIC_APP_NAME: str = "App Name"
    NEW_RELIC_EVENT_NAMESPACE: str = "AppName"
    NEW_RELIC_LICENSE_KEY: str = None
    NEW_RELIC_LOG_ENABLEDE: bool = True
    NEW_RELIC_NO_CONFIG_FILEE: bool = True

    @validator("LOG_LEVEL", pre=True)
    def get_log_level(cls, v: str) -> str:
        return v.upper().strip()

    @validator("LOG_RENDERER", pre=True)
    def get_log_renderer(cls, v: str) -> str:
        return v.upper().strip()

    @validator("DATABASE_URL", pre=True)
    def get_database_url(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            return None
        return v

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()

