def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def max_occurring_divisor_in_interval(a, b):
    max_divisors = 0
    max_divisor = a
    for i in range(a, b + 1):
        divisors_count = count_divisors(i)
        if divisors_count > max_divisors:
            max_divisors = divisors_count
            max_divisor = i
    return max_divisor


print(max_occurring_divisor_in_interval(1, 10))