def hasduplicates(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

print(hasduplicates([1, 2, 3, 4]))