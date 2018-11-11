from Usecases import *
from data_source import find
from Usecases.flavour_choose import get_flavour_names
import random
from data_source.flavour_getters import *


def find_flavour_by_name(name, flavours):
    func = lambda flavour: flavour["name"] == name
    return find(func, flavours)

def handle(message: str):
    text = message.lower()
    flavours = get_flavours()
    target_category = find_flavour_by_name(text, flavours)
    descriptions = target_category["description"]
    return random.choice(descriptions)


predicate = make_word_in_list_predicate(get_flavour_names())


def markup():
    return None
