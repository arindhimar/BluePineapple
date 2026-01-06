def split_in_two_max(tempNum):
    tempStr=str(tempNum)
    
    tempListOfDigits=[int(digit) for digit in tempStr]
    
    tempSum=0
    maxSum=0
    if len(tempListOfDigits)<2: return tempNum 
    for i in range(1,len(tempStr)):
        firstPart=int(tempStr[:i])
        secondPart=int(tempStr[i:])
        
        tempSum=firstPart+secondPart
        if tempSum>maxSum:
            maxSum=tempSum
    
    return maxSum
        
        

number=int(input("Enter a positive integer: "))
print(split_in_two_max(number))
        