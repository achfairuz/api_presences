from sqlalchemy.orm import Session
from app.schemas.presence_schema import PresenceCreate, PresenceResponse
from app.core.handlers.ResponseHandler import ResponseStatus as response
from app.user_cases.presence_service import PresenceService
from app.user_cases.device_service import DeviceService
from app.infrastructure.device_repository import DeviceRepository
from app.infrastructure.presence_repository import PresenceRepository
from fastapi import HTTPException
from typing import List

class PresenceController:
    def __init__(self, db: Session):
        # repository
        presence_repo = PresenceRepository(db)
        device_repo = DeviceRepository(db)
        
        # service
        self.presence_service = PresenceService(presence_repo, device_repo)
        self.device_service = DeviceService(device_repo)
    
    def create_presence(self, payloads: List[PresenceCreate]) -> List[PresenceResponse]:
        try:
            presences = self.presence_service.create_presence(payloads)
            return response.success(presences,"Presence created successfully", )
        except HTTPException as e:
            return response.error(e.detail)
        except Exception as e:
            return response.error(debug={str(e)})
        
    def get_all_presences(self) -> PresenceResponse:
        try:
            presences = self.presence_service.get_all_presences()
            return response.success("Presences retrieved successfully", presences)
        except Exception as e:
            return response.error(f"Error retrieving presences: {str(e)}")
