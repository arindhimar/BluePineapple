def count_equilateral_triangles(n):
    if n < 1:
        return 0
    return (n * (n + 2) * (2 * n + 1)) // 8

