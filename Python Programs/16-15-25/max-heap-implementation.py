def insert_number(i):
    h.append(i)
    
    idx=len(h)-1
    
    while idx> 0 and h[(idx-1) //2] < h[idx]:
        h[idx],h[(idx-1)//2]=h[(idx-1)//2],h[idx]
        idx=(idx-1)//2


list_of_numbers=[1,2,3,4,5]
h=[]

for i in list_of_numbers:
    insert_number(i)
    

print(h)