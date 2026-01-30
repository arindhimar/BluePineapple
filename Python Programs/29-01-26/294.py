def max_in_heterogeneous_list(lst):
    max_value = None
    for item in lst:
        if isinstance(item, (int, float)):
            if max_value is None or item > max_value:
                max_value = item
    return max_value

print(max_in_heterogeneous_list([1, 'a', 3.5, None, 2, 'hello', 4]))  