def check_elements_in_list(list1):
    return len(set(list1)) == 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(check_elements_in_list(list1))