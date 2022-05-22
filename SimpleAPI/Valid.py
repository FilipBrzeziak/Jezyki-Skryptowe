import re


def valid_email(email):
    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[pwr]+\.[edu]+\.[pl]{2,}\b', email):
        name = str(re.split("@", email, maxsplit=1)[0])
        return True
    else:
        return False


def valid_number(phone_nuber):
    if (re.fullmatch(r'^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{3}', phone_nuber)) or (
            re.fullmatch(r'[\dA-Z]{3} [\dA-Z]{3} [\dA-Z]{3}', phone_nuber)) or (
            re.fullmatch(r'[+]48+[ ]+[\dA-Z]{9}', phone_nuber)) or (
            re.fullmatch(r'[+]48+[ ]+[\dA-Z]{3} [\dA-Z]{3} [\dA-Z]{3}', phone_nuber)):
        return True
    else:
        return False