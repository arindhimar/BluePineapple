def are_all_elements_equal(input_list, string):
    return all(element == string for element in input_list)

print(are_all_elements_equal(['test', 'test', 'test'], 'test'))