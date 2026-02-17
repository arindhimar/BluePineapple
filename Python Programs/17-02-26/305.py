def match_p_words(words):
    p_words = [word for word in words if word.lower().startswith('p')]

    if len(p_words) < 2:
        return None
    
    return p_words[0], p_words[1]


words = ["pear", "apple", "peach", "plum", "banana"]
result = match_p_words(words)

print(result)
