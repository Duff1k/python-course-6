import psycopg2
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    print("Подключение к БД успешно")

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
            username TEXT NOT NULL UNIQUE,  
            password_hash TEXT NOT NULL
        )     
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
            name TEXT NOT NULL,  
            price NUMERIC(10, 2) CHECK (price > 0)  
        )
    """)

    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        users = [
            ("admin", "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"),  # admin123
            ("user_p", "e606e38b0d8c19b24cf0ee3808183162ea7cd63ff7912dbb22b5e803286b4446")   # user123
        ]
        cur.executemany("INSERT INTO users (username, password_hash) VALUES (%s, %s)", users)

    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        products = [
            ("Картошка", 30),
            ("Трюфель", 1500),
        ]
        cur.executemany("INSERT INTO products (name, price) VALUES (%s, %s)", products)

    cur.close()

    conn.commit()
    print("Все ОК")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    if conn:
        conn.close()
        print("Соединение с БД закрыто")



