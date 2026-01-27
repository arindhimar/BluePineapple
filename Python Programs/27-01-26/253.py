from collections import Counter

def count_integers(int_list):
    counter = Counter(int_list)
    return dict(counter)