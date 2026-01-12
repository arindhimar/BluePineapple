def sum_of_list(temp_list,temp_range):
    tempSum=0
    for i in range(temp_range[0],temp_range[1]+1):
        tempSum+=temp_list[i]
    return tempSum


print(sum_of_list([1,2,3,4,5,6,7,8,9,10],[2,5]))


