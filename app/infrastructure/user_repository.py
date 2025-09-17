from sqlalchemy.orm import Session
from app.models.user import User as UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_user(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def create(self, user: UserModel):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user