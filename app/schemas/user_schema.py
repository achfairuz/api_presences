from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # agar bisa convert dari SQLAlchemy model


class userCreate(BaseModel):
    email: EmailStr
    name: str