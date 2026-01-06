from collections import Counter

def find_item_with_max_freq(items):
    counter = Counter(items)
    max_freq = max(counter.values())
    return [item for item, freq in counter.items() if freq == max_freq]


print(find_item_with_max_freq(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))  