def perimeter_of_pentagon(n):
    if n < 0:
        return None
    
    return 5 * n


n=int(input("enter the length of the pentagon: "))
print(perimeter_of_pentagon(n))