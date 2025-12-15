li=[10,25,37,42,58,63]
for i in range(len(li)):
    num=li[i]
    if num<2:
        print(f"{num} is not a prime number")
        continue
    for j in range(2,num):
        if num%j==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
