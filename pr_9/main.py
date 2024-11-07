# Task 9 - OpenWeather

import requests
import telebot
import os
from datetime import datetime
import pytz


# Paste tokens from Forlabs


# BOT_TOKEN = os.getenv("BOT_TOKEN")
# WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")
# NASA_TOKEN = os.getenv("NASA_TOKEN")

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


def answer_for_not_a_text(user):
    bot.send_message(f'{user}, я не могу понять, о чем идет речь.')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,f'Привет, {message.chat.first_name}! Напиши название города, в котором хочешь узнать погоду.')


@bot.message_handler(func=lambda message: message.text is not None)
def send_weather(message):
    city = message.text.strip()
    user = message.chat.first_name
    weather = get_weather(city, user)
    bot.send_message(message.chat.id, weather)


@bot.message_handler(func=lambda message: message.text is None)
def non_text(message):
    user = message.chat.first_name
    bot.send_message(f'{user}, я не могу понять, о чем идет речь.')


bot.infinity_polling()
