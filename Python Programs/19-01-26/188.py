def is_product_of_two_squares(n):
    if n < 0:
        return False
    
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n


n=int(input("Enter n"))
print(is_product_of_two_squares(n))