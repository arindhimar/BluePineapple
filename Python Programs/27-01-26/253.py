def count_total_integer_in_lists(input_list):
    total_count = 0
    for item in input_list:
        if isinstance(item, list):
            total_count += count_total_integer_in_lists(item)
        if isinstance(item, int):
            total_count += 1
    return total_count

