def count_numbers_with_bits_set(numbers, o, n):
    count = 0
    for n in numbers:
        if (n & (1 << o)) and (n & (1 << n)):
            count += 1
    return count

numbers = [3, 5, 7, 9, 15]
o = 0
n = 1
result = count_numbers_with_bits_set(numbers, o, n)
print(result)