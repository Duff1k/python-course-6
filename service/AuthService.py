import bcrypt
from repository.UserRepository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, username: str, password: str) -> bool:
        user = self.user_repo.get_by_username(username)
        if not user:
            return False
        stored_hash = user["password_hash"].encode()
        return bcrypt.checkpw(password.encode(), stored_hash)
