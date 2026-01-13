#Write a function to search some literals strings in a string.

def search_literals(string, literals):
    for literal in literals:
        if literal in string:
            return True
    return False


string = input("enter the string: ")
literals = input("enter the literals: ").split()
print(search_literals(string, literals))