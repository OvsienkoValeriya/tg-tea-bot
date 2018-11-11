from data_source import get_json


def get_categories():
    return get_json("data_source/category_description.json")["tea_category"]


def get_name(category_name):
    return category_name["name"]


def get_description(category):
    return category["description"]
