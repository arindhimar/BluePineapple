def domino(n):
    n=abs(n)
    if n%2!=0:
        return 0
    
    a0=1
    a2=3
    
    if n==0:
        return a0
    elif n==2:
        return 3
    
    for i in range(4,n+1,2):
        temp=4*a2-a0
        a0,a2=a2,temp    
    return a2


n=int(input("Enter n"))
print(domino(n))