from telebot import types
from Usecases import *
from data_source import VEGAN, SWEET, BERRY, FRUIT, FLOWER, VEGETABLE, NUTS, SPICY, TREE, TEA_CHOOSE_FLAVOUR

FLAVOUR_COMMAND = ["by_flavour"]


def handle():
    return "Тогда выбери вкус"


def commands():
    return FLAVOUR_COMMAND


def markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    tea_flavours = [VEGAN, SWEET, BERRY, FRUIT, FLOWER, VEGETABLE, NUTS, SPICY, TREE]
    return fill_markup_with_words(markup, capitalize_all(tea_flavours))


predicate = make_word_in_list_predicate([TEA_CHOOSE_FLAVOUR])
