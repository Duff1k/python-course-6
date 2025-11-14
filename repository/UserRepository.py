from psycopg2.extras import RealDictCursor
from db.DatabaseConnection import DatabaseConnection

class UserRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def get_by_username(self, username: str):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            return cur.fetchone()

    def create_user(self, username: str, password_hash: str):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING *;",
                (username, password_hash)
            )
            conn.commit()
            return cur.fetchone()
