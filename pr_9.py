import os

import requests

# paste token from forlabs
WEATHER_TOKEN = ""

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
