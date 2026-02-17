def find_element_after_rotations(arr, rotations, index):
    n = len(arr)
    rotations = rotations % n
    new_index = (index - rotations) % n  
    return arr[new_index]

print(find_element_after_rotations([1, 2, 3, 4, 5], 2, 0))