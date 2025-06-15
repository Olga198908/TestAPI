import requests

API_KLYUCH = "feede04274cb8bb3f089d0da039d00e4"  # 🔑 Вставьте сюда ваш API-ключ
BAZOVYY_URL = "https://api.openweathermap.org"

def pechat_otveta(nazvanie, otvet):
    print(f"\n=== {nazvanie} ===")
    print(f"Статус ответа: {otvet.status_code}")
    print("Тело ответа:", otvet.json())

def tekushchaya_pogoda_po_gorodu(gorod):
    # Текущая погода по названию города
    url = f"{BAZOVYY_URL}/data/2.5/weather"
    parametry = {
        "q": gorod,
        "appid": API_KLYUCH,
        "units": "metric"
    }
    pechat_otveta(f"Текущая погода в городе {gorod}", requests.get(url, params=parametry))

def gruppa_pogody_po_id(id_gorodov):
    # Групповой запрос погоды по ID городов
    url = f"{BAZOVYY_URL}/data/2.5/group"
    parametry = {
        "id": ",".join(map(str, id_gorodov)),
        "appid": API_KLYUCH,
        "units": "metric"
    }
    pechat_otveta("Групповая погода по ID городов", requests.get(url, params=parametry))

def geokodirovanie(gorod):
    # Прямое геокодирование по названию города
    url = f"{BAZOVYY_URL}/geo/1.0/direct"

def obratnoe_geokodirovanie(shirota, dolgota):
    # Обратное геокодирование по координатам
    url = f"{BAZOVYY_URL}/geo/1.0/reverse"

def prognoz_na_5_dney(gorod):
    # Прогноз на 5 дней по городу
    url = f"{BAZOVYY_URL}/data/2.5/forecast"

def zagryaznenie_vozdukha(shirota, dolgota):
    # Текущий уровень загрязнения воздуха по координатам
    url = f"{BAZOVYY_URL}/data/2.5/air_pollution"


# === Примеры вызова функций ===
tekushchaya_pogoda_po_gorodu("Moscow")
gruppa_pogody_po_id([524901, 703448, 2643743])  # Москва, Киев, Лондон
