def find_first_duplicates(tempNumList):
    sortedList=sorted(tempNumList)
    for i in range(len(sortedList)-1):
        if sortedList[i]==sortedList[i+1]:
            print (sortedList[i])
            return
        
list_of_numbers=[1,2,3,4,5,5,6,6,7,4,3,21,3,3]

find_first_duplicates(list_of_numbers)