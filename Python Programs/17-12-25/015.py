def split_at_lower(st):
    resuslt=[]
    curr=""
    
    for i in st:
        if i.islower():
            resuslt.append(curr)
            curr=""
        else:
            curr+=i
        
    resuslt.append(curr)
    
    print(resuslt)


split_at_lower("HElLoWORlD this is SAMPLE")