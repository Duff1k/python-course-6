import psycopg2
from db_configuration import db_configuration

def insert_products(cur):
    cur.execute("""
                INSERT INTO products (name, price)
                VALUES ('Яблоко', 100),
                       ('Салат Глаз Дракона Пам Парам', 300);
                """)
    print("Продукты в корзине")


def insert_users(cur):
    cur.execute("""
    INSERT INTO users (username, password)
    VALUES ('admin', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
           ('user_p', 'e606e38b0d8c19b24cf0ee3808183162ea7cd63ff7912dbb22b5e803286b4446');
    """);
    print("Пользователи в очереди")


def create_products_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
	        id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	        name VARCHAR(100) NOT NULL,
	        price FLOAT NOT NULL
        );
    """)
    insert_products(cur)


def create_users_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
	        id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(300) NOT NULL
        );
    """)
    insert_users(cur)


def create_database():
    with psycopg2.connect(
            dbname=db_configuration["dbname"],  
            user=db_configuration["user"],  
            password=db_configuration["password"],  
            host=db_configuration["host"],  
            port=db_configuration["port"]  
    ) as conn:
        with conn.cursor() as cur:
            create_products_table(cur)
            create_users_table(cur)

create_database()

class DatabaseConnection:
    def __init__(self):
        self.host = db_configuration["host"]
        self.port = db_configuration["port"]
        self.user = db_configuration["user"]
        self.password = db_configuration["password"]
        self.dbname = db_configuration["dbname"]

    def get_connection(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname = self.dbname
        )