def muliply_without_operator(a, b):
    result=0
    for _ in range(abs(b)):
        result+=a
    if b < 0:
        result = -result
    return result


x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

print(muliply_without_operator(x, y))