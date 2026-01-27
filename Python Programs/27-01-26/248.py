def harmonic_sum(n):
    s = 0.0
    for i in range(1, n + 1):
        s += 1 / i
    return s

print(harmonic_sum(5))