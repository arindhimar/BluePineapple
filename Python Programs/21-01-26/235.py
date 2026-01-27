def set_even_bits(n):
    for i in range(len(str(n))):
        if i % 2 == 0:
            n |= (1 << i)
    return n