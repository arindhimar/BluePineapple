def find_majority_element(arr):
    count = 1
    majority_count = len(arr) // 2

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
            if count > majority_count:
                return arr[i]
        else:
            count = 1

    return -1

print(find_majority_element([1,6,4,3,1,1,2,3,4,5,5,4,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))