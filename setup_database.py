import hashlib
from db.DatabaseConnection import DatabaseConnection
from app_config import USER_CREDENTIALS


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def initialize_database():
    db = DatabaseConnection()

    try:
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(50) UNIQUE NOT NULL,
                        password VARCHAR(255) NOT NULL
                    )
                """)

                cur.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        price DECIMAL(10, 2) NOT NULL
                    )
                """)

                for username, password in USER_CREDENTIALS.items():
                    hashed_password = hash_password(password)
                    cur.execute(
                        "INSERT INTO users (username, password) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING",
                        (username, hashed_password)
                    )

                products = [
                    ("Диван", 900.10),
                    ("Стол", 500.20),
                    ("Стул", 200.30)
                ]

                for name, price in products:
                    cur.execute(
                        "INSERT INTO products (name, price) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                        (name, price)
                    )

                conn.commit()
                print("База данных создана")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    initialize_database()