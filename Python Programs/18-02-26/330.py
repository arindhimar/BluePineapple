import re


def find_words_by_length(text):
    pattern = re.compile(r"\b\w{3,5}\b")
    matches = pattern.findall(text)
    return matches

input_string = "The quick brown fox jumps over the lazy dog. The speed is 120 mph."
result = find_words_by_length(input_string)
print(result)
