def findmultiples(n,m):
    return[n*i for i in range(1,m+1)]

n=int(input("enter n"))
m=int(input("enter m"))

print(findmultiples(n,m))
