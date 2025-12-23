def check_if_tuple_is_div_by_k(tuple,k):
    for i in tuple:
        if i%k!=0:
            return False
        
    return True




tuples_list = [
    (5, 10, 15, 20),
    (21, 28, 35, 42),  
    (8, 12, 16, 24),
    (7, 14, 49, 56),   
    (9, 18, 27, 36)
]

for i in tuples_list:
    print(check_if_tuple_is_div_by_k(i,k=7))
    