#Write a function to decode a run-length encoded given list.

def decode_rle(encoded_list):
    decoded_list = []
    for item in encoded_list:
        value, count = item
        decoded_list.extend([value] * count)
    return decoded_list

encoded_list = [('A', 3), ('B', 2), ('C', 4)]
result = decode_rle(encoded_list)
print(result)