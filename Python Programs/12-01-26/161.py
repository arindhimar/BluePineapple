def remove_elements(source_list, elements_to_remove):
    return [item for item in source_list if item not in elements_to_remove]


source_list = [1, 2, 3, 4, 5, 6]
elements_to_remove = [2, 4, 6]
result = remove_elements(source_list, elements_to_remove)

print(result)  