import re


def split_with_delimeters(st, delimiters):
    return re.split(f"[{re.escape(delimiters)}]+", st)


txt="Hello, world! How are you doing today?"
delimiters=",!?"
result=split_with_delimeters(txt,delimiters)
print(result)