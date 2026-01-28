def divide_tuples(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length")
    
    result = []
    for a, b in zip(tuple1, tuple2):
        if b == 0:
            result.append(float('inf'))
        else:
            result.append(a / b)
    
    return tuple(result)

print(divide_tuples((10, 20, 30), (2, 4, 5)))  