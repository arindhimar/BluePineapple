def sum_of_common_divisors(a,b):
    common_divisors=[]
    
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            common_divisors.append(i)
    return sum(common_divisors)


a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

result=sum_of_common_divisors(a,b)

print(result)