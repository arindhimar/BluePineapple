def count_even_xor_pairs(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] ^ arr[j]) % 2 == 0:
                count += 1
    return count

arr = [1, 2, 3, 4, 5]
print(count_even_xor_pairs(arr))