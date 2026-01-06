def check_if_number_is_in_infinite_sequence(n):
    term=1
    while term<n:
        term=term*2+1
    return term==n



number=int(input("Enter n:  "))
print(check_if_number_is_in_infinite_sequence(number))