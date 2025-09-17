from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.interfaces.user_controller import UserController
from app.interfaces.device_controller import DeviceController
from app.interfaces.presence_controller import PresenceController


def get_user_controller(db: Session = Depends(get_db)):
    return UserController(db)

def get_device_controller(db: Session = Depends(get_db)):
    return DeviceController(db)

def get_presence_controller(db: Session = Depends(get_db)):
    return PresenceController(db)