import os

import telebot

import Usecases.category_choose
import Usecases.category_description
import Usecases.easter_egg
import Usecases.flavour_choose
import Usecases.flavour_description
import Usecases.help
import Usecases.logger
import Usecases.random_choose
import Usecases.sameness_choose
import Usecases.welcome
import Usecases.push_message

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=Usecases.help.commands())
def send_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.help.handle(), reply_markup=Usecases.help.markup())


@bot.message_handler(commands=Usecases.welcome.commands())
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.welcome.handle(), reply_markup=Usecases.welcome.markup())


# по категории. показывает меню
@bot.message_handler(commands=Usecases.category_choose.commands())
@bot.message_handler(func=Usecases.category_choose.predicate)
def send_category_choose(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.category_choose.handle(), reply_markup=Usecases.category_choose.markup())


# по категории. показывает текст после выбора
@bot.message_handler(func=Usecases.category_description.predicate)
def send_tea_menu_choose(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text=Usecases.category_description.handle(chat_id, message.text),
                     reply_markup=Usecases.category_description.markup())


# по вкусу
@bot.message_handler(commands=Usecases.flavour_choose.commands())
@bot.message_handler(func=Usecases.flavour_choose.predicate)
def send_flavour_menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.flavour_choose.handle(), reply_markup=Usecases.flavour_choose.markup())


# по вкусу. показывает текст после выбора
@bot.message_handler(func=Usecases.flavour_description.predicate)
def send_tea_flavour_choose(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text=Usecases.flavour_description.handle(chat_id, message.text),
                     reply_markup=Usecases.flavour_description.markup())


# по воле божьей
@bot.message_handler(commands=Usecases.random_choose.commands())
@bot.message_handler(func=Usecases.random_choose.predicate)
def send_predicate_menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.random_choose.handle(chat_id), reply_markup=Usecases.random_choose.markup())


# по похожему
@bot.message_handler(commands=Usecases.sameness_choose.commands())
@bot.message_handler(func=Usecases.sameness_choose.predicate)
def send_sorry(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.sameness_choose.handle(), reply_markup=Usecases.sameness_choose.markup())

def send_messages(message, user_ids):
    for id in user_ids:
        bot.send_message(id, "test")

# рассылка
@bot.message_handler(commands=Usecases.push_message.commands())
def messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.push_message.handle(id, message.text, send_messages ))


# пасхалка
@bot.message_handler(func=Usecases.easter_egg.predicate)
@bot.message_handler(commands=Usecases.easter_egg.commands())
def send_easter_egg(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.easter_egg.handle(), reply_markup=Usecases.easter_egg.markup())


@bot.message_handler(func=Usecases.logger.predicate)
def log_message(message):
    Usecases.logger.log_unresolved_message(message)


def log_all(messages):
    for message in messages:
        Usecases.logger.log_message(message)


bot.set_update_listener(log_all)

# запускает бота
bot.polling()
