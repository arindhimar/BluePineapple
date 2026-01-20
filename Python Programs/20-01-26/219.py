def extract_max_min_k_elements(input_tuple, k):
    if k <= 0 or k > len(input_tuple):
        return "Invalid value of k"
    
    sorted_tuple = sorted(input_tuple)
    min_k_elements = tuple(sorted_tuple[:k])
    max_k_elements = tuple(sorted_tuple[-k:])
    
    return min_k_elements, max_k_elements


input_tuple = (5, 1, 9, 3, 7, 2, 8, 4, 6)
k = 3
print(extract_max_min_k_elements(input_tuple, k))