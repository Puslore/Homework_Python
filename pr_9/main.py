# Task 9 - OpenWeather

import os
import requests
import telebot
from datetime import  datetime
import pytz


BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")
print(BOT_TOKEN)
bot = telebot.TeleBot(BOT_TOKEN)


def logging(usr, msg):
    with open('logs.txt', 'a') as file:
        file.write(f'{usr} : {msg} {datetime.now(tz=pytz.timezone("Asia/Irkutsk")).today()}\n')
    return True

def get_weather(city):
    try:
        req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric")
        data = req.json()
        weather = {
            'temp': data["main"]["temp"],
            'pressure': data["main"]["pressure"],
            'wind_speed': data["wind"]["speed"]
        }
        weather_unpack = dict_unpack(weather, city)
        return weather_unpack
    except:
        err_msg = 'Проверьте название города - возможно вы ошиблись'
        return err_msg

def dict_unpack(dict_, city):
    string_ = (f'Температура в городе {city}: {dict_["temp"]}° по Цельсию\n'
               f'Давление: {dict_["pressure"]} HPA\nСкорость ветра: {dict_["wind_speed"]} метра в секунду')
    return string_


@bot.message_handler(commands=['start'])
def start_message(message):
    logging(message.chat.first_name, message.text)
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}! Напиши название города, в котором хочешь узнать погоду')

@bot.message_handler(content_types=['text'])
def send_weather(message):
    weather = get_weather(message.text)
    bot.send_message(message.chat.id, weather)
    logging(message.chat.first_name, message.text)

bot.infinity_polling()
