#Write a function to replace maximum n occurrences of spaces, commas, or dots with a colon.
import re

def replace_max_n_occurrences(text, n):
    if n <= 0:
        return text
    pattern = r'[ ,.]'
    
    
    result = re.sub(pattern, ':', text, count=n)
    
    return result


print(replace_max_n_occurrences("Hello, world. This is a test string.", 3))