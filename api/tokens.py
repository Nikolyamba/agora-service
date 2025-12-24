from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from db.session import get_db
from features.get_user import get_current_user
from services.limiter import limiter
from models.token_log_model import TokenLog
from schemas.tokens_schema import RTCTokenRequest, RTMTokenRequest
from services.agora_service import AgoraService

t_router = APIRouter(prefix='/tokens')

agora_service = AgoraService()
TOKEN_TTL = 3600

@t_router.post("/rtc") #можно было бы использовать response_model = но решил обойтись без этого
@limiter.limit("5/minute")
async def generate_rtc_token(request: Request, data: RTCTokenRequest, db: AsyncSession = Depends(get_db),
                             user_id: str = Depends(get_current_user)) -> dict:
    token = agora_service.generate_rtc_token(
        channel_name=data.channel,
        uid=data.uid,
        role=data.role
    )

    db.add(TokenLog(
        user_id=user_id,
        channel=data.channel,
        token_type="rtc",
        issued_at=datetime.utcnow(),
        expires_at=datetime.utcnow() + timedelta(seconds=TOKEN_TTL),
        ip_address=request.client.host
    ))
    await db.commit()

    return {"token": token, "expires_in": TOKEN_TTL}

@t_router.post("/rtm") #тоже самое
@limiter.limit("5/minute")
async def generate_rtm_token(request: Request, data: RTMTokenRequest, db: AsyncSession = Depends(get_db),
                             user_id: str = Depends(get_current_user)):
    token = agora_service.generate_rtm_token(uid=data.uid)
    db.add(TokenLog(
        user_id=user_id,
        channel=None,
        token_type="rtm",
        issued_at=datetime.utcnow(),
        expires_at=datetime.utcnow() + timedelta(seconds=TOKEN_TTL),
        ip_address=request.client.host
    ))
    await db.commit()

    return {"token": token, "expires_in": TOKEN_TTL}