def remove_special_characters(string):
    return ''.join(e for e in string if e.isalnum())

s=input("enter the string: ")
print(remove_special_characters(s))