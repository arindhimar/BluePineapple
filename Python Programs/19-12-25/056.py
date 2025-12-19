def check_if_less_then_twice_reverse(n):
    strRev=str(n)[::-1]
    
    newNumebrStr=strRev*2
    newNumebr=int(newNumebrStr)-1
    
    if n<newNumebr: 
        return True 
    else: 
        return False
    


n=int(input("Enter value for n      "))
print(check_if_less_then_twice_reverse(n))