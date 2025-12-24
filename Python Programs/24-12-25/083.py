def find_char_from_string(s):
    total_ascii_value=sum(ord(char) for char in s)
    result_char=chr(total_ascii_value)
    return result_char

input_string="abc"
res=find_char_from_string(input_string)
print(res)
