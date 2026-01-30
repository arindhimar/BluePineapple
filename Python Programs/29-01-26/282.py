def subtract_lists(list1, list2):
    return list(map(lambda x, y: x - y, list1, list2))

print(subtract_lists([10, 20, 30], [1, 2, 3]))