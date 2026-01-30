def find_nested_elements(nested_list, elements):
    result = []
    for sublist in nested_list:
        for item in sublist:
            if item in elements:
                result.append(item)
    return result

print(find_nested_elements([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [2, 5, 8]))