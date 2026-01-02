def findTripletWithSum(tempListOfNumbers,requriedSum):
    for i in range(len(tempListOfNumbers)):
        for j in range(i+1,len(tempListOfNumbers)):
            for k in range(j+1,len(tempListOfNumbers)):
                if tempListOfNumbers[i] + tempListOfNumbers[j] + tempListOfNumbers[k] == requriedSum:
                    return (i,j,k)
                
    
    return ()


print(findTripletWithSum([1,2,3,4,5,6,7,8],10))