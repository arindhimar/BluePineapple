def sequential_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

print(sequential_search([4, 2, 5, 1, 3], 1))  