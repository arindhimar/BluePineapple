def nth_star_number(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    star_number = 6 * n * (n - 1) + 1
    return star_number

print(nth_star_number(4))