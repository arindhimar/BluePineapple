
def generate_3d_array(x, y, z):
    return [[['*' for _ in range(z)] for _ in range(y)] for _ in range(x)]

print(generate_3d_array(2, 3, 4))