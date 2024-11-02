# Task 9 - OpenWeather

import requests
import telebot


BOT_TOKEN = ''
WEATHER_TOKEN = ''
bot = telebot.TeleBot(BOT_TOKEN)


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
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}! Напиши название города, в котором хочешь узнать погоду')

@bot.message_handler(content_types=['text'])
def send_weather(message):
    weather = get_weather(message.text)
    bot.send_message(message.chat.id, weather)

bot.infinity_polling()
