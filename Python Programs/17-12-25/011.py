s="arin is working in blupineapple"

c='i'

pos=[i for i in range(len(s)) if s[i]==c]
if positions:
    last=pos[-1]
    s=s[:last]+s[last+1:]
    
    first=pos[0]
    s=s[:first]+s[first+1:]
    
print(s)
