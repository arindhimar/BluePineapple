def maximize_tuples(tup1, tup2):
    return tuple(max(a, b) for a, b in zip(tup1, tup2))

print(maximize_tuples((5, 10, 15), (3, 12, 9)))