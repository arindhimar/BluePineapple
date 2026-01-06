def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Magic square generation works only for odd numbers")

    magic = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2

    while num<= n*n:
        magic[i][j]=num
        num += 1

        new_i=(i-1)%n
        new_j=(j+1)%n

        if magic[new_i][new_j] != 0:
            i =(i+ 1) % n
        else:
            i,j=new_i,new_j

    return magic


n=int(input("Enter the size of the magic square (odd number): "))

magic_square=generate_magic_square(n)

for row in magic_square:
    print(row)
    