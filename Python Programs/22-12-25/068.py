def isotonic_increasing_decreasing(tempList):
    l=len(tempList)
    i=1
    ck=None  
    while i<l:
        if ck is None:
            if tempList[i-1] <= tempList[i]:
                ck=True
            else:
                ck=False
        
        else:
            if ck: 
                if tempList[i-1]>tempList[i]:
                    print("Not")
                    return
            else:  
                if tempList[i-1] <tempList[i]:
                    print("Not")
                    return
        i+=1
    
    print("Yes")


list_of_numbers = [47, 3, 88, 15, 62, 29, 94, 8, 56, 71]
isotonic_increasing_decreasing(list_of_numbers)
