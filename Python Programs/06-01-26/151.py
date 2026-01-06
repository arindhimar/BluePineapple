def gcd(a, b):
    while b:
        a,b=b,a%b
    return a


def check_if_number_is_co_prime(n,m):
    return gcd(n,m) == 1


n=int(input("Enter first number: "))
m=int(input("Enter second number: "))

print(check_if_number_is_co_prime(n,m))