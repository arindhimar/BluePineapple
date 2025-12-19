def find_max_diff_in_tuples(tempList):
    sortedList=sorted(tempList)
    # print(sortedList)
    
    return sortedList[-1]-sortedList[0]
        


list_of_numbers=(9,8,6,5,3,4,5,7,7,8,3,2)

print(find_max_diff_in_tuples(list_of_numbers))
