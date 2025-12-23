import uuid

from sqlalchemy import Column, UUID, String, Boolean, DateTime, func, Integer

from db.base import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    agora_channel_name = Column(String, nullable=False, unique=True)
    is_private = Column(Boolean, default=False)
    max_participants = Column(Integer)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())