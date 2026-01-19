def remove_tuples_with_length_k(list1, k):
    return [tup for tup in list1 if len(tup) != k]


list1 = [(1, 2), (3, 4), (5, 6), (7, 8, 9)]
k = 2
print(remove_tuples_with_length_k(list1, k))