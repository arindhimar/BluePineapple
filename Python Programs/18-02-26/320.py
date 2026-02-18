def difference(n):
    sum_n = n * (n + 1) // 2
    square_of_sum = sum_n ** 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    return square_of_sum - sum_of_squares


print(difference(10))
