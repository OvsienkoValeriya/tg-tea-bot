from data_source import get_json


def get_teas():
    return get_json("tea_passport.json")["teas"]


# get teaProperties

def get_name(tea):
    return tea["name"]


def get_translation(tea):
    return tea["translation"]


def get_category(tea):
    return tea["category"]


def get_flavour(tea):
    return tea["flavour"]


def get_condition(tea):
    return tea["condition"]


def get_description(tea):
    return tea["description"]
