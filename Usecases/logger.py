def log_message(message):
    print("Message arrived:",message.text)

def log_unresolved_message(message):
    print("Message not recognized:", message.text)

def predicate(message):
    return True