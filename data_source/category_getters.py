from data_source import get_json


def get_categories():
    return get_json("data_source/category_description.json")["tea_category"]


def get_id(category):
    return category["id"]


def get_name(category):
    return category["name"]


def get_description(category):
    return category["description"]
