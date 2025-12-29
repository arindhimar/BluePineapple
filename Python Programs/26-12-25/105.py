def countTrue(tempList):
    return len(list(filter(lambda x:x==True,tempList)))



print(countTrue([False,True,True,True]))