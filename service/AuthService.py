import hashlib
from repository.UserRepository import UserRepository


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def verify_password(self, username: str, password: str) -> bool:
        print("USERNAME =", username)
        print("PASSWORD =", password)
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        return user["password"] == hashlib.sha256(password.encode()).hexdigest()
