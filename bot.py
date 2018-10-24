import telebot

TOKEN = "789845045:AAF4GvK-9DYhedra0Vc47ZPKku93KjNmUAQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, хочешь чаю?")


@bot.message_handler(func=lambda m: True)
def send_message(message):
    bot.reply_to(message, "Отлично:" + message.text)

bot.polling()