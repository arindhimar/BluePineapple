import math

def findEulerian(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    
    else:
        sum=2
        
        for i in range(2,n+1):
            sum+=(1/math.factorial(i))
    
    return sum
        
    


n=int(input("Enter n more or equal to 1     "))

print(findEulerian(n))