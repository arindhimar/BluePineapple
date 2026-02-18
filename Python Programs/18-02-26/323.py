def rearrange_alternate(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    result = []
    i = j = 0

    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1

    while i < len(pos):
        result.append(pos[i])
        i += 1

    while j < len(neg):
        result.append(neg[j])
        j += 1

    return result


print(rearrange_alternate([1, 2, 3, -4, -1, 4]))
    