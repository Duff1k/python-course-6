from service.ProductService import ProductService
from service.AuthService import AuthService
import uuid

def test_product_crud():
    product_service = ProductService()

    print("Создаем продукт...")
    product = product_service.create({"name": "Test Product", "price": 123.45})
    print("Создан продукт:", product)

    product_id = product["id"]

    print("Получаем список продуктов...")
    products = product_service.list_all()
    print("Текущие продукты:", products)

    print(f"Получаем продукт по id={product_id}...")
    product_by_id = product_service.get(product_id)
    print("Продукт по ID:", product_by_id)

    print(f"Обновляем продукт id={product_id}...")
    updated_product = product_service.update(product_id, {"name": "Updated Name", "price": 543.21})
    print("Обновленный продукт:", updated_product)

    print(f"Удаляем продукт id={product_id}...")
    deleted = product_service.delete(product_id)
    print("Удален:", deleted)

def test_user_auth():
    auth_service = AuthService()

    username = "testuser_" + str(uuid.uuid4())[:8]  # уникальный username для теста
    password = "testpassword"

    print("Регистрируем пользователя...")
    user = auth_service.create_user(username, password)
    print("Пользователь создан:", user)

    print("Проверяем пароль (правильный)...")
    assert auth_service.verify_password(username, password) == True
    print("Пароль верный")

    print("Проверяем пароль (неправильный)...")
    assert auth_service.verify_password(username, "wrongpassword") == False
    print("Обнаружен неправильный пароль")

if __name__ == "__main__":
    test_product_crud()
    test_user_auth()
    print("Все проверки завершены")
