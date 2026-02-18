def min_indices(lst):
    min_value = min(lst)
    indices = []
    i = 0
    while i < len(lst):
        if lst[i] == min_value:
            indices.append(i)
        i += 1
    return indices


print(min_indices([4, 2, 7, 2, 9, 2]))
