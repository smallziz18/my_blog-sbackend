from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent
ENV_FILE = BASE_DIR / ".envs/.env"


class Settings(BaseSettings):
    ENVIRONMENT: Literal["dev", "prod"] = "dev"
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8"
    )

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "My Blog API"
    PROJECT_DESCRIPTION: str = "Backend API for my blog"
    SITE_NAME: str = "SMALLZIZ'S BLOG"
    DATABASE_URL: str = "postgresql+asyncpg://smallziz:dabzo123@postgres:5432/nextgen"
    MAIL_FROM: str = "noreply@gmail.com"
    MAIL_FROM_NAME: str = "SMALLZIZ'S BLOG"
    SMTP_HOST: str = "mailpit"
    SMTP_PORT: int = 1025
    SMTP_UI_PORT: int = 8025


settings = Settings()
