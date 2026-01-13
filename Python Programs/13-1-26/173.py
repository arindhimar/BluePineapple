#Write a function to remove everything except alphanumeric characters from a string.

def remove_special_characters(string):
    return ''.join(e for e in string if e.isalnum())

s=input("enter the string: ")
print(remove_special_characters(s))