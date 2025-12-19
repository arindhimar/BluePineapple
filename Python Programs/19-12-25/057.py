def find_largest_number(n):
    digit=[i for i in str(n)]
    newSortedDigit=sorted(digit,reverse=True)
    # print(newSortedDigit)
    maxNm=''.join(newSortedDigit)
    return maxNm


print(find_largest_number(10101010))

