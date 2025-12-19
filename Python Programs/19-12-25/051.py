def is_equilateral(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return "Invalid side"
    if a==b==c:
        return "Equi"
    else:
        return "Non equi"
    
print(is_equilateral(5,5,5))
