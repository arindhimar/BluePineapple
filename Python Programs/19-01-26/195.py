def find_first_position_of_element_in_sorted_list(list1, element):
    for i in range(len(list1)):
        if list1[i] == element:
            return i
    return -1