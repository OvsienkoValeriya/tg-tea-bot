from data_source import get_json


def get_flavours():
    return get_json("data_source/category_description.json")["tea_flavour"]


def get_id(flavour):
    return flavour["id"]


def get_name(flavour):
    return flavour["name"]


def get_description(flavour):
    return flavour["description"]
