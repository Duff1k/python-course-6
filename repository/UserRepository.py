from psycopg2.extras import RealDictCursor
from db.DatabaseConnection import DatabaseConnection
from utils.password_hasher import verify_password

from psycopg2.extras import RealDictCursor
from db.DatabaseConnection import DatabaseConnection
from utils.password_hasher import verify_password

class UserRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def get_user_by_username(self, username: str):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            return cur.fetchone()

    def verify_user_password(self, username: str, password: str) -> bool:
        user = self.get_user_by_username(username)
        if not user:
            return False
        return verify_password(password, user["password"], user["salt"])