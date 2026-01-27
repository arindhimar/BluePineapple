def next_perfect_square(n):
    if n < 0:
        return 0
    root = int(n**0.5) + 1
    return root * root

print(next_perfect_square(25))