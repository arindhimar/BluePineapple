import re

def findMoreThen4(input_string):
    pt=r"\b\w{4,}\b"
    return re.findall(pt, input_string)

input_string = "The quick brown fox jumps over the lazy dog, which has a long tail."
res=findMoreThen4(input_string)

print(res)