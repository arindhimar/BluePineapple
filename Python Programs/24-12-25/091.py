def is_substring_in_list(substring, str_list):
    for string in str_list:
        if substring in string:
            return True
    return False


strings=["apple","banana","cherry","date"]
substr="ban"
res=is_substring_in_list(substr, strings)
print(res)