from pydantic_settings import BaseSettings
from supabase import  create_client

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_KEY: str
    ENV: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()

#supabaase client
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
