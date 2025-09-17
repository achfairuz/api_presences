from pydantic import BaseModel

class PresenceResponse(BaseModel):
    id: int
    device_id: int
    timestamp: str  # ISO format datetime as string
    duration_seconds: int
    status: str  # Enum as string

    class Config:
        from_attributes = True  # agar bisa convert dari SQLAlchemy model
        
class PresenceCreate(BaseModel):
    device_id: int
    timestamp: str  # ISO format datetime as string
    duration_seconds: int
    status: str  # Enum as string