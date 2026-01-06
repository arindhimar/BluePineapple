def find_same_pair_in_3_lists(list1, list2, list3):
    return [(a, b) for a in list1 for b in list2 if a == b and a in list3]


