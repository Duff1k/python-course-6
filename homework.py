import hashlib
from db.DatabaseConnection import DatabaseConnection

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def init_database():
    db = DatabaseConnection()

    try:
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                # Создание таблицы пользователей
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        username VARCHAR(50) UNIQUE NOT NULL,
                        password VARCHAR(255) NOT NULL
                    )
                """)

                # Создание таблицы продуктов
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        name VARCHAR(100) UNIQUE NOT NULL,
                        price DECIMAL(10, 2) NOT NULL
                    )
                """)

                # Создание индексов для оптимизации запросов
                cur.execute("CREATE INDEX IF NOT EXISTS idx_users_username ON users(username)")
                cur.execute("CREATE INDEX IF NOT EXISTS idx_products_name ON products(name)")

                # Вставка тестовых пользователей
                cur.execute("""
                    INSERT INTO users (username, password) 
                    VALUES 
                        (%s, %s),
                        (%s, %s), 
                        (%s, %s)
                    ON CONFLICT (username) DO NOTHING
                """, (
                    "admin", _hash_password("admin123"),
                    "user1", _hash_password("user1123"),
                    "user2", _hash_password("user2123")
                ))

                # Вставка тестовых продуктов (теперь с конфликтом по name)
                cur.execute("""
                    INSERT INTO products (name, price) 
                    VALUES 
                        (%s, %s),
                        (%s, %s), 
                        (%s, %s)
                    ON CONFLICT (name) DO NOTHING
                """, (
                    "Диван", 900.10,
                    "Стол", 500.20,
                    "Стул", 200.30
                ))

                conn.commit()
                print("✅ База данных успешно инициализирована")

    except Exception as e:
        print(f"❌ Ошибка при инициализации базы данных: {e}")

if __name__ == "__main__":
    init_database()
