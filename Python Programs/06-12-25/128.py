def find_words_longer_than(words, n):
    return [word for word in words if len(word)>n]



print(find_words_longer_than(['apple', 'banana', 'pear', 'kiwi', 'grapefruit'], 4))  