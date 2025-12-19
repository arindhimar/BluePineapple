def check_if_diff_signs(n1,n2):
    
    if (n1<0 and n2>= 0) or (n1>=0 and n2 < 0):
        return "Yes diff signs" 
    else :
        return "No diff signs" 

print(check_if_diff_signs(14,-12))