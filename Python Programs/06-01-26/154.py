def find_specified_elemetn_from_2d_list(matrix,n):
    for row in matrix:
        for col in row:
            if col == n:
                return (matrix.index(row), row.index(col))
    return None


