from collections import Counter


def count_similar_occurrences(tuples_list):
    occurrence_count = Counter(tuples_list)
    # print(occurrence_count)
    count_of_similar_occurrences = Counter(occurrence_count.values())
    return dict(count_of_similar_occurrences)

print(count_similar_occurrences([(1, 2), (2, 3), (1, 2), (4, 5), (2, 3), (2, 3)]))