def next_smallest_palindrome(n):
    n += 1
    while True:
        if str(n) == str(n)[::-1]:
            return n
        n += 1
