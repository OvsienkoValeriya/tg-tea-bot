import requests


url="https://api.telegram.org/bot789845045:AAF4GvK-9DYhedra0Vc47ZPKku93KjNmUAQ/"

from telegram.ext import Updater,
updater = Updater(token="789845045:AAF4GvK-9DYhedra0Vc47ZPKku93KjNmUAQ")
dispatcher = updater.dispatcher

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def startCommand(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, хочешь чаю?")

def textMessage(bot, update):
    response = "Отлично:" + update.message.text
    