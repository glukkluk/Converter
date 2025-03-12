from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
print(BASE_DIR)


class BotConfig(BaseModel):
    bot_token: str


class MiscConfig(BaseModel):
    tinify_api_key: str


class ApiConfig(BaseModel):
    base_url: str = "http://bot:8000/api/v1/"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_nested_delimiter="__"
    )

    bot: BotConfig
    misc: MiscConfig

    api: ApiConfig = ApiConfig()


settings = Settings()
