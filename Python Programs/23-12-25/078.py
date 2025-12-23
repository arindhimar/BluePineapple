def count_int_with_odd_bits(n):
    count=0
    for i in range(1,n+1):
        if bin(i).count('1')%2==1:
            count+=1
    return count


print(count_int_with_odd_bits(1))
print(count_int_with_odd_bits(5))
