def add_list_to_tuple(tempList,tempTuple):
    tempNewList=list(tempTuple)
    
    for i in tempList:
        tempNewList.extend(i)
        
    return tempNewList



print(add_list_to_tuple([[4,5,6],[7,8,9]],(1,2,3)))