def find_index_of_all_max_element(list1):
    max_element = max(list1)
    return [index for index, element in enumerate(list1) if element == max_element]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_index_of_all_max_element(list1))