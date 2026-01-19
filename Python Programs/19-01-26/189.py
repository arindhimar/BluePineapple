def find_first_missing_positive_number(list_of_numbers):
    sorted_list_of_numbers = sorted(x for x in list_of_numbers if x > 0)

    expected = 1
    for num in sorted_list_of_numbers:
        if num == expected:
            expected += 1
        elif num > expected:
            return expected

    return expected
