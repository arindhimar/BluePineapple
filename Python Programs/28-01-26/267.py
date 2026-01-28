def sum_of_squares_of_odd_natural_numbers(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    temp_sum = 0
    for i in range(n):
        odd_number = 2 * i + 1
        temp_sum += odd_number ** 2
        
    return temp_sum

print(sum_of_squares_of_odd_natural_numbers(5))