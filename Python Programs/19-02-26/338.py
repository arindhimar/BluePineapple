def count_number_of_substring_with_same_first_and_last_char(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                count += 1
    return count

print(count_number_of_substring_with_same_first_and_last_char("abcab"))