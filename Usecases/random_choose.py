import random
from data_source.user_getters import update_user
from Usecases import *
from data_source import TEA_CHOOSE_RANDOM
from data_source.tea_getters import *

RANDOM_COMMAND = ['random']


def handle(id):
    teas = get_teas()
    tea = random.choice(teas)
    remember_tea(id,tea)
    return "Попробуйте " + get_name(tea) + "\n" + get_description(tea)

def remember_tea(id, tea):
    update_user(id, get_name (tea))


def commands():
    return RANDOM_COMMAND


def markup():
    return None


predicate = make_word_in_list_predicate([TEA_CHOOSE_RANDOM])
