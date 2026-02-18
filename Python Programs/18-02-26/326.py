def most_occuring_word(str):
    words_split = str.split(' ')
    count = {}

    for word in words_split:
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1

    most_occuring = max(count, key=count.get)

    return most_occuring

print(most_occuring_word("hello world hello"))
