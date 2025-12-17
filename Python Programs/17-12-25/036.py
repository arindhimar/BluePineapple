def nth_digit(a, b, n):
    rem=a%b
    for _ in range(n):
        if rem==0:
            return 0
        rem*=10
        digit=rem //b
        rem%=b
    return digit


print(nth_digit(1, 2, 1))