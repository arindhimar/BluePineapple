def find_max_even_length(list_of_words):
    return max([len(w) for w in list_of_words if len(w)%2==0])

words = ["apple", "banana", "pear", "kiwi"]

print(find_max_even_length(words))