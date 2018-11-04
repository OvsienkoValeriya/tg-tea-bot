from Usecases import *
from data_source import ALIVE, QUIET, TEA_CHOOSE_CONDITION

CONDITION_COMMAND = ['by_condition']


def handle():
    return "Тогда выбери состояние"


def commands():
    return CONDITION_COMMAND


def markup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    tea_conditions = [ALIVE, QUIET]
    return fill_markup_with_words(markup, capitalize_all(tea_conditions))


predicate = make_word_in_list_predicate([TEA_CHOOSE_CONDITION])
