import telebot
from telebot import types

TOKEN = "789845045:AAF4GvK-9DYhedra0Vc47ZPKku93KjNmUAQ"
bot = telebot.TeleBot(TOKEN)


def tea_menu_predicate(message):
    text = message.text.lower()
    return text == "какой бывает чай?" or \
        text == "какой чай бывает?" or \
        text == "не знаю"


def tea_menu_make_markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn_green = types.KeyboardButton ("Зеленый")
    itembtn_white = types.KeyboardButton ("Белый")
    itembtn_hell_turquois = types.KeyboardButton ("Светлый Улун")
    itembtn_dark_turquois = types.KeyboardButton ("Темный Улун")
    itembtn_red = types.KeyboardButton ("Красный")
    itembtn_shen = types.KeyboardButton ("Шен Пуэр")
    itembtn_shu = types.KeyboardButton ("Шу Пуэр")
    itembtn_black = types.KeyboardButton ("Чёрный Хэй Ча")
    itembtn_help = types.KeyboardButton ("Что?")
    markup.add (itembtn_green, itembtn_white, itembtn_hell_turquois, itembtn_dark_turquois, itembtn_red, itembtn_shen, itembtn_shu, itembtn_black, itembtn_help)
    return markup

