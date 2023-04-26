# app/api/meeting_room.py

from fastapi import APIRouter, Depends, HTTPException

# Импортируем класс асинхронной сессии для аннотации параметра.
from sqlalchemy.ext.asyncio import AsyncSession

# Импортируем асинхронный генератор сессий.
from app.core.db import get_async_session
from app.crud.meeting_room import create_meeting_room, get_room_id_by_name, read_all_rooms_from_db
# Импортируем схему ответа.
from app.schemas.meeting_room import MeetingRoomCreate, MeetingRoomDB


# Добавьте параметр prefix.
router = APIRouter(
    prefix='/meeting_rooms',
    tags=['Meeting Rooms']
) 


@router.post(
    '/',
    # Указываем схему ответа.
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
)
async def create_new_meeting_room(
        meeting_room: MeetingRoomCreate,
        # Указываем зависимость, предоставляющую объект сессии, как параметр функции.
        session: AsyncSession = Depends(get_async_session),
):
    # Вторым параметром передаём сессию в CRUD-функцию:
    room_id = await get_room_id_by_name(meeting_room.name, session)
    # Если такой объект уже есть в базе - вызываем ошибку:
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Переговорка с таким именем уже существует!',
        )

    # Вторым параметром передаём сессию в CRUD-функцию:
    new_room = await create_meeting_room(meeting_room, session)
    return new_room

@router.get(
    '/',
    response_model=list[MeetingRoomDB],
    response_model_exclude_none=True,
)
async def get_all_meeting_rooms(
        session: AsyncSession = Depends(get_async_session),
):
    all_rooms = await read_all_rooms_from_db(session)
    return all_rooms 