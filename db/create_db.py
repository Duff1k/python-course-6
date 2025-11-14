import psycopg2
from db.config import db_host, db_port, db_name, db_user, db_password

try:
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        dbname=db_name
    )
    print("Подключение к БД успешно")

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
            username VARCHAR (50) NOT NULL UNIQUE,  
            password VARCHAR (300) NOT NULL
        )     
    """)
    print("Юзеры созданы")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price FLOAT NOT NULL	
        )
    """)
    print("Продукты созданы")

    cur.execute("""
        INSERT INTO users (username, password) 
        VALUES ('admin', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
        ('user_p', 'e606e38b0d8c19b24cf0ee3808183162ea7cd63ff7912dbb22b5e803286b4446');
    """)
    print("Юзеры заполнены")

    cur.execute("""
        INSERT INTO products (name, price) 
        VALUES ('Персики', '320'),
        ('Груши', '170');
    """)
    print("Продукты заполнены")

    cur.close()

except Exception as e:
    print("Ошибка:", e)
