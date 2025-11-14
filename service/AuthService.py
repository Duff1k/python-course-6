from repository.UserRepository import UserRepository


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def verify_password(self, username: str, password: str) -> bool:
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        return user["password"] == password

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return user["password_hash"] == password_hash
