from collections import Counter

def check_digit_frequency(num):
    digit_count = Counter(str(num))
    for digit, count in digit_count.items():
        if count > int(digit):
            return False
    return True

print(check_digit_frequency(122333))  