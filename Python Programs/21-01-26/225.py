def find_min_element_in_sorted_rotated_array(input_arr):
    if not input_arr:
        return -1
    for i in range(1, len(input_arr)):
        if input_arr[i] < input_arr[i - 1]:
            return input_arr[i]
    return input_arr[0]