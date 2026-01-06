def split_in_two_max(tempNum):
    tempStr=str(tempNum)
    
    tempListOfDigits=[int(digit) for digit in tempStr]
    
    tempSum=0
    
    for i in range(len(tempListOfDigits)):
        for j in range(i+1,len(tempListOfDigits)):
            sumOfPair=tempListOfDigits[i]+tempListOfDigits[j]
            if sumOfPair>tempSum:

                tempSum=sumOfPair
    # print(tempListOfDigits[i],tempListOfDigits[j])
    return tempSum


number=int(input("Enter a positive integer: "))
print(split_in_two_max(number))
        