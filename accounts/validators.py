import re


def validate_email(email):
    return True


def email_exists(email):
    return validate_email(email)


def email_validator(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(pattern, email) and email_exists(email)


def phone_number_validator(phone):
    pattern = r"\+254\w{9}"
    return re.match(pattern, phone)
