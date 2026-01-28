def ascii_value(char):
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    return ord(char)

try:
    print(ascii_value('A'))
except ValueError as e:
    print(e)