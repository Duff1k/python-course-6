from repository.UserRepository import UserRepository
from werkzeug.security import check_password_hash  # сравнивает хеш и пароль и возвращает true/false
from werkzeug.security import generate_password_hash #хеширует пароль


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, username: str, password: str):
        hashed_password = generate_password_hash(password)
        return self.user_repo.create_user(username, hashed_password)

    def verify_password(self, username: str, password: str) -> bool:
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        # return user["password"] == password
        return check_password_hash(user["password"], password)
