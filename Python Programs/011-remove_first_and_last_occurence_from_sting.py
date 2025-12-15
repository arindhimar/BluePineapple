s="thisisasamplestring"
ch='i'
positions=[i for i in range(len(s)) if s[i]==ch]
if positions:
    last=positions[-1]
    s=s[:last]+s[last+1:]
    first=positions[0]
    s=s[:first]+s[first+1:]
print(s)
