def nth_decagonal_number(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    decagonal_number = 4 * n * (n - 1) + 1
    return decagonal_number


try:
    print(nth_decagonal_number(5))
except ValueError as e:
    print(e)