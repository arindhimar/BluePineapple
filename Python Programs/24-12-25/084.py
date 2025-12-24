def newman_conway(n):
    if n <= 0:
        return None
    if n == 1 or n == 2:
        return 1

    p=[0]* (n + 1)
    p[1]=p[2] =1

    for i in range(3, n + 1):
        p[i]=p[p[i-1]]+p[i-p[i-1]]

    return p[n]

print(newman_conway(10))
