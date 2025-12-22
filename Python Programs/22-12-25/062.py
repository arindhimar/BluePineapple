def find_smallest_number_in_the_list(tempList):
    return ''.join([str(i) for i in sorted(tempList)])


print(find_smallest_number_in_the_list([0,1,3,0,1,2,3,4,5]))