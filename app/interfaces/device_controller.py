from sqlalchemy.orm import Session
from app.core.handlers.ResponseHandler import ResponseStatus as response
from app.user_cases.device_service import DeviceService
from app.infrastructure.device_repository import DeviceRepository
from app.schemas.device_schema import DeviceCreate, DeviceResponse
from typing import Optional, List


from fastapi import HTTPException

class DeviceController:
    def __init__(self, db: Session, ):
        repo = DeviceRepository(db)
        self.device_service = DeviceService(repo)
    
    def create_device(self, payload: DeviceCreate) -> DeviceResponse:
        try:
            device = self.device_service.create_device(payload)
            return response.success_create(
                data=DeviceResponse.from_orm(device)
            )
        except Exception as e:
            return response.error(
                debug=str(e),
            )
            
    def get_device(self, device_id: int ) -> Optional[DeviceResponse]:
        try:
            device = self.device_service.get_device(device_id)
            if not device:
                return response.not_found()
            
            return response.success(
                data=DeviceResponse.from_orm(device)
            )
        except Exception as e:
            return response.error(
                debug=str(e),
            )
    
    def get_devices(self) -> List[DeviceResponse]:
        try:
            devices = self.device_service.get_all_devices()
            if not devices:
                return []
            return response.success(
                data=[DeviceResponse.from_orm(device) for device in devices]
            )
        except Exception as e:
            return response.error(
                debug=str(e),
            )
    
   
    def update_device(self, device_id: int, payload: dict) -> Optional[DeviceResponse]:
        try:
            device = self.device_service.update_device(device_id, payload)
            if not device:
                return response.not_found()
            return response.update_success(data=DeviceResponse.from_orm(device))
        except Exception as e:
            return response.error(
                debug=str(e),
            )
            
    def delete_device(self, device_id: int) -> Optional[dict]:
        try:
            result = self.device_service.delete_device(device_id)
            if not result:
                return response.not_found()
            return response.delete_success(message="Device deleted successfully")
        except Exception as e:
            return response.error(
                debug=str(e),
            )
            
  