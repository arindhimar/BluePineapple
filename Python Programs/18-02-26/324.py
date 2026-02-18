def sum_alternate_tuples(lst):
    total=0
    for i in range(0, len(lst), 2):
        total += sum(lst[i])
    return total


tuples_list=[(1,2),(3,4),(5,6),(7,8)]
print(sum_alternate_tuples(tuples_list))
