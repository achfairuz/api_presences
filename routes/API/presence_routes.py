from fastapi import FastAPI, Depends, APIRouter
from app.interfaces.presence_controller import PresenceController
from app.schemas.presence_schema import PresenceResponse, PresenceCreate
from routes.API.dependencies import get_presence_controller

router = APIRouter()

@router.post("/presences", response_model=PresenceResponse)
def create_presence(payload: PresenceCreate, controller: PresenceController = Depends(get_presence_controller)):
    return controller.create_presence(payload)
@router.get("/presences/", response_model=PresenceResponse)
def get_presence( controller: PresenceController = Depends(get_presence_controller)):
    return controller.get_all_presences()