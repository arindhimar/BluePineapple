import re

def check_atleast_one_number_and_one_alpha(string):
    pattern = "[a-zA-Z]+[0-9]+|[0-9]+[a-zA-Z]+"
    if re.search(pattern, string):
        return True
    else:
        return False


string = input("Enter a string: ")
print(check_atleast_one_number_and_one_alpha(string))