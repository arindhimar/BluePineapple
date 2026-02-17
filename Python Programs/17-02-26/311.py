def set_left_most_bit(str):
    tempBits=list(str)
    for i in range(len(tempBits)):
        if tempBits[i] == '0':
            tempBits[i]='1'
            break
    
    return ''.join(tempBits)


print(set_left_most_bit('1010101'))