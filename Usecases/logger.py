def log_message(message):
    print("Message arrived:",message.text,"from chat:",message.chat.id)

def log_unresolved_message(message):
    print("Message not recognized:", message.text)

def predicate(message):
    return True