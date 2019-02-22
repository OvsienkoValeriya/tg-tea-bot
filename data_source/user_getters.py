from data_source import *

USERS = client.get_default_database()["users"]


def insert_user(id, tea_list):
    user = {"_id": id, "tea_list": tea_list}
    USERS.insert_one(user)


def get_user(id):
    user_query = {"_id": id}
    user = USERS.find_one(user_query)
    return user


def update_user(id, new_tea):
    user = get_user(id)
    if user is not None:
        tea_list = user["tea_list"] + [new_tea]
        delete_user(id)
        insert_user(id, tea_list)
    else:
        insert_user(id, [new_tea])


def delete_user(id):
    user_query = {"_id": id}
    USERS.delete_one(user_query)


def get_users():
    return map(lambda user:user["_id"], USERS.find())