import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from schemes import (
    resource_list_schema,
    register_success_schema,
    create_user_schema,
    update_schema
)

def test_get_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert "data" in response.json(), "Ответ не содержит ожидаемого поля 'data'."
    print("GET /api/users/2: Ответ соответствует схеме.")

def test_get_user_negative():
    url = "https://reqres.in/api/users/9999"
    response = requests.get(url)
    assert response.status_code == 404, f"Expected status 404, got {response.status_code}"
    assert "data" not in response.json(), "Ответ содержит поле 'data', которого не должно быть."
    print("GET /api/users/9999: Ошибка соответствует ожиданиям.")
# 1. Тесты для GET /api/users
def test_get_users():
    url = "https://reqres.in/api/users?page=1"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    validate(instance=response.json(), schema=resource_list_schema)
    print("GET /api/users: Ответ соответствует схеме.")

# 2. Тесты для POST /api/users
def test_post_users():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "John Doe",
        "job": "Software Developer"
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201, f"Expected status 201, got {response.status_code}"

    validate(instance=response.json(), schema=register_success_schema)
    print("POST /api/users: Ответ соответствует схеме.")

def test_post_users_negative():
    url = "https://reqres.in/api/users"
    payload = ""

    response = requests.post(url, json=payload)
    assert response.status_code == 400, f"Expected status 400, got {response.status_code}"
    print("POST /api/users with empty payload: Ошибка соответствует ожиданиям.")

# 3. Тесты для PUT /api/users
def test_put_user():
    url = "https://reqres.in/api/users/2"
    payload = {
        "name": "Jane Doe",
        "job": "Senior Developer"
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    validate(instance=response.json(), schema=update_schema)
    print("PUT /api/users: Ответ соответствует схеме.")

# 4. Тесты для DELETE
def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)
    assert response.status_code == 204, f"Expected status 204, got {response.status_code}"
    assert response.text == "", "Ответ тела DELETE должен быть пустым."
    print("DELETE /api/users/2: Ошибка соответствует ожиданиям.")
# 5. Тесты для некорректного POST

def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "John Doe",
        "job": "Software Developer"
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201, f"Expected status 201, got {response.status_code}"

    validate(instance=response.json(), schema=create_user_schema)
    print("POST /api/users: Ответ соответствует схеме.")


if __name__ == "__main__":
    test_get_user()
    test_get_user_negative()
    test_get_users()
    test_post_users()
    test_post_users_negative()
    test_put_user()
    test_delete_user()
    test_create_user()