def binary_to_decimal(str):
    l=len(str)
    i=l-1
    tempSum=0
    while i>=0:
        tempSum+=2**(i) * int(str[i])
        i-=1    
    
    print(tempSum)


binary_to_decimal("1111")


