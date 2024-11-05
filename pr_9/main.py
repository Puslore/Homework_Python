# Task 9 - OpenWeather

import requests
import telebot
import os
from datetime import datetime
import pytz


BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


def get_weather(city, user):
    try:
        req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric')
        data = req.json()

        if req.status_code == 200 and "main" in data and "wind" in data:
            weather = {
                'temp': data["main"]["temp"],
                'pressure': data["main"]["pressure"],
                'wind_speed': data["wind"]["speed"]
            }
            return dict_unpack(weather, city)

        else:
            return 'Проверьте название города.'

    except Exception as err:
        logging(user, f'ERROR: {err}')
        return 'Проверьте название города - возможно вы ошиблись. Возможна ошибка со стороны сервиса'


def dict_unpack(dict_, city):
    return (f'Температура в городе {city}: {dict_["temp"]}°C\n'
            f'Давление: {dict_["pressure"]} HPa\n'
            f'Скорость ветра: {dict_["wind_speed"]} м/с')


def logging(user, message):
    time = datetime.now(tz=pytz.timezone('Asia/Irkutsk')).date()
    with open('./logs.txt', 'a') as file:
        file.write(f'{user} : {message}  {time}\n')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,f'Привет, {message.chat.first_name}! Напиши название города, в котором хочешь узнать погоду.')


@bot.message_handler(content_types=['text'])
def send_weather(message):
    city = message.text.strip()
    user = message.chat.first_name
    weather = get_weather(city, user)
    bot.send_message(message.chat.id, weather)
    logging(user, city)


bot.infinity_polling()
