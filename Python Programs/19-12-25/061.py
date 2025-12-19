def count_substr_equal_to_len(tempList):
    n=len(tempList)
    count =0

    for i in range(n):
        current_sum=0
        for j in range(i, n):
            current_sum+=tempList[j]
            if current_sum==(j - i + 1):
                count+=1

    return count


list_of_numbers=[9,8,6,5,3,4,5,7,7,8,3,2]

print(count_substr_equal_to_len(list_of_numbers))