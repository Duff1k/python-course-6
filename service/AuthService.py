from repository.UserRepository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def verify_password(self, username: str, password: str) -> bool:
        return self.user_repo.verify_user_password(username, password)
