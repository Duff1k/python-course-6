from db.DatabaseConnection import DatabaseConnection
from utils.password_hasher import hash_password


def init_database():
    """Инициализирует базу данных с тестовыми данными"""
    db = DatabaseConnection()

    try:
        with db.get_connection() as conn, conn.cursor() as cur:
            # Создаем таблицу продуктов
            cur.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    price DECIMAL(10,2) NOT NULL
                )
            """)

            # Создаем таблицу пользователей
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(64) NOT NULL,
                    salt VARCHAR(32) NOT NULL
                )
            """)

            # Добавляем тестового пользователя
            hashed_password, salt = hash_password("admin123")
            cur.execute("""
                INSERT INTO users (username, password, salt) 
                VALUES (%s, %s, %s)
                ON CONFLICT (username) DO NOTHING
            """, ("admin", hashed_password, salt))

            # Добавляем тестовые продукты
            cur.execute("""
                INSERT INTO products (name, price) 
                VALUES 
                ('Laptop', 999.99),
                ('Mouse', 25.50),
                ('Keyboard', 75.00)
                ON CONFLICT DO NOTHING
            """)

            conn.commit()
            print("✅ База данных успешно инициализирована!")
            print("👤 Тестовый пользователь: admin / admin123")

    except Exception as e:
        print(f"❌ Ошибка инициализации базы данных: {e}")


if __name__ == "__main__":
    init_database()