from Usecases import *
from data_source import map, TEA_CHOOSE_CONDITION
from data_source.condition_getters import *
import random

CONDITION_COMMAND = ['by_condition']


def handle():
    return "Тогда выбери состояние"


def commands():
    return CONDITION_COMMAND


def markup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    tea_conditions = get_condition_names()
    return fill_markup_with_words(markup, capitalize_all(tea_conditions))

def get_condition_names():
    conditions = get_conditions()
    names = map (get_name, conditions)
    return names

predicate = make_word_in_list_predicate([TEA_CHOOSE_CONDITION])
