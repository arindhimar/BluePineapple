def elementOccuringOnlyOnce(tempSortedList):
    if len(tempSortedList) == 0:
        return "List is empty!"
    elif len(tempSortedList) == 1:
        return "None of the element are repeated!"
    tempRepeatingElements = set()
    for i in range(1,len(tempSortedList)):
        if tempSortedList[i-1] == tempSortedList[i]:
            # print(tempSortedList[i])
            tempRepeatingElements.add(tempSortedList[i])
    return tempRepeatingElements


print(elementOccuringOnlyOnce([1,1,2,2,3,3,4,4,5,5,6]))