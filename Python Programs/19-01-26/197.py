def perform_exponential_of_tuples(tuple1,tuple2):
    exponential = 1
    for i in range(len(tuple1)):
        exponential *= tuple1[i] ** tuple2[i]
    return exponential

tuple1 = (1, 2, 3)
tuple2 = (2, 3, 4)
print(perform_exponential_of_tuples(tuple1, tuple2))

    