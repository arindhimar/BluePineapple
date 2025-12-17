tempList=["abv","123","12a"]

res=[]
for i in tempList:
    flag=True
    for j in i:
        if j.isnumeric():
            flag=False
            break
    if flag:
        res.append(i)
        

print(res)