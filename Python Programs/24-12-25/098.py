def multiply_then_divide(tempList):
    l=len(tempList)
    
    mul=1
    for i in tempList:
        mul*=i
        
    return (mul/l)