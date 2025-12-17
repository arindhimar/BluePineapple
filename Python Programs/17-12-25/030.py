def substrings_same_start_end(word):
    substrs=[]
    n=len(word)
    
    for i in range(n):
        for j in range(i+1, n+1):
            substr=word[i:j]
            if substr[0]==substr[-1]:
                substrs.append(substr)
    
    return substrs

word="aba"
print(substrings_same_start_end(word))
