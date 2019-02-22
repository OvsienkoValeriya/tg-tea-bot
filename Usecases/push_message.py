import os

from data_source.user_getters import get_users

PUSH_COMMAND = "send_message"
admin_id = os.environ["ADMIN_ID"]


def commands():
    return [PUSH_COMMAND]


def handle(id, message: str, callback):
    if str(id) == admin_id:
        send_messages(message, callback)
        return "Сообщение отправлено"
    else:
        return "Access denied"


def send_messages(message: str, callback):
    user_ids = get_users()
    command_len = len(PUSH_COMMAND) + 2
    filtered_message = message[command_len:]
    callback(filtered_message, user_ids)
