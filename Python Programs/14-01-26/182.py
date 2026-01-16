import re

def analyze_string(text):
    uppercase = re.findall(r'[A-Z]', text)
    lowercase = re.findall(r'[a-z]', text)
    digits = re.findall(r'[0-9]', text)
    special = re.findall(r'[^A-Za-z0-9]', text)

    return {
        "uppercase": uppercase,
        "lowercase": lowercase,
        "digits": digits,
        "special_characters": special
    }
