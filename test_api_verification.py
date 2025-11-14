import requests
import json
import base64


def test_all_api_endpoints():
    """
    Проверка всех API endpoints для демонстрации работоспособности
    """
    BASE_URL = "http://localhost:5001"

    print("🔍 ТЕСТИРОВАНИЕ ВСЕХ API ENDPOINTS")
    print("=" * 50)

    # Тестовые данные
    test_product = {"name": "Test Product", "price": 99.99}
    auth = ("admin", "admin123")

    results = []

    # 1. GET /products
    print("\n1. GET /products")
    try:
        response = requests.get(f"{BASE_URL}/products")
        success = response.status_code == 200
        results.append(("GET /products", success, response.status_code))
        print(f"   ✅ Статус: {response.status_code}, Продуктов: {len(response.json())}")
    except Exception as e:
        results.append(("GET /products", False, str(e)))
        print(f"   ❌ Ошибка: {e}")

    # 2. GET /products/1
    print("\n2. GET /products/1")
    try:
        response = requests.get(f"{BASE_URL}/products/1")
        success = response.status_code == 200
        results.append(("GET /products/1", success, response.status_code))
        if success:
            product = response.json()
            print(f"   ✅ Статус: {response.status_code}, Продукт: {product.get('name')}")
        else:
            print(f"   ❌ Статус: {response.status_code}")
    except Exception as e:
        results.append(("GET /products/1", False, str(e)))
        print(f"   ❌ Ошибка: {e}")

    # 3. POST /products (с авторизацией)
    print("\n3. POST /products (с авторизацией)")
    try:
        response = requests.post(f"{BASE_URL}/products", json=test_product, auth=auth)
        success = response.status_code == 200
        results.append(("POST /products", success, response.status_code))
        if success:
            product = response.json()
            print(f"   ✅ Статус: {response.status_code}, Создан: {product.get('name')}")
            created_id = product.get('id')
        else:
            print(f"   ❌ Статус: {response.status_code}")
            created_id = None
    except Exception as e:
        results.append(("POST /products", False, str(e)))
        print(f"   ❌ Ошибка: {e}")
        created_id = None

    # 4. PUT /products/2 (с авторизацией)
    print("\n4. PUT /products/2 (с авторизацией)")
    try:
        update_data = {"name": "Updated Product", "price": 149.99}
        response = requests.put(f"{BASE_URL}/products/2", json=update_data, auth=auth)
        success = response.status_code == 200
        results.append(("PUT /products/2", success, response.status_code))
        if success:
            product = response.json()
            print(f"   ✅ Статус: {response.status_code}, Обновлен: {product.get('name')}")
        else:
            print(f"   ❌ Статус: {response.status_code}")
    except Exception as e:
        results.append(("PUT /products/2", False, str(e)))
        print(f"   ❌ Ошибка: {e}")

    # 5. DELETE /products (с авторизацией) - если продукт был создан
    if created_id:
        print(f"\n5. DELETE /products/{created_id} (с авторизацией)")
        try:
            response = requests.delete(f"{BASE_URL}/products/{created_id}", auth=auth)
            success = response.status_code == 200
            results.append(("DELETE /products", success, response.status_code))
            if success:
                print(f"   ✅ Статус: {response.status_code}, Удален продукт ID: {created_id}")
            else:
                print(f"   ❌ Статус: {response.status_code}")
        except Exception as e:
            results.append(("DELETE /products", False, str(e)))
            print(f"   ❌ Ошибка: {e}")

    # 6. Проверка защиты endpoints
    print("\n6. Проверка защиты endpoints")
    try:
        response = requests.post(f"{BASE_URL}/products", json=test_product)
        success = response.status_code == 401
        results.append(("POST /products (без auth)", success, response.status_code))
        print(f"   ✅ Защита работает: {response.status_code == 401}")
    except Exception as e:
        results.append(("POST /products (без auth)", False, str(e)))
        print(f"   ❌ Ошибка: {e}")

    # Итоговый отчет
    print("\n" + "=" * 50)
    print("📊 ИТОГОВЫЙ ОТЧЕТ:")
    print("=" * 50)

    all_passed = True
    for endpoint, success, status in results:
        status_icon = "✅" if success else "❌"
        print(f"{status_icon} {endpoint}: {status}")
        if not success:
            all_passed = False

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ВСЕ ENDPOINTS РАБОТАЮТ КОРРЕКТНО!")
    else:
        print("⚠️  Некоторые endpoints требуют внимания")

    print(f"\n📎 Для тестирования запустите сервер и выполните:")
    print(f"   python test_api_verification.py")


if __name__ == "__main__":
    test_all_api_endpoints()