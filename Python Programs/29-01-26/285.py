import re

def match_a_followed_by_b(input_string):
    pattern = r'b{2,3}'
    return bool(re.search(pattern, input_string))

print(match_a_followed_by_b("abbb"))  # True
