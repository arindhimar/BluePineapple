def convertToIntergers(TupleOfInts):
    tempList=[]
    for i in range(0,len(TupleOfInts)):
        if i % 2 == 0:
            tempList.append(-1 * TupleOfInts[i])
        else:
            tempList.append(TupleOfInts[i])
    
    return tuple(tempList)
    
    

print(convertToIntergers((1,2,3,4,5)))