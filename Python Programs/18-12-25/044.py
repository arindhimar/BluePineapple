def match_word_at_start(text):
    if not text:
        return None

    word=""
    for ch in text:
        if ('a'<=ch<='z') or ('A'<=ch<='Z') or ('0'<=ch<='9') or ch =='_':
            word+=ch
        else:
            break

    return word if word else None


print(match_word_at_start("Hello world"))