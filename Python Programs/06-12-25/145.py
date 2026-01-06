def find_max_diff_bw_2_elements(arr):
    if len(arr) < 2:
        return 0
    max_diff =arr[1]-arr[0]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            diff=arr[j]-arr[i]
            if diff>max_diff:
                max_diff=diff
    return max_diff

array=[2,3,10,6,4,8,1]
print(find_max_diff_bw_2_elements(array))