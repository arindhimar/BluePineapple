def count_occurrences(string):
    count = 0
    for i in string:
        if i == 's' or i == 't' or i == 'd':
            count += 1
    return count

s=input("enter the string: ")
print(count_occurrences(s))
