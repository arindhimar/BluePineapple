def toggle_even_bits_of_binary(n):
    for i in range(n):
        if i % 2 == 0:
            n[i]= 1 - n[i]
    return n

tempBin = input("Enter binary number: ")
binList = [int(bit) for bit in tempBin]
result = toggle_even_bits_of_binary(binList)
print("".join(map(str, result)))