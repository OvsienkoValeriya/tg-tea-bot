import random

from Usecases import *
from Usecases.condition_choose import get_condition_names
from data_source import find
from data_source.condition_getters import *


def find_condition_by_name(name, conditions):
    func = lambda condition: condition["name"] == name
    return find(func, conditions)


def handle(message: str):
    text = message.lower()
    conditions = get_conditions()
    target_category = find_condition_by_name(text, conditions)
    descriptions = target_category["description"]
    return random.choice(descriptions)


predicate = make_word_in_list_predicate(get_condition_names())


def markup():
    return None
