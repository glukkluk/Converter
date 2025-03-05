from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ApiConfig(BaseModel):
    base_url: str = "http://127.0.0.1:8000/api/v1/"


class Settings(BaseSettings):
    api: ApiConfig = ApiConfig()


settings = Settings()