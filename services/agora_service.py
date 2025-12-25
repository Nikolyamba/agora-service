from datetime import datetime

from agora_token_builder import RtcTokenBuilder, RtmTokenBuilder
from agora_token_builder.RtcTokenBuilder import Role_Publisher, Role_Attendee
from agora_token_builder.RtmTokenBuilder import Role_Rtm_User

from services.log import setup_logger
from services.settings import agora_app_id, agora_app_certificate

logger = setup_logger()

class AgoraService:
    def __init__(self):
        self.app_id = agora_app_id
        self.app_certificate = agora_app_certificate
        self.ttl_seconds = 3600

    def generate_rtc_token(self, channel_name: str, uid: str, role: str) -> str:

        logger.info(
            f"Генерация РТС токена | channel={channel_name} uid={uid} role={role}"
        )

        role_map={
            "host": Role_Publisher,
            "audience": Role_Attendee,
        }

        if role not in role_map:
            raise ValueError("Роль должна быть либо 'Host' либо 'Audience'")

        expire_ts = int(datetime.utcnow().timestamp()) + self.ttl_seconds

        try:
            token = RtcTokenBuilder.buildTokenWithUid(
            self.app_id,
            self.app_certificate,
            channel_name,
            uid,
            role_map[role],
            expire_ts,
            )
            logger.info('Генерация прошла твёрдо и чётко')

            return token
        except Exception as e:
            logger.exception("Не удалось сгенерировать токен")
            raise

    def generate_rtm_token(self, uid: str) -> str:
        logger.info(
            f"Генерация РТМ токена | uid={uid}"
        )

        expire_ts = int(datetime.utcnow().timestamp()) + self.ttl_seconds

        try:
            token = RtmTokenBuilder.buildToken(
            self.app_id,
            self.app_certificate,
            uid,
            Role_Rtm_User,
            expire_ts
            )
            logger.info('Генерация прошла твёрдо и чётко')

            return token

        except Exception as e:
            logger.exception("Не удалось сгенерировать токен")
            raise