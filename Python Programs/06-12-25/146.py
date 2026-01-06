def find_ascii_value_sum(s):
    return sum(ord(char) for char in s)

s=input("Enter a string: ")
print(find_ascii_value_sum(s))