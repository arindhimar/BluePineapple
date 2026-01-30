def are_elements_unique(input_list):
    return len(input_list) == len(set(input_list))

print(are_elements_unique([1, 2, 3, 4, 5]))  