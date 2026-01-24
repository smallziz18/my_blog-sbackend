from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict
BASE_DIR = Path(__file__).parent.parent
ENV_FILE = BASE_DIR / ".envs/.env"

class Settings(BaseSettings):
    ENVIRONMENT: Literal["dev", "prod"] = "dev"
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
    )
    API_V1_STR: str = ""
    PROJECT_NAME: str = ""
    PROJECT_DESCRIPTION: str = ""
    SITE_NAME: str = ""
    DATABASE_URL: str = ""
    MAIL_FROM: str = ""
    MAIL_FROM_NAME: str = ""
    SMTP_HOST: str = "mailpit"
    SMTP_PORT: int = 1025
    SMTP_UI_PORT: int = 8025



settings = Settings()