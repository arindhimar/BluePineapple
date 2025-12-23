def can_be_written(n):
    
    if (n%4==0) or not(n%4==2):
        return True
    
    
    
    return False


print(can_be_written(30))