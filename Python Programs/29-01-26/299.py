def max_aggregate(tuples_list):
    if not tuples_list:
        return 0
    return max(sum(tup) for tup in tuples_list)


print(max_aggregate([(1, 2), (3, 4), (5, 6)]))  