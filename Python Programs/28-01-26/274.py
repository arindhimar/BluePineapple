def sum_of_even_index_binomial_coefficients(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    from math import comb
    
    temp_sum = 0
    for k in range(0, n + 1, 2):
        temp_sum += comb(n, k)
        
    return temp_sum

try:
    print(sum_of_even_index_binomial_coefficients(5))
except ValueError as e:
    print(e)