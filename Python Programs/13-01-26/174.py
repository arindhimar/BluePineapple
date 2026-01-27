def group_key_value_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

pairs = [(1, 'a'), (2, 'b'), (1, 'c'), (2, 'd'), (3, 'e')]
print(group_key_value_pairs(pairs))