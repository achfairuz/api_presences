from fastapi import FastAPI, Depends, APIRouter
from app.interfaces.user_controller import UserController
from app.schemas.user_schema import UserResponse, userCreate
from routes.API.dependencies import get_user_controller

router = APIRouter()

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, controller: UserController = Depends(get_user_controller)):
    return controller.get_user(user_id)

@router.post("/users", response_model=UserResponse)
def create_user(user:userCreate, controller: UserController = Depends(get_user_controller)):
    return controller.create_user(user)