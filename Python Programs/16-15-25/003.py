def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        
    return True


list_of_numbers=[0,2,-3,4,5]

for i in list_of_numbers:
    if i==0:
        print("0 is neither")
    elif i <0:
        print("Not prime")
    else:
        if isPrime(i)==False:
            print(str(i )+ "is not Prime")