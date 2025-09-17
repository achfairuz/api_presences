from sqlalchemy.orm import Session
from app.models.device import Device

class DeviceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payload: Device) -> Device:
        self.db.add(payload)
        self.db.commit()
        self.db.refresh(payload)
        return payload

    def get_all(self) -> list[Device]:
        return self.db.query(Device).all()

    def get_id(self, device_id: int) -> Device | None:
        return self.db.query(Device).filter_by(id=device_id).first()

    def update(self, device_id: int, payload: dict) -> Device | None:
        device = self.get_id(device_id)
        if not device:
            return None
        for key, value in payload.items():
            if hasattr(device, key):
                setattr(device, key, value)
        self.db.commit()
        self.db.refresh(device)
        return device

    def delete(self, device_id: int) -> Device | None:
        device = self.get_id(device_id)
        if not device:
            return None
        self.db.delete(device)
        self.db.commit()
        return device
