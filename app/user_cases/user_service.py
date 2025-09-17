from app.models.user import User as UserModel
from app.infrastructure.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def get_user(self, user_id: int):
        return self.user_repository.get_user(user_id)
    
    def create_user(self, name: str, email: str):
        new_user = UserModel(name=name, email=email)
        return self.user_repository.create(new_user)