def count_positive_num_in_list(tempList):
    return len(list(filter(lambda x: x>0,tempList)))


list_of_numbers = [47, -3, 88, -15, 62, -29, 94, -8, 56, -71]

print(count_positive_num_in_list(list_of_numbers))