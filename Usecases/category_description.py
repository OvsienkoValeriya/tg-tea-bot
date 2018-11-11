import random

from Usecases import *
from Usecases.category_choose import get_category_names
from data_source import find
from data_source.category_getters import *


def find_category_by_name(name, categories):
    func = lambda category: category["name"] == name
    return find(func, categories)


def handle(message: str):
    text = message.lower()
    categories = get_categories()
    target_category = find_category_by_name(text, categories)
    descriptions = target_category["description"]
    return random.choise(descriptions)


predicate = make_word_in_list_predicate(get_category_names())


def markup():
    return None
