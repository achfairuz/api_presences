from pydantic import BaseModel

class DeviceResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # agar bisa convert dari SQLAlchemy model

class DeviceCreate(BaseModel):
    name: str