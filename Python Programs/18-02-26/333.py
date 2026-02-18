def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])


lst = [[1, 3], [4, 2], [6, 5], [2, 8]]

print(sort_by_second_element(lst))