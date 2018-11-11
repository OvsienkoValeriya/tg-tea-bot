import random

from Usecases import *
from Usecases.category_choose import get_category_names
from data_source import find, filter, map
from data_source.category_getters import *
from data_source.tea_getters import *


def find_category_by_name(name, categories):
    func = lambda category: category["name"] == name
    return find(func, categories)


def handle(message: str):
    text = message.lower()
    categories = get_categories()
    target_category = find_category_by_name(text, categories)
    descriptions = target_category["description"]
    return random.choice(descriptions) + "\n" + render_tea(target_category)


def render_tea(category):
    teas = get_teas()
    category_id = get_id(category)
    filtered_teas = filter(lambda tea: get_category(tea) == category_id, teas)
    tea_names = map(get_name, filtered_teas)
    random.shuffle(tea_names)

    return "Попробуйте " + tea_names[0]


predicate = make_word_in_list_predicate(get_category_names())


def markup():
    return None
