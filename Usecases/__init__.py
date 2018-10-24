import telebot
from telebot import types

GREEN = "зеленый"
WHITE = "белый"
HELL_TURQUOIS = "светлый улун"
DARK_TURQUOIS = "темный улун"
RED = "красный"
SHEN = "шен пуэр"
SHU = "шу пуэр"
BLACK = "чёрный хэй ча"
HELP = "что?"

TEA_DESCRIPTION = {
    GREEN: "Зеленый чай самый бодрящий",
    WHITE: "Белый - гербарий",
    HELL_TURQUOIS: "Светлый улун собирают в горах",
    DARK_TURQUOIS: "Темный улун любит Миша",
    RED: "Красный лучше пить осенью"
    SHEN: "Чем старше шен - тем он вкусней",
    SHU: "Шу Пуэр любит Лера",
    BLACK: "На черном чае можно увидеть плесень",
    HELP: "Сейчас я все объясню"
}


def tea_menu_predicate(message):
    text = message.text.lower()
    return text == "какой бывает чай?" or \
        text == "какой чай бывает?" or \
        text == "не знаю"


def tea_menu_make_markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn_green = types.KeyboardButton (GREEN.capitalize())
    itembtn_white = types.KeyboardButton (WHITE.capitalize())
    itembtn_hell_turquois = types.KeyboardButton (HELL_TURQUOIS.capitalize())
    itembtn_dark_turquois = types.KeyboardButton (DARK_TURQUOIS.capitalize())
    itembtn_red = types.KeyboardButton (RED.capitalize())
    itembtn_shen = types.KeyboardButton (SHEN.capitalize())
    itembtn_shu = types.KeyboardButton (SHU.capitalize())
    itembtn_black = types.KeyboardButton (BLACK.capitalize())
    itembtn_help = types.KeyboardButton (HELP.capitalize())
    markup.add (itembtn_green, itembtn_white, itembtn_hell_turquois, itembtn_dark_turquois, itembtn_red, itembtn_shen, itembtn_shu, itembtn_black, itembtn_help)
    return markup

def tea_menu_choose_predicate(message):
    text = message.text.lower()
    return text in [GREEN, WHITE, HELL_TURQUOIS, DARK_TURQUOIS, RED, SHEN, SHU, BLACK, HELP]

def handle_tea_type(message:str):
    text = message.lower()
    return TEA_DESCRIPTION[text]
