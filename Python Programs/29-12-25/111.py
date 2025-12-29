def find_common_in_nested(tempList):
    max_len=len(tempList[0])
    max_idx=0
    commonWords=[]
    for i in range(1,len(tempList)):
        if len(tempList[i])>max_len:
            max_idx=i
    
    
    for i in range(len(tempList[max_idx])):
        temp=tempList[max_idx][i]
        
        for j in range(len(tempList)):
            if j!=max_idx and temp in tempList[j]:
                commonWords.append(temp)

    
    return commonWords



# print(find_common_in_nested([]))


print(find_common_in_nested([[1,2,3],[2,3,4],[3,2]]))