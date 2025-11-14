import requests
import json

BASE_URL = "http://localhost:5000"
AUTH = ("admin", "admin123")

def test_get_all_products():
    """Тест получения всех продуктов"""
    print("1.  Тест получения всех продуктов")
    response = requests.get(f"{BASE_URL}/products")
    print(f"   GET /products - Status: {response.status_code}")
    if response.status_code == 200:
        products = response.json()
        print(f"   Найдено продуктов: {len(products)}")
        if products:
            print(f"   Первый продукт: {products[0]['name']} - ${products[0]['price']}")
    print("-" * 50)

def test_get_existing_product():
    """Тест получения существующего продукта"""
    print("2.  Тест получения существующего продукта")
    # Сначала получаем список продуктов чтобы взять реальный ID
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200 and response.json():
        product_id = response.json()[0]['id']
        response = requests.get(f"{BASE_URL}/products/{product_id}")
        print(f"   GET /products/{product_id} - Status: {response.status_code}")
        if response.status_code == 200:
            product = response.json()
            print(f"   Продукт: {product['name']} - ${product['price']}")
    else:
        print("    Нет продуктов для тестирования")
    print("-" * 50)

def test_get_nonexistent_product():
    """Тест получения несуществующего продукта"""
    print("3.  Тест получения несуществующего продукта")
    response = requests.get(f"{BASE_URL}/products/9999")
    print(f"   GET /products/9999 - Status: {response.status_code}")
    if response.status_code == 404:
        print("   ✅ Корректно вернул 404 для несуществующего продукта")
    print("-" * 50)

def test_create_product():
    """Тест создания продукта"""
    print("4.  Тест создания продукта")
    data = {
        "name": "Новый тестовый продукт",
        "price": 199.99
    }
    response = requests.post(
        f"{BASE_URL}/products",
        json=data,
        auth=AUTH
    )
    print(f"   POST /products - Status: {response.status_code}")
    if response.status_code == 200:
        product = response.json()
        print(f"   Создан продукт: {product['name']} - ${product['price']} (ID: {product['id']})")
        return product['id']
    return None

def test_unauthorized_create():
    """Тест создания без авторизации"""
    print("5.  Тест создания без авторизации")
    data = {"name": "Неавторизованный", "price": 50}
    response = requests.post(f"{BASE_URL}/products", json=data)
    print(f"   POST /products (no auth) - Status: {response.status_code}")
    if response.status_code == 401:
        print("   ✅ Корректно требует авторизацию")
    print("-" * 50)

def test_update_product():
    """Тест обновления продукта"""
    print("6.  Тест обновления продукта")
    # Сначала создаем продукт для обновления
    product_id = test_create_product()
    if product_id:
        data = {
            "name": "Обновленный продукт",
            "price": 299.99
        }
        response = requests.put(
            f"{BASE_URL}/products/{product_id}",
            json=data,
            auth=AUTH
        )
        print(f"   PUT /products/{product_id} - Status: {response.status_code}")
        if response.status_code == 200:
            product = response.json()
            print(f"   Обновлен продукт: {product['name']} - ${product['price']}")
    print("-" * 50)

def test_delete_product():
    """Тест удаления продукта"""
    print("7.  Тест удаления продукта")
    # Сначала создаем продукт для удаления
    product_id = test_create_product()
    if product_id:
        response = requests.delete(
            f"{BASE_URL}/products/{product_id}",
            auth=AUTH
        )
        print(f"   DELETE /products/{product_id} - Status: {response.status_code}")
        if response.status_code == 200:
            print("    Продукт успешно удален")
    print("-" * 50)

def test_wrong_auth():
    """Тест с неправильными credentials"""
    print("8.  Тест с неправильным паролем")
    data = {"name": "Тест", "price": 100}
    response = requests.post(
        f"{BASE_URL}/products", 
        json=data, 
        auth=("admin", "wrongpassword")
    )
    print(f"   POST /products (wrong pass) - Status: {response.status_code}")
    if response.status_code == 401:
        print("    Корректно отвергает неправильный пароль")
    print("-" * 50)

def run_all_tests():
    """Запуск всех тестов"""
    print(" ЗАПУСК ТЕСТИРОВАНИЯ API")
    print("=" * 50)
    
    try:
        # Тесты которые не меняют данные
        test_get_all_products()
        test_get_existing_product()
        test_get_nonexistent_product()
        test_unauthorized_create()
        test_wrong_auth()
        
        # Тесты которые создают/изменяют данные
        test_create_product()
        test_update_product()
        test_delete_product()
        
        print("✅ ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
        
    except requests.exceptions.ConnectionError:
        print(" ОШИБКА: Не могу подключиться к серверу")
        print("   Запустите сервер: python ProductController.py")
    except Exception as e:
        print(f" ОШИБКА: {e}")

if __name__ == "__main__":
    run_all_tests()