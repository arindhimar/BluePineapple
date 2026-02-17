def get_max_in_cols(tempList):
    temp_max=[]
    # print(len(tempList[0]))
    for i in range(len(tempList[0])):
        temp_max.append(max(tempList[0][i],tempList[1][i]))
        
    return temp_max

def max_sum_brute_force(arr):
    n = len(arr)
    max_sum = 0
    
    for i in range(n):
        curr_sum = arr[i]
        j = i + 2
        while j < n:
            curr_sum += arr[j]
            j += 2
        if curr_sum > max_sum:
            max_sum = curr_sum
    
    return max_sum

temp = get_max_in_cols([
    [1,2,3,1],
    [2,3,4,5],
])

print(max_sum_brute_force(temp))