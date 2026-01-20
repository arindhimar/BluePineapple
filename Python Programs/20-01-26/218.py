def min_operations_to_equal(a, b):
    operations = 0
    while a != b:
        if a > b:
            a -= 1
        else:
            b -= 1
        operations += 1
    return operations

input_a = int(input("Enter first integer: " ))
input_b = int(input("Enter second integer: "))
print(min_operations_to_equal(input_a, input_b))