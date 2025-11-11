import bcrypt
from repository.UserRepository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def hash_password(self, password: str) -> str:
        # Генерируем соль и хэш
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def verify_password(self, username, password) -> bool:
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        stored_hash = user["password"]
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
