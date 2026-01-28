def sum_of_even_numbers_at_even_positions(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    temp_sum = 0
    for i in range(n):
        even_number = 2 * i
        temp_sum += even_number
        
    return temp_sum

try:
    print(sum_of_even_numbers_at_even_positions(5))
except ValueError as e:
    print(e)