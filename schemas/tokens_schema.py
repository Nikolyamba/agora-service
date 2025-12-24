from enum import Enum
from pydantic import BaseModel, Field

class RoleEnum(str, Enum):
    host = "host"
    audience = "audience"

class RTCTokenRequest(BaseModel):
    channel: str = Field(min_length=3, max_length=64) #отсебятина
    uid: str
    role: RoleEnum

class RTMTokenRequest(BaseModel):
    uid: str