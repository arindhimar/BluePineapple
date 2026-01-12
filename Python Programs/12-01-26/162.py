def sum_positive_integers(n):
    total = 0
    for i in range(n, 0, -2):
        total += i
    return total

n = 6
print(sum_positive_integers(n))