def hexagonal_number(n):
    return n * (2 * n - 1)

n = int(input("Enter a positive integer n: "))
print(hexagonal_number(n))