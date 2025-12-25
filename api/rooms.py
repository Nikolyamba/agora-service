import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from db.session import get_db
from features.get_user import get_current_user
from services.limiter import limiter
from models.rooms_model import Room
from schemas.room_schema import CreateRoomRequest
from services.log import setup_logger

r_router = APIRouter(prefix='/rooms')

logger = setup_logger()

@r_router.post("")
@limiter.limit("5/minute")
async def create_room(request: Request, data: CreateRoomRequest, db: AsyncSession = Depends(get_db),
                      user_id: str = Depends(get_current_user)):
    agora_channel_name = 'agora_channel_xyz' + f"{uuid.uuid4().hex[:12]}"
    room = Room(name=data.name,
        agora_channel_name=agora_channel_name,
        is_private=data.is_private,
        max_participants=data.max_participants,
        created_by=user_id)

    logger.info(f"Комната создана | room_id={room.id} channel={room.agora_channel_name} user={user_id}")

    db.add(room)
    await db.commit()
    await db.refresh(room)

    return {
        "room_id": str(room.id),
        "channel_name": room.agora_channel_name,
    }