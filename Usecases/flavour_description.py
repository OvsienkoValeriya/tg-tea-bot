from Usecases import *
from data_source import VEGAN, SWEET, BERRY, FRUIT, FLOWER, VEGETABLE, NUTS, SPICY, TREE

TEA_FLAVOUR = {
    VEGAN: "Пей зелёнку",
    SWEET: "Любимый чай мамы - женьшень улун",
    BERRY: "Шен",
    FRUIT: "Почувствуйте сирень в Те Гуан Ине",
    FLOWER: "Снова зеленка",
    VEGETABLE: "Шены-ваша судьба",
    NUTS: "Пейте шу и будьте счастливы",
    SPICY: "Темные улуны (их пьет Миша)",
    TREE: "Шу - ваш выбор"
}


def handle(message: str):
    text = message.lower()
    return TEA_FLAVOUR[text]


predicate = make_word_in_list_predicate(
    [VEGAN, SWEET, BERRY, FRUIT, FLOWER, VEGETABLE, NUTS, SPICY, TREE])


def commands():
    return None


def markup():
    return None
