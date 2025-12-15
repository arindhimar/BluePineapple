t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

for i in range(len(t1)):
    if t1[i] in t2:
        print(t1[i])
        
# lol = tuple(set(t1) & set(t2))

# print(lol)