def find_xy(a, b, n):
    for x in range(n // a + 1):
        for y in range(n // b + 1):
            if a * x + b * y == n:
                return (x, y)
    return None

a=int(input("Enter value for a: "))
b=int(input("Enter value for b: "))

n=int(input("Enter value for n: "))

print(find_xy(a, b, n))