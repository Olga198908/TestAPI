import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

# Тест добавления нового питомца
def test_add_pet():
    url = f"{BASE_URL}/pet"
    pet_data = {
        "id": 1,
        "name": "ApiPet",
        "photoUrls": ["http://example.com/photo1"],
        "status": "in stock"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=pet_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "ApiPet"
    assert data["status"] == "in stock"

# Тест получения питомца по ID
def test_get_pet_by_id():
    pet_id = 1
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == pet_id
    assert data["name"] == "ApiPet"

# Тест обновления питомца
def test_update_pet():
    url = f"{BASE_URL}/pet"
    pet_data = {
        "id": 1,
        "name": "UpdateApiPet",
        "photoUrls": ["http://example.com/photo1"],
        "status": "booked"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, json=pet_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "UpdateApiPet"
    assert data["status"] == "booked"

# Тест удаления питомца
def test_delete_pet():
    pet_id = 1
    url = f"{BASE_URL}/pet/{pet_id}"
    headers = {"api_key": "special-key"}  # если требуется api_key в заголовке
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200