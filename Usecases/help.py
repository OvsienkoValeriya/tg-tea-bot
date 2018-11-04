from telebot import types

HELP_COMMAND = ["help"]

HELP = "Вот что я умею:\n" + \
       "/start - Начни чайное путешествие\n" + \
       "/by_category - Расскажу о разных видах чая\n" + \
       "/by_flavour - Подберу чай по вкусу\n" + \
       "/by_condition - Помогу достичь чайного состояния\n" + \
       "/by_same - Подберу чай по вашим личным предпочтениям\n" + \
       "/help - Еще раз расскажу о том, что умею\n"


def handle():
    return HELP


def commands():
    return HELP_COMMAND


def predicate(message):
    return False


def markup():
    return None
