from repository.UserRepository import UserRepository
from service.AuthService import AuthService

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.auth_service = AuthService()

    def init_schema(self):
        self.user_repo.init_table()

    def create_user(self, username:str, password:str):
        password = self.auth_service.hash_password(password)
        return self.user_repo.create_user(username, password)

    def ensure_default_users(self):
        default_users = [
            ("Katie", "meowLove"),
            ("katusha", "Love"),
        ]
        for username, password in default_users:
            self.create_user(username, password)