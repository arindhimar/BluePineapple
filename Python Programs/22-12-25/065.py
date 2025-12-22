def sum_of_numbers(tempList):
    if not tempList:
        return 0
    return tempList[0] + sum_of_numbers(tempList[1:])

list_of_numbers = [47, 3, 88, 15, 62, 29, 94, 8, 56, 71]
result = sum_of_numbers(list_of_numbers)
print(result)
