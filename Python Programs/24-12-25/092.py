def is_undulating(n):
    s=str(n)
    if len(s)<3:
        return False
    return all(s[i]==s[i%2] for i in range(len(s)))


print(is_undulating(1212))
print(is_undulating(1234))
print(is_undulating(777))
