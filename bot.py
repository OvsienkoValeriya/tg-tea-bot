import telebot

TOKEN = "789845045:AAF4GvK-9DYhedra0Vc47ZPKku93KjNmUAQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id= message.chat.id
    bot.send_message(chat.id, "Привет, какого хочешь чаю?")


@bot.message_handler(func=lambda m: True)
def send_message(message):
    chat_id= message.chat.id
    bot.send_message(chat.id, "Отлично:" + message.text)

bot.polling()