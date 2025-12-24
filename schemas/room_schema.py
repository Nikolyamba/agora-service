from pydantic import BaseModel, Field

class CreateRoomRequest(BaseModel):
    name: str = Field(min_length=3, max_length=128)
    is_private: bool = False
    max_participants: int