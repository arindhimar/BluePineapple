def find_abs_diff_in_pair_list(pair_list):
    return [abs(a - b) for a, b in pair_list]

pair_list =[(3,5),(10,4), (7, 7), (1, 9)]
print(find_abs_diff_in_pair_list(pair_list))