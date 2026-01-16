def find_difference_k(list_of_numbers, k):
    pairs = []
    for i in range(len(list_of_numbers)):
        for j in range(i + 1, len(list_of_numbers)):
            if abs(list_of_numbers[i] - list_of_numbers[j]) == k:
                pairs.append((list_of_numbers[i], list_of_numbers[j]))

    return pairs


nums = [1, 5, 3, 4, 2]
k = 2
print(find_difference_k(nums , k))