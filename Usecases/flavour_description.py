import random

from Usecases import *
from Usecases.flavour_choose import get_flavour_names
from data_source import find
from data_source.flavour_getters import *
from data_source.tea_getters import *


def find_flavour_by_name(name, flavours):
    func = lambda flavour: flavour["name"] == name
    return find(func, flavours)


def handle(message: str):
    text = message.lower()
    flavours = get_flavours()
    target_flavour = find_flavour_by_name(text, flavours)
    descriptions = target_flavour["description"]
    return random.choice(descriptions) + "\n" + render_flavours(target_flavour)


def render_flavours(flavour):
    teas = get_teas()
    flavour_id = get_id(flavour)
    filtered_teas = filter(lambda tea: get_flavour(tea) == flavour_id, teas)
    tea_names = map(get_name, filtered_teas)
    random.shuffle(tea_names)

    return "Попробуйте " + tea_names[0]


predicate = make_word_in_list_predicate(get_flavour_names())


def markup():
    return None
