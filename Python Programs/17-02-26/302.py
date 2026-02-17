def most_significant_set_bit(n):
    if n == 0:
        return 0
    msb = 1
    while n > 1:
        n = n >> 1
        msb = msb << 1
    return msb



print(most_significant_set_bit(18))  