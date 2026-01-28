def last_removed_position(arr, n):
    if n <= 0 or n > len(arr):
        raise ValueError("n must be between 1 and the length of the array")
    
    index = 0
    while len(arr) > 1:
        index = (index + n - 1) % len(arr)
        arr.pop(index)
    
    return arr[0]

print(last_removed_position([1, 2, 3, 4, 5], 2))