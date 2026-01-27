def insert_before_each(lst, element):
    result = []
    for item in lst:
        result.append(element)
        result.append(item)
    return result