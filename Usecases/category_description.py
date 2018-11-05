from data_source import GREEN, WHITE, HELL_TURQUOIS, DARK_TURQUOIS, RED, SHEN, SHU, BLACK, YELLOW
from Usecases import *

TEA_DESCRIPTION = {
    GREEN: "Зеленый чай самый бодрящий",
    WHITE: "Белый - гербарий",
    HELL_TURQUOIS: "Светлый улун собирают в горах",
    DARK_TURQUOIS: "Темный улун любит Миша",
    RED: "Красный лучше пить осенью",
    SHEN: "Чем старше шен - тем он вкусней",
    SHU: "Шу Пуэр любит Лера",
    BLACK: "На черном чае можно увидеть плесень",
    YELLOW: "Желтый - очень дорогой"
}


def handle(message: str):
    text = message.lower()
    return TEA_DESCRIPTION.get(text, "Я вас не понимаю")


predicate = make_word_in_list_predicate([GREEN, WHITE, HELL_TURQUOIS, DARK_TURQUOIS, RED, SHEN, SHU, BLACK, YELLOW])


def commands():
    return None


def markup():
    return None
