def left_rotate_list(temp_list,n):
    if n < len(temp_list):
        return temp_list[ n : len(temp_list) + 1] + temp_list[ 0 : n ]


print(left_rotate_list([1,2,3,4,5],2))