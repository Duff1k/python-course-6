from psycopg2.extras import RealDictCursor
from db.DatabaseConnection import DatabaseConnection

class UserRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_user(self, username, hashed_password):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s) RETURNING *;",
                        (username, hashed_password))
            conn.commit()
            return cur.fetchone()

    def get_user_by_username(self, username: str):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            return cur.fetchone()

    def delete_user_by_username(self, username):
        with self.db.get_connection() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE username = %s;", (username,))
            conn.commit()
