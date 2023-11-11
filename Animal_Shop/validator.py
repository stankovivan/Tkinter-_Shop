import string


def password_validator(value):
    result = True
    password = str(value)

    if 5 > len(password):
        result = False

    if 12 < len(password):
        result = False

    if not any(digit.isdigit() for digit in password):
        result = False

    if not any(digit.isupper() for digit in password):
        result = False

    if not any(char.islower() for char in password):
        result = False

    if not any(char in string.punctuation for char in password):
        result = False

    if result:
        return result
    else:
        return result
