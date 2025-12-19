def find_smallest_number_in_list(tempList):
    min_ele=None
    
    for i in tempList:
        if min_ele==None:
            min_ele=i
        elif i<min_ele:
            min_ele=i
        
    return min_ele


list_of_numbers=[9,8,6,5,3,4,5,7,7,8,3,2]
print(find_smallest_number_in_list(list_of_numbers))