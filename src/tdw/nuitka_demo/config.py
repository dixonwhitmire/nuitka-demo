from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    uvicorn_app: str = "tdw.nuitka_demo.asgi:app"
    uvicorn_host: str = "0.0.0.0"
    uvicorn_port: int = 5000
    uvicorn_reload: bool = False

@lru_cache()
def get_settings() -> Settings:
    """Returns the settings instance"""
    return Settings()
