from data_source import get_json


def get_flavours():
    return get_json("data_source/category_description.json")["tea_flavour"]


def get_name(flavour_name):
    return flavour_name["name"]


def get_description(flavour):
    return flavour["description"]
