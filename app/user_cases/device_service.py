from app.models.device import Device as DeviceModel
from app.infrastructure.device_repository import DeviceRepository
from app.schemas.device_schema import DeviceCreate

class DeviceService:
        def __init__(self, user_repository: DeviceRepository):
            self.repo = user_repository
        
        def create_device(self, paylaod: DeviceCreate):
            new_device = DeviceModel(name=paylaod.name)
            return self.repo.create(new_device)
        
        def get_all_devices(self):
            return self.repo.get_all()
        
        def get_device(self, device_id: int):
            return self.repo.get_id(device_id)
        
        def update_device(self, device_id: int, payload: dict):
            return self.repo.update(device_id, payload)
        
        def delete_device(self, device_id: int):
            return self.repo.delete(device_id)
        
       