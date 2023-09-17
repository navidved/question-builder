import re


def validate_phone_number(phone_number):
    if not re.match(r"^(?:\+98|0)?9\d{9}$", phone_number):
        return False
    return True