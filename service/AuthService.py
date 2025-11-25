from werkzeug.security import generate_password_hash, check_password_hash
from repository.UserRepository import UserRepository

class AuthService():
    def __init__(self):
        self.user_repo = UserRepository()

    def verify_password(self, username: str, password: str) -> bool:
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        return check_password_hash(user['password'],password)

    def hash_password(self, password: str) -> str:
        return generate_password_hash(password)

    def create_user(self, username: str, password: str):
        password_hash = self.hash_password(password)
        return self.user_repo.create_user(username, password_hash)
