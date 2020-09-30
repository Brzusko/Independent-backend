

def generate_failed_message(failed_message):
    return {
        "message": failed_message,
        "code": 500
    }


def generate_success_message(message, data = None):
    message_to_generate = {
        "message": message,
        "code": 200
    }
    if data is not None:
        message_to_generate['data'] = data;

    return message_to_generate;