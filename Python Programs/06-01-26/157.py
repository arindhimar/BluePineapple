s = input("enter string")
count = 0
tempChar = None
output = ""



for ch in s:
    if ch == tempChar:
        count += 1
    else:
        if tempChar is not None:
            output += str(count) + tempChar
        tempChar = ch
        count = 1

output += str(count) + tempChar

print(output)
