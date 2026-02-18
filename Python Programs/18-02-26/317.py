def modified_rle(lst):
    if not lst:
        return []
    
    result = []
    count = 1

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            result.append((count, lst[i - 1]))
            count = 1

    result.append((count, lst[-1]))
    
    return result


print(modified_rle([1,1,1,2,3,3]))
