import json
from pymongo import MongoClient
import os

MongoDBURL=os.environ["DB_URL"]
client=MongoClient(MongoDBURL)

# VEGETABLE заменен на BREAD, BLACK заменен на GABA и расположен под тёмным улуном, YELLOW удален
GREEN = "зелёный"
WHITE = "белый"
HELL_TURQUOIS = "светлый улун"
DARK_TURQUOIS = "тёмный улун"
GABA = "габа улун"
RED = "красный"
SHEN = "шен пуэр"
SHU = "шу пуэр"

TEA_CHOOSE_CATEGORY = "по категории"
TEA_CHOOSE_FLAVOUR = "по вкусу"
TEA_CHOOSE_RANDOM = "мне повезёт"
TEA_CHOOSE_RELATED = "по похожему"

VEGAN = "растительный"
SWEET = "сладко-кондитерский"
BERRY = "кисло-ягодный"
FRUIT = "фруктовый"
FLOWER = "цветочный"
BREAD = "хлебный"
NUTS = "ореховый"
SPICY = "пряный"
TREE = "древесный"

ALIVE = "бодрящий"
QUIET = "успокаивающий"

TEA_CONDITION = {
    ALIVE: "пей шу и все остальные чаи",
    QUIET: "габа - твой выбор"
}


# Utiles
def get_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def map(func, lst):
    new_lst=[]
    for x in lst:
        new_lst.append(func(x))
    return new_lst

def filter(func, lst):
    new_lst=[]
    for x in lst:
        if func(x) == True:
            new_lst.append(x)
        else:
            continue
    return new_lst

def find(func, lst):
    for x in lst:
        if func(x)==True:
            return x
    return None
