def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))