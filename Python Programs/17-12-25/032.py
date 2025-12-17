def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        
    return True

def largestPrimeFactor(n):
    largest=None
    for i in range(2,n+1):
        if n%i==0 and isPrime(i):
            largest=i
    return largest


n=int(input("Enter n"))
print(largestPrimeFactor(n))

