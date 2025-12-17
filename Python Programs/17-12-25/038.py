def divide_first_even_odd(numbers):
    fe=None
    fo=None
    for n in numbers:
        if n%2==0 and fe is None:
            fe=n
        elif n%2!=0 and fo is None:
            fo=n
        if fe is not None and fo is not None:
            break
    if fe is None or fo is None:
        return None
    return fe/fo


print(divide_first_even_odd([9,8,6,5,3,4,5,7,7,8,3,2]))