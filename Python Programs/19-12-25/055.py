def find_nth_geometric(n,r,a):
    return a*r**(n-1)

n=int(input("Enter input for nth term"))
r=int(input("Enter input for r(cmn ratio)"))
a=int(input("Enter input for a(First term)"))

print(find_nth_geometric(n,r,a))