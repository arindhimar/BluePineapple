def sort_mixed(tempList):
    num=sorted(i for i in tempList if isinstance(i, int))
    st=sorted(i for i in tempList if isinstance(i, str))
    
    print([num+st])
    
    
sort_mixed([3, "banana", 1, "apple", 10, "cherry", 2])