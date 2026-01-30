def max_length_lists(list_of_lists):
    if not list_of_lists:
        return []
    
    max_length = max(len(lst) for lst in list_of_lists)
    return [lst for lst in list_of_lists if len(lst) == max_length]

print(max_length_lists([[1, 2, 3], [4, 5], [6, 7, 8], [9]]))