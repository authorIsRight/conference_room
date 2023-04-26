# app/schemas/meeting_room.py

from typing import Optional

from pydantic import BaseModel, validator, Field

# Базовый класс схемы, от которого наследуем все остальные.
class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


# Теперь наследуем схему не от BaseModel, а от MeetingRoomBase.
class MeetingRoomCreate(MeetingRoomBase):
    # Переопределяем атрибут name, делаем его обязательным.
    name: str = Field(..., min_length=1, max_length=100)
    # Описывать поле description не нужно: оно уже есть в базовом классе.

    @validator('name')
    def name_no_blank_no_too_long(cls, value: str):
        if not value:
            raise ValueError('Имя не должно быть пустым')
        return value

class MeetingRoomDB(MeetingRoomCreate):
    id: int 
    
    class Config:
        orm_mode = True 