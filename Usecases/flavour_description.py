import random

from Usecases import *
from Usecases.flavour_choose import get_flavour_names
from data_source import find, filter
from data_source.flavour_getters import *
from data_source.tea_getters import *
from data_source.user_getters import update_user


def find_flavour_by_name(name, flavours):
    func = lambda flavour: flavour["name"] == name
    return find(func, flavours)


def handle(id, message: str):
    text = message.lower()
    flavours = get_flavours()
    target_flavour = find_flavour_by_name(text, flavours)
    descriptions = target_flavour["description"]
    tea = random_tea(target_flavour)

    remember_tea(id, tea)
    return random.choice(descriptions) + "\n" + render_flavours(target_flavour)


def remember_tea(id, tea):
    update_user(id, get_name(tea))


def random_tea(flavours):
    teas = get_teas()
    flavours_id = get_id(flavours)
    filtered_teas = filter(lambda tea: flavours_id in get_flavour(tea), teas)
    tea = random.choice(filtered_teas)
    return tea


def render_flavours(tea):
    return "Попробуйте " + get_name(tea) + ".\n" + get_description(tea)


predicate = make_word_in_list_predicate(get_flavour_names())


def markup():
    return None
