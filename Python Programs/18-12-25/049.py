def extract_first_one(matrix):
    return [i[0] for i in matrix if i]

data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(extract_first_one(data))