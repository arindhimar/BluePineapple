def contains_sublist(main_list, sublist):
    n = len(main_list)
    m = len(sublist)

    if m==0:
        return True

    for i in range(n-m+1):
        if main_list[i:i+m] ==sublist:
            return True
    return False


main_list=[1,2,3,4,5,6]
sublist=[3,4,5]

print(contains_sublist(main_list, sublist)) 

