import re
def check_decimal(decimal):
    pattern = "^[0-9]+\.[0-9]{2}$"
    if re.search(pattern, decimal):
        return True
    else:
        return False

decimal = input("Enter a decimal: ")
print(check_decimal(decimal))