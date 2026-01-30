def count_inversions(arr):
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

print(count_inversions([2, 3, 8, 6, 1]))