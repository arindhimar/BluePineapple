def find_vertex_of_parabolna(a,b,c):
    h=-b/(2 a)
    k=c-(b**2)/(4 * a)
    return (h, k)
    
    
    
a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))

vertex=find_vertex_of_parabolna(a,b,c)
print(vertex)