def babylonian_sqrt(n, tolerance=1e-10):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if n == 0:
        return 0
    guess = n / 2.0
    while True:
        next_guess = (guess + n / guess) / 2
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess
        
print(babylonian_sqrt(25))