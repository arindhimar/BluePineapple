def arrange_negatives_before_positive(input_arr):
    negatives = [num for num in input_arr if num < 0]
    positives = [num for num in input_arr if num >= 0]
    return negatives + positives