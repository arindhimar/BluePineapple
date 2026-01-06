def ratio_of_zeroes(arr):
    zero_count=arr.count(0)
    total_count=len(arr)
    if total_count== 0:
        return 0
    return zero_count / total_count


