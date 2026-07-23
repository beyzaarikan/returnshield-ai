from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: str
    DEBUG: bool = True
    GEMINI_API_KEY: str = ""
    FRONTEND_ORIGINS: str = "http://localhost:3000"

settings = Settings()
