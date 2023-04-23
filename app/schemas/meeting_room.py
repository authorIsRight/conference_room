# app/schemas/meeting_room.py

from typing import Optional

from pydantic import BaseModel, validator, Field


class MeetingRoomCreate(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] 

    @validator('name')
    def name_no_blank_no_too_long(cls, value: str):
        if not value['name']:
            raise ValueError('Имя не должно быть пустым')
        return value