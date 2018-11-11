from telebot import types
from Usecases import *
from data_source import map, TEA_CHOOSE_FLAVOUR
from data_source.flavour_getters import *

FLAVOUR_COMMAND = ["by_flavour"]


def handle():
    return "Тогда выбери вкус"


def commands():
    return FLAVOUR_COMMAND


def markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    tea_flavours = get_flavour_names()
    return fill_markup_with_words(markup, capitalize_all(tea_flavours))

def get_flavour_names():
    flavours = get_flavours
    names = map (get_name, flavours)
    return names


predicate = make_word_in_list_predicate([TEA_CHOOSE_FLAVOUR])
