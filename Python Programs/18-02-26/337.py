import re

def match_word_at_end(text, word):
    pattern = rf"\b{re.escape(word)}[.,!?;:]*$"
    return bool(re.search(pattern, text))

print(match_word_at_end("Hello world!", "world"))   
print(match_word_at_end("It is a test.", "test"))   
print(match_word_at_end("Finish line", "line"))     
print(match_word_at_end("Check this out", "this"))  
