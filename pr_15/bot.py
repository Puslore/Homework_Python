import os
import telebot
from datetime import datetime
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from db import create_user, get_user_by_id
from main import BirthInfo


BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user = get_user(message.chat.id)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    if not user:
        button = KeyboardButton('Зарегистрироваться')
        keyboard.add(button)
        bot.send_message(chat_id, 'Здравствуйте! Нажмите на кнопку для регистрации', reply_markup=keyboard)

    else:
        button1 = KeyboardButton("Сколько мне лет?")
        button2 = KeyboardButton('Когда мой день рождения?')
        keyboard.add(button1, button2)
        bot.send_message(chat_id, 'Что вы хотите узнать?', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text =='Зарегистрироваться')
def reg_birthdate(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Введите вашу дату рождения (ДД-ММ-ГГГГ или ДД/ММ/ГГГГ или ДД.ММ.ГГГГ)')
    bot.register_next_step_handler(message,  chat_id, db)

def db(message, chat_id):
    try:
        if datetime.strptime(message.text, '%d-%m-%Y').date():
            birthdate = str(datetime.strptime(message.text, '%d-%m-%Y').date())

        elif datetime.strptime(message.text, '%d/%m/%Y').date():
            birthdate = str(datetime.strptime(message.text, '%d/%m/%Y').date())

        elif datetime.strptime(message.text, '%d.%m.%Y').date():
            birthdate = str(datetime.strptime(message.text, '%d.%m.%Y').date())

        else:
            raise ValueError

        user = create_user(id=chat_id, birthdate=birthdate)
        
        if user:
            bot.send_message(message.chat.id, f'Вы успешно зарегистрированы! Дата рождения: {birthdate}')
            bot.register_next_step_handler(message, start)

        else:
            bot.send_message(message.chat.id, f'Ошибка регистрации. Проверьте данные или попробуйте позже')
            bot.register_next_step_handler(message, start)

    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат даты. Попробуйте еще раз.')
        bot.register_next_step_handler(message, reg_birthdate)


def get_user(id):
    try:
        user_id = id
        user = get_user_by_id(user_id)

        if user:
            return user

        else:
            bot.send_message(id, f'Пользователь не найден')
        
    except ValueError:
        bot.send_message(id, f'Пользователь не найден, ошибка айди')
    
    except Exception as err:
        bot.send_message(id, f'Ошибка! Попробуйте позже')


@bot.message_handler(func=lambda message: message.text =='Сколько мне лет?')
def calculate_age(message):
    user = get_user(message.chat.id)

    try:
        if user:
            birthdate = user.birthdate
            bot.send_message(message.chat.id, f'{user.birthdate} first')
            age = BirthInfo(birthdate).age()
            bot.send_message(message.chat.id, f'{age} second')
            bot.send_message(message.chat.id, f'Вам {age} лет.')

        else:
            bot.send_message(message.chat.id, 'Вы не зарегистрированы. Используйте /register для регистрации.')
        
        bot.send_message(message.chat.id, f'без понятия в чем проблема')
    finally:
        bot.send_message(message.chat.id, f'{user.birthdate} finally')


@bot.message_handler(func=lambda message: message.text =='Когда мой день рождения?')
def days_to_birthday(message):
    user = get_user(message.chat.id)

    if user:
        birthdate = user.birthdate
        days_left = BirthInfo(birthdate).days_until_birthday()
        bot.send_message(message.chat.id, f'До вашего дня рождения осталось {days_left} дней.')
    else:
        bot.send_message(message.chat.id, 'Вы не зарегистрированы. Используйте /register для регистрации.')


bot.polling(none_stop=True)
