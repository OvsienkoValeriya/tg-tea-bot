from telebot import types
from data_source.category_getters import *
from data_source import map, TEA_CHOOSE_CATEGORY
from Usecases import *

CATEGORY_COMMAND = ["by_category"]


def handle():
    return "Тогда выбери категорию"


def commands():
    return CATEGORY_COMMAND


def markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    tea_words = get_category_names()
    return fill_markup_with_words(markup, capitalize_all(tea_words))

def get_category_names():
    categories = get_categories()
    names = map(get_name, categories)
    return names


predicate = make_word_in_list_predicate([TEA_CHOOSE_CATEGORY])
