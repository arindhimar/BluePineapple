def find_sub_sequence_with_max_len(tempList,k):
    n=len(tempList)
    maxLen=0
    for i in range(n):
        tempLen=1
        for j in range(i+1,n):
            if (tempList[j]-tempList[j-1])==k:
                tempLen+=1
            else:
                break
        maxLen=max(tempLen,maxLen)

    return maxLen    


list_of_numbers=[9,8,6,5,3,4,5,7,7,8,3,2]
print(find_sub_sequence_with_max_len(list_of_numbers,1))