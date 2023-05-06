# app/core/config.py
from pydantic import BaseSettings, EmailStr
from typing import Optional


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    description: str = 'Тестируем йобта'
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
