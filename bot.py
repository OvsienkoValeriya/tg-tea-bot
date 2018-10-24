import telebot
from telebot import types
from Usecases import *

TOKEN = "789845045:AAF4GvK-9DYhedra0Vc47ZPKku93KjNmUAQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id= message.chat.id
    bot.send_message(chat_id, "Привет, какого хочешь чаю?")

@bot.message_handler(commands=['tea_menu'], func=tea_menu_predicate)
def send_tea_menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Выбери вариант")


@bot.message_handler(regexp="(Я|я) (С|с)аша")
def send_easter_egg(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Тогда пей вискарь и не выебывайся")


@bot.message_handler(func=lambda m: not tea_menu_predicate(m))
def send_message(message):
    chat_id= message.chat.id
    bot.send_message(chat_id, "Отлично:" + message.text)

bot.polling()