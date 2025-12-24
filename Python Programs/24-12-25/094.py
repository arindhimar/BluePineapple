def find_idx_of_minimum_length(multi_tuples):
    tempList=[]
    for i in multi_tuples:
        min_ele=min(i)
        tempList.append(i.index(min_ele))
    
    return tempList