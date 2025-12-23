def find_diff_bw_even_and_odd(n):
    es=0
    od=0 
    
    for i in str(abs(n)):  
        digit=int(i)  
        if digit % 2 == 0:
            es+= digit 
        else:
            od+=digit  
            
    return abs(es-od)  
