def extract_rear_elements(tuple_list):
    return [t[-1] for t in tuple_list]

print(extract_rear_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))