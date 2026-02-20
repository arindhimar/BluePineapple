def sum_of_three_lowest_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    positive_numbers.sort()
    return sum(positive_numbers[:3])

print(sum_of_three_lowest_positive_numbers([5, 2, 9, 1, 3, -4, 0]))