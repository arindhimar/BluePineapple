import re

def find_literals(text, words):
    result = {}

    for word in words:
        result[word] = re.findall(re.escape(word), text)

    return result
