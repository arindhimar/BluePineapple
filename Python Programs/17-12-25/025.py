import math

def product_of_non_repeated(tempList):
    prod=[i for i in tempList if tempList.count(i)==1]
    print(math.prod(prod))

list_of_numbers=[1,2,3,4,5,2,6,8,7,5,1,7]
product_of_non_repeated(list_of_numbers)