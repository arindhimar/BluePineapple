def check_tuple_data_types(input_tuple):
    if not input_tuple:
        return True
    first_type = type(input_tuple[0])
    for element in input_tuple:
        if type(element) != first_type:
            return False
    return True