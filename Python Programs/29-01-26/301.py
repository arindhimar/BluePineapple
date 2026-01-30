def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    else:
        return 1 + max(dict_depth(v) for v in d.values())
    
print(dict_depth({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}))