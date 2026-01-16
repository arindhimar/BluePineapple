def find_values_greater_then_specified(list_of_numbers ,k):
    temp_list_of_numbers = []
    for i in list_of_numbers:
        if i > k:
            temp_list_of_numbers.append(i)
    
    
    return temp_list_of_numbers