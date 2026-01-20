def first_repeated_character(input_string):
    seen = set()
    for char in input_string:
        if char in seen:
            return char
        seen.add(char)
    return None


input_string = input("Enter a string: ")
print(first_repeated_character(input_string))