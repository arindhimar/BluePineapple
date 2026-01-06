#function to calulate summ of negative numvers usig lambda

def sum_of_negatives(numbers):
    negative_numbers = list(filter(lambda x: x < 0, numbers))
    return sum(negative_numbers)


numbers=[10,-5,3,-1,-7,2,8,-4]
print(sum_of_negatives(numbers))