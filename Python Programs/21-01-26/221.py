def find_first_even_numbers(list_of_numbers):
    for i in list_of_numbers:
        if i % 2 == 0 :
            return i
        
    return -1
