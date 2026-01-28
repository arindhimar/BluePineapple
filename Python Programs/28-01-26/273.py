def subtract_tuples(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length")
    
    result = []
    for a, b in zip(tuple1, tuple2):
        result.append(a - b)
    
    return tuple(result)


try:
    print(subtract_tuples((10, 20, 30), (1, 2, 3)))
except ValueError as e:
    print(e)