from Usecases import *
from data_source import ALIVE, QUIET, TEA_CONDITION

TEA_CONDITION = {
    ALIVE: "пей шу и все остальные чаи",
    QUIET: "габа - твой выбор"
}


def handle(message: str):
    text = message.lower()
    return TEA_CONDITION[text]


predicate = make_word_in_list_predicate([ALIVE, QUIET])


def markup():
    return None
