def count_substr_equal_to_len(tempStr):
    digits = [int(ch) for ch in tempStr]
    count = 0

    n = len(digits)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += digits[j]
            length = j - i + 1
            if curr_sum == length:
                count += 1

    print(count)

count_substr_equal_to_len("12332234")
