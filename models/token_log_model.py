import uuid

from sqlalchemy import Column, UUID, String, DateTime, func

from db.base import Base

class TokenLog(Base):
    __tablename__ = 'token_logs'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    channel = Column(String)
    token_type = Column(String, nullable=False)
    issued_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)
    ip_address = Column(String)

