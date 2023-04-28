# app/main.py
from fastapi import FastAPI

# Импортируем настройки проекта из config.py.
from app.core.config import settings
# Импортируем роутер.
from app.api.routers import main_router

# Устанавливаем заголовок приложения при помощи аргумента title,
# в качестве значения указываем атрибут app_title объекта settings.
app = FastAPI(title=settings.app_title, description=settings.description) 

# Подключаем главный роутер.
app.include_router(main_router)