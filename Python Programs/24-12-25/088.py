from collections import Counter

def element_frequency(lst):
    # print(Counter(lst))
    return dict(Counter(lst))

data=[1, 2, 2, 3, 3, 3, 4]
print(element_frequency(data))
