def count_same_position_chars(s):
    count = 0
    for i in range(len(s)):
        if s[i].lower() == chr(ord('a') + i % 26):
            count += 1
    return count

s = "AbcDefGhijKlmnoPqrstUvwxYz"
print(count_same_position_chars(s))
