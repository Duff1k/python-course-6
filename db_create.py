import psycopg2
import yaml

from hash_users_passwords import hash_password


def insert_products(cur):
    cur.execute("""
                INSERT INTO products (name, price)
                VALUES ('Первое', 100.50),
                       ('Второе', 149.09);
                """)
    print("Продукты добавлены")

def insert_users(cur):
    cur.execute(f"""
    INSERT INTO users (username, password)
    VALUES ('admin', '{hash_password('password')}'),
           ('user', '{hash_password('passw0rd')}');
    """);
    print("Пользователи добавлены")

def create_products_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
	        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	        name VARCHAR(100) NOT NULL,
	        price FLOAT NOT NULL
        );
    """)
    insert_products(cur)
def create_users_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
	        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(300) NOT NULL
        );
    """)
    insert_users(cur)

def create_database():
    with open('configDB.yml', 'r') as f:
        data = yaml.full_load(f)
    with psycopg2.connect(
        host=data['db_conf']['host'],
        port=data['db_conf']['port'],
        user=data['db_conf']['user'],
        password=data['db_conf']['password'],
        dbname=data['db_conf']['dbname']
    ) as conn:
        with conn.cursor() as cur:
            create_products_table(cur)
            create_users_table(cur)
create_database()