def split_at_lowercase(st):
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


split_at_lowercase("HElLoWORlD")