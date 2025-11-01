import re

text="This is a simple demonstration of Regex Function in Py"
rgx=r"\b\w{4,}\b"
res=re.findall(rgx,text,re.IGNORECASE)
print(res)
