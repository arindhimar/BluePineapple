def is_keith_number(n):
    digits = list(map(int, str(n)))
    k = len(digits)
    seq = digits.copy()

    while True:
        next_term = sum(seq[-k:])
        if next_term == n:
            return True
        if next_term > n:
            return False
        seq.append(next_term)

n=int(input("Entetr n"))
print(is_keith_number(n))