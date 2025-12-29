def find_missing_values(tempList,startRange,endRange):
    tempMissingNumbers=[]
    for i in range(startRange,endRange+1):
        if tempList.count(i)==0:
            tempMissingNumbers.append(i)
    return tempMissingNumbers


print(find_missing_values([1,3,4,5,7],1,9))