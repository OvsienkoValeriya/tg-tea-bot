from data_source import TEA_CHOOSE_CATEGORY, TEA_CHOOSE_FLAVOUR, TEA_CHOOSE_RANDOM, TEA_CHOOSE_RELATED
from telebot import types
from Usecases import *

WELCOME = "Сегодня прекрасный день. Как вам подобрать чай?"

WELCOME_BACK = "Напиши \"Чай\" чтобы вернуться в начало"

WELCOME_COMMAND = ["start"]


def handle():
    return [WELCOME, WELCOME_BACK]


def markup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    tea_choose = [TEA_CHOOSE_CATEGORY, TEA_CHOOSE_FLAVOUR, TEA_CHOOSE_RANDOM, TEA_CHOOSE_RELATED]
    return fill_markup_with_words(markup, capitalize_all(tea_choose))


def commands():
    return WELCOME_COMMAND


predicate = make_word_in_list_predicate(["чай"])