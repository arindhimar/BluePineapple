def longest_common_subsequence(s):
    max_len = 0
    
    for i in range(len(s)):
        revStr = s[i:][::-1]
        if s[i:] == revStr:
            curr_len = len(s) - i
            if curr_len > max_len:
                max_len = curr_len
    return max_len

        
        


print(longest_common_subsequence("arin"))