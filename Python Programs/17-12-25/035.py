def find_rectangle_number(n):
    return n*(n+1)

n=int(input("Enter n"))

if n>=0:
    print(find_rectangle_number(n))