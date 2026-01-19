def octal_to_decimal(octal_num):
    return int(octal_num, 8)


octal_num = input("Enter an octal number: ")
print(octal_to_decimal(octal_num))