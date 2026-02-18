import re

def find_five_letter_words(text):
    pattern = r'\b\w{5}\b'
    return re.findall(pattern, text)

sample_text = "Hello there, these words exist: apple, mango, and berry."
print(find_five_letter_words(sample_text))
