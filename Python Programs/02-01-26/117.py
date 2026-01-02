def convertElementsToFloat(tempInt):
    return float(tempInt)

def convertItemsToFloat(tempListOfInt):
    tempListOfFloat = []
    for i in tempListOfInt:
        tempListOfFloat.append(convertElementsToFloat(i))
    
    return tempListOfFloat


print(convertItemsToFloat([1,2,3,4,5,6,7]))