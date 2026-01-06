def can_be_expressed_as_sum_of_powers_of_2(n):
    while n > 0:
        if n%2==0:
            n-=2
        else:
            n-=1
    return n==0


n=int(input("Enter a positive integer n: "))
print(can_be_expressed_as_sum_of_powers_of_2(n))