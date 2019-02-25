from threading import Timer
import time
from telebot import types

def markup():
    markup = types.ReplyKeyboardMarkup(row_width=5)
    return fill_markup(markup)

def fill_markup(markup, lst):
    buttons = []
    for number in lst:
        buttons.append(types.KeyboardButton(number))
    markup.add(buttons)
    return markup

def timer_maker(bot):
    def timer():
        t = Timer(TIME_TO_SEND, timeout, args=[bot])
        t.start()
    return timer

def timeout(bot):
    bot.send_message()

TIME_TO_SEND = 12*60*60