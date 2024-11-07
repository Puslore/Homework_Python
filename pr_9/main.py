# Task 9 and 10 - OpenWeather and NASA APIs

import requests
import telebot
from Cython.Compiler.Errors import message
from telebot import types
import os
from datetime import datetime
import pytz


# Paste tokens from Forlabs
WEATHER_TOKEN = ''
BOT_TOKEN = ''
NASA_TOKEN = ''

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
            return 'Проверьте название города'

    except Exception as err:
        logging(user, f'ERROR: {err}')
        return 'Проверьте название города - возможно вы ошиблись. Возможна ошибка со стороны сервиса.'


def send_weather(message):
    city = message.text.strip()
    user = message.chat.first_name
    weather = get_weather(city, user)
    bot.send_message(message.chat.id, weather, reply_markup=start_buttons())
    bot.send_message(message.chat.id, 'Главное меню')


def dict_unpack(dict_, city):
    return (f'Температура в городе {city}: {dict_["temp"]}°C\n'
            f'Давление: {dict_["pressure"]} HPa\n'
            f'Скорость ветра: {dict_["wind_speed"]} м/с')


def logging(user, message):
    time = datetime.now(tz=pytz.timezone('Asia/Irkutsk')).date()
    with open('./logs.txt', 'a') as file:
        file.write(f'{user} : {message}  {time}\n')


def start_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather_button = types.KeyboardButton('Узнать погоду')
    nasa_button = types.KeyboardButton('Получить фотографию с сайта NASA')
    markup.add(weather_button, nasa_button)
    return markup


def back_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button_ = types.KeyboardButton('Назад')
    markup.add(back_button_)
    return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}! Нажми на нужную кнопку!', reply_markup=start_buttons())


@bot.message_handler(func=lambda message: message.text == 'Узнать погоду')
def ask_city(message):
    bot.send_message(message.chat.id, 'Введите название города:', reply_markup=back_button())
    bot.register_next_step_handler(message, send_weather)


@bot.message_handler(func=lambda message: message.text == 'Получить фотографию с сайта NASA')
def send_nasa_photo(message):
    user = message.chat.first_name
    try:
        req = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_TOKEN}")
        data = req.json()
        photo_url = data['url']

        if photo_url.endswith(('jpg', 'png')):
            bot.send_photo(message.chat.id, photo_url)
        else:
            bot.send_message(message.chat.id, 'Сегодня в NASA только ссылка на фотографию, а не само фото :(. Попробуйте завтра! {photo_url}')

    except Exception as e:
        bot.send_message(message.chat.id, 'Произошла ошибка при получении фотографии.')
        logging(user, 'NASA photo troubles')

    bot.send_message(message.chat.id, "Главное меню.", reply_markup=start_buttons())



@bot.message_handler(func=lambda message: message.text == 'Назад')
def back_to_start(message):
    bot.send_message(message.chat.id, 'Главное меню.', reply_markup=start_buttons())


@bot.message_handler(func=lambda message: message.text is not None)
def not_text(message):
    user = message.chat.first_name
    bot.send_message(message.chat.id, f'{user}, я не могу понять, о чем идет речь.', reply_markup=start_buttons())

bot.infinity_polling()
