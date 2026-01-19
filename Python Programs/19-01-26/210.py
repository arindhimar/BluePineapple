import re

def check_string(string):
    pattern = "^[a-zA-Z0-9]+$"
    if re.search(pattern, string):
        return True
    else:
        return False

string = input("Enter a string: ")
print(check_string(string))