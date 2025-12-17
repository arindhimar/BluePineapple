def differ_by_one_bit(num1, num2):
    xor = num1^num2
    # print(bin(xor)[2:])
    return bin(xor).count("1") == 1

print(differ_by_one_bit(1, 2))