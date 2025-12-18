def find_sum_of_repeated_elements(tempList):
    tempSum=0
    for i in tempList:
        if tempList.count(i)>1:
            tempSum+=i
    
    return tempSum
    
list_of_numbers=[9,8,6,5,3,4,5,7,7,8,3,2]

print(find_sum_of_repeated_elements(list_of_numbers))