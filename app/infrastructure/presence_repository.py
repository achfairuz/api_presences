from sqlalchemy.orm import Session
from app.models.presence import Presence
from typing import Optional, List, Dict, Any

class PresenceRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_id(self, presence_id: int)-> Optional[Presence]:
        return self.db.query(Presence).filter(Presence.id == presence_id).first()
    
    def get_all(self) -> List[Presence]:
        return self.db.query(Presence).all()
    
    def create(self, payloads: List[Presence])-> List[Presence]:
        
        self.db.add_all(payloads)
        self.db.commit()
        # self.db.refresh(payloads)
        for obj in payloads:
            self.db.refresh(obj)
        return payloads

    def update(self, presence_id: int, payload: Dict[str, Any]) -> Optional[Presence]:
        presence = self.get_id(presence_id)
        if presence:
            for key, value in payload.items():
                if value is not None:  # hanya update jika value ada
                    setattr(presence, key, value)
            self.db.commit()
            self.db.refresh(presence)
        return presence

    
    def delete(self, presence_id: int) -> Optional[Dict[str, str]]:
        presence = self.get_id(presence_id)
        if not presence:
            return None
        self.db.delete(presence)
        self.db.commit()
        return {"message": "Presen  ce deleted successfully"}