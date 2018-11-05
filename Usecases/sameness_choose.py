from Usecases import *
from data_source import TEA_CHOOSE_RELATED

SAME_COMMAND = ["by_same"]


def commands():
    return SAME_COMMAND


def handle():
    return "Раздел находится в разработке"


def markup():
    return None


predicate = make_word_in_list_predicate([TEA_CHOOSE_RELATED])
