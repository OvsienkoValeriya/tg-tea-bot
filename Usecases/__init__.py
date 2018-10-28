import telebot
from telebot import types

GREEN = "зелёный"
WHITE = "белый"
HELL_TURQUOIS = "светлый улун"
DARK_TURQUOIS = "тёмный улун"
RED = "красный"
SHEN = "шен пуэр"
SHU = "шу пуэр"
BLACK = "чёрный хэй ча"
YELLOW = "жёлтый"

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
TEA_CHOOSE_CATEGORY = "по категории"
TEA_CHOOSE_FLAVOUR = "по вкусу"
TEA_CHOOSE_CONDITION = "по состоянию"
TEA_CHOOSE_RELATED = "по похожему"

VEGAN = "растительный"
SWEET = "сладко-кондитерский"
BERRY = "кисло-ягодный"
FRUIT = "фруктовый"
FLOWER = "цветочный"
VEGETABLE = "овощной"
NUTS = "ореховый"
SPICY = "пряный"
TREE = "древесный"

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

ALIVE = "бодрящий"
QUIET = "успокаивающий"

TEA_CONDITION = {
    ALIVE: "пей шу и все остальные чаи",
    QUIET: "габа - твой выбор"
}
def make_word_in_list_predicate(lst):
    return lambda message: message.text.lower() in lst


# делаем из списка слов кнопки и добавляем их в markup
def fill_markup_with_words(markup, lst):
    for word in lst:
        markup.add(types.KeyboardButton(word))
    return markup


#
# меню по категориям подбора
#

def tea_choose_make_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    tea_choose = [TEA_CHOOSE_CATEGORY, TEA_CHOOSE_FLAVOUR, TEA_CHOOSE_CONDITION, TEA_CHOOSE_RELATED]
    return fill_markup_with_words(markup, tea_choose)


tea_menu_predicate = make_word_in_list_predicate([TEA_CHOOSE_CATEGORY])


# меню по типу чая
def tea_menu_make_markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    tea_words = [GREEN, WHITE, HELL_TURQUOIS, DARK_TURQUOIS, RED, SHEN, SHU, BLACK, YELLOW]
    capitalized_tea_words = []
    for tea_word in tea_words:
        capitalized_tea_words.append(tea_word.capitalize())
    return fill_markup_with_words(markup, capitalized_tea_words)


tea_menu_choose_predicate = make_word_in_list_predicate(
    [GREEN, WHITE, HELL_TURQUOIS, DARK_TURQUOIS, RED, SHEN, SHU, BLACK, YELLOW])


# меню по типу чая. отображение описания
def handle_tea_type(message: str):
    text = message.lower()
    return TEA_DESCRIPTION[text]


# меню по вкусам чая
def tea_flavour_make_markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    tea_flavours = [VEGAN, SWEET, BERRY, FRUIT, FLOWER, VEGETABLE, NUTS, SPICY, TREE]
    capitalized_tea_flavours = []
    for tea_flavour in tea_flavours:
        capitalized_tea_flavours.append(tea_flavour.capitalize())
    return fill_markup_with_words(markup, capitalized_tea_flavours)


tea_flavour_predicate = make_word_in_list_predicate([TEA_CHOOSE_FLAVOUR])

tea_flavour_choose_predicate = make_word_in_list_predicate(
    [VEGAN, SWEET, BERRY, FRUIT, FLOWER, VEGETABLE, NUTS, SPICY, TREE])


# меню по вкусам чая. отображение описания
def handle_tea_flavour(message: str):
    text = message.lower()
    return TEA_FLAVOUR[text]

#меню по состоянию
tea_condition_predicate = make_word_in_list_predicate([TEA_CHOOSE_CONDITION])

def tea_condition_make_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    tea_conditions = [ALIVE, QUIET]
    capitalized_tea_conditions = []
    for tea_condition in tea_conditions:
        capitalized_tea_conditions.append(tea_condition.capitalize())
    return fill_markup_with_words(markup, capitalized_tea_conditions)

tea_condition_choose_predicate = make_word_in_list_predicate([ALIVE, QUIET])

#меню по состоянию. отображение описания
def handle_tea_condition(message:str):
    text = message.lower()
    return TEA_CONDITION[text]

#меню по стостоянию
tea_related_predicate = make_word_in_list_predicate([TEA_CHOOSE_RELATED])