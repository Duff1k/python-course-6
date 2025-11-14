import hashlib
from repository.UserRepository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    
    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, username: str, password: str) -> bool:
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        
        return user["password"] == self.hash_password(password)
