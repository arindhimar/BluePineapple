def findOddTimesOccuringNumber(list):
    tempList=[]
    for i in list:
        if list.count(i)%2!=0:
            if i not in tempList:
                tempList.append(i)
    return tempList

list_of_numbers=[1,2,3,4,5,2,6,8,7,5,7,3,4,8,6,8,8,8]
print(findOddTimesOccuringNumber(list_of_numbers))
    