def check_if_all_are_diff(tempList):
    for i in tempList:
        if tempList.count(i)>1:
            return False
        
    return True 
        



# list_of_numbers=[9,8,6,5,3,4,5,7,7,8,3,2]
list_of_numbers=[1,2,3,4,5]


print("Yes they are" if check_if_all_are_diff(list_of_numbers) else "No they are not")