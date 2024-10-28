import os

import requests

# paste token from forlabs
WEATHER_TOKEN = "299147b63c1c74d4df3eaea5fd7cfc3a"

def get_weather():
    try:
        city = input('Введите название города на русском языке: ')
        req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric", )
        data = req.json()
        weather = data["main"]["temp"]
        print(f"Погода в городе {city}: {weather} по шкале Цельсия")
    except:
        print("Проверьте название города")

get_weather()
