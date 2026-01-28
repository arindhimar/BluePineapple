def sum_of_fifth_power_of_even_natural_numbers(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    temp_sum = 0
    for i in range(n):
        even_number = 2 * (i + 1)
        temp_sum += even_number ** 5
        
    return temp_sum

try:
    print(sum_of_fifth_power_of_even_natural_numbers(3))
except ValueError as e:
    print(e)