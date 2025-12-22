def countSort(tempList):
    l=len(tempList)
    max_num=max(tempList)
    tempCountList=[0]*(max_num + 1)
    # print(tempCountList)
    for i in tempList:
        tempCountList[i]+=1
        # print(tempCountList[i])
        # print(i)
        
    
    print(tempCountList)
    tempSortedList=[]
    for i in range(len(tempCountList)):
        count=0
        while count<tempCountList[i]:
            tempSortedList.append(i)
            count+=1
            
    print(tempSortedList)
    


list_of_numbers=[9,8,6,5,3,4,5,7,7,8,3,2]
countSort(list_of_numbers)