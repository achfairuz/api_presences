from sqlalchemy.orm import Session
from app.user_cases.user_service import UserService
from app.infrastructure.user_repository import UserRepository
from app.schemas.user_schema import userCreate, UserResponse
from typing import  Optional
from fastapi import HTTPException
from app.core.handlers.ResponseHandler import ResponseStatus as ResponseHandler

class UserController:
    def __init__(self, db: Session):
        repo = UserRepository(db)
        self.user_service = UserService(repo)
        
    
    def get_user(self, user_id: int ) -> Optional[UserResponse]:
        try:
            user = self.user_service.get_user(user_id)
            if not user: 
                return None
            return UserResponse.from_orm(user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def create_user(self, user_create: userCreate) -> UserResponse:
        try:
            user = self.user_service.create_user(
                name=user_create.name,
                email=user_create.email
            )
            return UserResponse.from_orm(user)
        except Exception as e:
            return ResponseHandler.error(
                debug=str(e),
            )