import telebot
import Usecases.category_choose
import Usecases.category_description
import Usecases.condition_choose
import Usecases.condition_description
import Usecases.easter_egg
import Usecases.flavour_choose
import Usecases.flavour_description
import Usecases.help
import Usecases.welcome
import Usecases.sameness_choose

TOKEN = "789845045:AAF4GvK-9DYhedra0Vc47ZPKku93KjNmUAQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=Usecases.help.commands())
@bot.message_handler(func=Usecases.help.predicate)
def send_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.help.handle(), reply_markup=Usecases.help.markup())


@bot.message_handler(commands=Usecases.welcome.commands())
@bot.message_handler(func=Usecases.welcome.predicate)
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
@bot.message_handler(commands=Usecases.category_description.commands())
def send_tea_menu_choose(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text=Usecases.category_description.handle(message.text),
                     reply_markup=Usecases.category_description.markup())


# по вкусу
@bot.message_handler(commands=Usecases.flavour_choose.commands())
@bot.message_handler(func=Usecases.flavour_choose.predicate)
def send_flavour_menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.flavour_choose.handle(), reply_markup=Usecases.flavour_choose.markup())


# по вкусу. показывает текст после выбора
@bot.message_handler(func=Usecases.flavour_description.predicate)
@bot.message_handler(commands=Usecases.flavour_description.commands())
def send_tea_flavour_choose(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text=Usecases.flavour_description.handle(message.text),
                     reply_markup=Usecases.flavour_description.markup())


# по состоянию
@bot.message_handler(commands=Usecases.condition_choose.commands())
@bot.message_handler(func=Usecases.condition_choose.predicate)
def send_predicate_menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.condition_choose.handle(), reply_markup=Usecases.condition_choose.markup())


# по состоянию. показывает текст
@bot.message_handler(func=Usecases.condition_description.predicate)
@bot.message_handler(commands=Usecases.condition_description.commands())
def send_tea_condition(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text=Usecases.condition_description.handle(message.text),
                     reply_markup=Usecases.condition_description.markup())


# по похожему
@bot.message_handler(commands=Usecases.sameness_choose.commands())
@bot.message_handler(func=Usecases.sameness_choose.predicate)
def send_sorry(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.sameness_choose.handle(), reply_markup=Usecases.sameness_choose.markup())


# пасхалка
@bot.message_handler(func=Usecases.easter_egg)
@bot.message_handler(commands=Usecases.easter_egg.commands())
def send_easter_egg(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, Usecases.easter_egg.handle(), reply_markup=Usecases.easter_egg.markup())


# запускает бота
bot.polling()
