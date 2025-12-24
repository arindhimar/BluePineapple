def power(a, b):
    res=1
    exp=abs(b)
    for _ in range(exp):
        res*=a
    if b<0:
        return 1/res
    return res


print(power(2,3))
print(power(2,-3))

