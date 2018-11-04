from telebot import types


def make_word_in_list_predicate(lst):
    return lambda message: message.text.lower() in lst


# делаем из списка слов кнопки и добавляем их в markup
def fill_markup_with_words(markup, lst):
    list_of_buttons = []
    for word in lst:
        list_of_buttons.append(types.KeyboardButton(word))
    markup.add(*list_of_buttons)
    return markup


# все пишем с большой буквы
def capitalize_all(lst):
    capitalized_lst = []
    for word in lst:
        capitalized_lst.append(word.capitalize())
    return capitalized_lst
