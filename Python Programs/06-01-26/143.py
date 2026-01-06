def find_no_of_list_in_tuple(tup):
    return sum(1 for item in tup if isinstance(item, list))


tempTuple = (1, [2, 3], 'hello', [4, 5], 6.7, [8, 9])
print(find_no_of_list_in_tuple(tempTuple))