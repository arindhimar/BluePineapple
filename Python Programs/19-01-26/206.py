def perform_adjacent_element_concatenation(tuple1):
    return tuple(tuple1[i] + tuple1[i + 1] for i in range(len(tuple1) - 1))


tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(perform_adjacent_element_concatenation(tuple1))
