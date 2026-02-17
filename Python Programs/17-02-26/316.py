def find_last_occurence(list_of_numbers,n):
    prev_index=-1
    for i in list_of_numbers:
        if i == n:
            prev_index = i
            
    return i