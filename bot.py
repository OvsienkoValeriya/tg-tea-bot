import telebot
from telebot import types
from Usecases import *

TOKEN = "789845045:AAF4GvK-9DYhedra0Vc47ZPKku93KjNmUAQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Сегодня прекрасный день. Как вам подобрать чай?", reply_markup=tea_choose_make_markup())

#по категории. показывает меню
@bot.message_handler(commands=['by_category'])
@bot.message_handler(func=tea_menu_predicate)
def send_tea_menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Тогда выбери категорию", reply_markup=tea_menu_make_markup())

#по категории. показывает текст после выбора
@bot.message_handler(func=tea_menu_choose_predicate)
def send_tea_menu_choose(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text=handle_tea_type(message.text))

#по вкусу
@bot.message_handler(commands = ['by_flavour'])
@bot.message_handler(func=tea_flavour_predicate)
def send_flavour_menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Тогда выбери категорию", reply_markup=tea_flavour_make_markup())

#по вкусу. показывает текст после выбора
@bot.message_handler(func=tea_flavour_choose_predicate)
def send_tea_flavour_choose(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text=handle_tea_flavour(message.text))

#по состоянию
@bot.message_handler(commands = ['by_condition'])
@bot.message_handler(func=tea_condition_predicate)
def send_predicate_menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Тогда выбери категорию", reply_markup=tea_condition_make_markup())

#по похожему
@bot.message_handler(commands = ['by_same'])
@bot.message_handler(func=tea_related_predicate)
def send_sorry(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Раздел находится в разработке")


#пасхалка
@bot.message_handler(regexp="(Я|я) (С|с)аша")
def send_easter_egg(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Тогда пей вискарь и не выебывайся")


# запускает бота
bot.polling()
