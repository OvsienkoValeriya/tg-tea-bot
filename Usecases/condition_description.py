import random

from Usecases import *
from Usecases.condition_choose import get_condition_names
from data_source import find, filter, map
from data_source.condition_getters import *
from data_source.tea_getters import *


def find_condition_by_name(name, conditions):
    func = lambda condition: condition["name"] == name
    return find(func, conditions)


def handle(message: str):
    text = message.lower()
    conditions = get_conditions()
    target_condition = find_condition_by_name(text, conditions)
    descriptions = target_condition["description"]
    return random.choice(descriptions) + "\n" + render_condition(target_condition)

def render_condition(condition):
    teas = get_teas()
    condition_id = get_id(condition)
    filtered_teas = filter(lambda tea: get_condition(tea) == condition_id, teas)
    tea_names = map(get_name, filtered_teas)
    random.shuffle(tea_names)

    return "Попробуйте " + tea_names[0]

predicate = make_word_in_list_predicate(get_condition_names())


def markup():
    return None
