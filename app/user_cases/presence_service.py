from app.models.presence import Presence as PresenceModel
from app.infrastructure.presence_repository import PresenceRepository
from app.infrastructure.device_repository import DeviceRepository
from app.schemas.presence_schema import PresenceCreate
from typing import Optional, List, Dict, Any
from fastapi import HTTPException

class PresenceService:
    def __init__(self, presence_repository: PresenceRepository, device_repository: DeviceRepository):
        self.repo = presence_repository
        self.device_repo = device_repository
        
    def get_all_presences(self) -> List[PresenceModel]:
        return self.repo.get_all()
    
    def create_presence(self, payload: PresenceCreate) -> PresenceModel:
        device = self.device_repo.get_id(payload.device_id)
        
        if not device:
            raise HTTPException(status_code=404, detail="Device not found")
            
        new_presence = PresenceModel(
           
            device_id=payload.device_id,
            duration_seconds=payload.duration_seconds,
            timestamp=payload.timestamp,
            status=payload.status
        )
        return self.repo.create(new_presence)
    
    def update_presence(self, presence_id: int, payload: Dict[str, Any]) -> Optional[PresenceModel]:
        return self.repo.update(presence_id, payload)
    
    def delete_presence(self, presence_id: int) -> Optional[Dict[str, str]]:
        return self.repo.delete(presence_id)
    
    def get_presence(self, presence_id: int) -> Optional[PresenceModel]:
        return self.repo.get_id(presence_id)
        