from telebot import types
from data_source import GREEN, WHITE, HELL_TURQUOIS, DARK_TURQUOIS, RED, SHEN, SHU, BLACK, YELLOW, TEA_CHOOSE_CATEGORY
from Usecases import *

CATEGORY_COMMAND = ["by_category"]


def handle():
    return "Тогда выбери категорию"


def commands():
    return CATEGORY_COMMAND


def markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    tea_words = [GREEN, WHITE, HELL_TURQUOIS, DARK_TURQUOIS, RED, SHEN, SHU, BLACK, YELLOW]
    return fill_markup_with_words(markup, capitalize_all(tea_words))


predicate = make_word_in_list_predicate([TEA_CHOOSE_CATEGORY])
