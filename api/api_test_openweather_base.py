import requests

API_KLYUCH = "feede04274cb8bb3f089d0da039d00e4"
BAZOVYY_URL = "https://api.openweathermap.org"

def test_tekushchaya_pogoda_po_gorodu():
    params = {
        "q": "Novosibirsk",
        "appid": API_KLYUCH,
        "units": "metric"
    }
    response = requests.get(f"{BAZOVYY_URL}/data/2.5/weather", params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

def test_geokodirovanie_po_gorodu_1():
    params = {
        "q": "Berdsk",
        "appid": API_KLYUCH
    }
    response = requests.get(f"{BAZOVYY_URL}/geo/1.0/direct", params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

def test_obratnoe_geokodirovanie_1():
    params = {
        "lat": 54.75,
        "lon": 83.10,
        "appid": API_KLYUCH
    }
    response = requests.get(f"{BAZOVYY_URL}/geo/1.0/reverse", params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

def test_geokodirovanie_po_gorodu_2():
    params = {
        "q": "Iskitim",
        "appid": API_KLYUCH
    }
    response = requests.get(f"{BAZOVYY_URL}/geo/1.0/direct", params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

def test_obratnoe_geokodirovanie_2():
    params = {
        "lat": 54.64,
        "lon": 83.30,
        "appid": API_KLYUCH
    }
    response = requests.get(f"{BAZOVYY_URL}/geo/1.0/reverse", params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

def test_geokodirovanie_po_gorodu_3():
    params = {
        "q": "Toguchin",
        "appid": API_KLYUCH
    }
    response = requests.get(f"{BAZOVYY_URL}/geo/1.0/direct", params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

def test_obratnoe_geokodirovanie_3():
    params = {
        "lat": 55.23,
        "lon": 84.40,
        "appid": API_KLYUCH
    }
    response = requests.get(f"{BAZOVYY_URL}/geo/1.0/reverse", params=params)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200
