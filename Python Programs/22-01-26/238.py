#Write a python function to count number of non-empty substrings of a given string.

def count_non_empty_substrings(s):
    n = len(s)
    return n * (n + 1) // 2

print(count_non_empty_substrings("abc",))