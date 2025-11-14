from db.DatabaseConnection import DatabaseConnection
from service.AuthService import AuthService
from repository.UserRepository import UserRepository
from repository.ProductRepository import ProductRepository

def init_database():
    db = DatabaseConnection()
    auth_service = AuthService()
    user_repo = UserRepository()
    product_repo = ProductRepository()
    
    # Создаем таблицы
    with db.get_connection() as conn, conn.cursor() as cur:
        # Таблица продуктов (если еще не создана)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2) NOT NULL
            )
        """)
        
        # Таблица пользователей
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)
        
        conn.commit()
        print(" Таблицы созданы успешно")
    
    # Создаем тестового пользователя
    test_user = user_repo.get_user_by_username("admin")
    if not test_user:
        hashed_password = auth_service.hash_password("admin123")
        user_repo.create_user("admin", hashed_password)
        print(" Тестовый пользователь создан: admin / admin123")
    else:
        print("ℹ  Пользователь admin уже существует")

    # Создаем тестовые продукты
    test_products = [
        {"name": "Ноутбук", "price": 999.99},
        {"name": "Мышь", "price": 29.99},
        {"name": "Клавиатура", "price": 79.99}
    ]
    
    existing_products = product_repo.get_all()
    if not existing_products:
        for product in test_products:
            product_repo.create(product["name"], product["price"])
        print(" Тестовые продукты созданы")
    else:
        print(f"ℹ  В базе уже есть {len(existing_products)} продуктов")

    # Показываем что получилось
    print("\n Созданные продукты:")
    products = product_repo.get_all()
    for product in products:
        print(f"  - {product['name']}: ${product['price']}")

if __name__ == "__main__":
    init_database()