def count_negative_numbers(list_of_numbers):
    return len(list(filter(lambda x : x < 0, list_of_numbers)))


numbers = [1, -2, 3, -4, 5, -6]
print(count_negative_numbers(numbers))