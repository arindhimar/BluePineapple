def remove_chars(s1, s2):
    result = ""
    for c in s1:
        if c not in s2:
            result += c
    return result

print(remove_chars("hello world", "ole"))
