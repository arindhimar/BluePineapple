def findMatch(tuple1,tuple2):
    res=[]
    for i in tuple1:
        if i in tuple2:
            res.append(i)
    
    return res

print(findMatch((1,2,3),(3,4,5)))
    
    