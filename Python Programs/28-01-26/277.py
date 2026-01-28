def filter_dict_by_value(input_dict, threshold):
    filtered_dict = {k: v for k, v in input_dict.items() if v > threshold}
    return filtered_dict

print(filter_dict_by_value({'a': 10, 'b': 5, 'c': 15}, 7))