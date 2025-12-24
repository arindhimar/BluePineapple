def find_divisor_count(N):
    count=0
    n=abs(N)
    for i in range(1,n+1):
        if n%i==0:
            count+=1

    return count