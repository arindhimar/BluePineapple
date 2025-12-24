def longest_word_length(words):
    return max(len(word) for word in words)


words=["apple","banana","cherry","date"]
print(longest_word_length(words))
