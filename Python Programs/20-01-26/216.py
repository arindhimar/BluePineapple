def is_subset(nested_list1, nested_list2):
    for sublist in nested_list1:
        if sublist not in nested_list2:
            return False
    return True

list1 = [[1, 2], [3, 4]]
list2 = [[1, 2], [3, 4], [5, 6]]
result = is_subset(list1, list2)
print(result)  