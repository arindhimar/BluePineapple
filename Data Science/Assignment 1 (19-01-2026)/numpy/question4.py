import numpy as np

def create_and_normalize_matrix():
    '''
    Create a (4, 5) matrix of random floats and normalize each row to sum to 1
    '''
    # Create a (4, 5) matrix of random floats
    matrix = np.random.rand(4, 5)
    # print(matrix)
    
    # Create a (5,) vector
    vector = np.random.rand(5)
    # print(vector)
    
    # Add the vector to every row using broadcasting
    broadcasted_matrix = matrix + vector
    # print(broadcasted_matrix)
    
    # Normalize each row to sum to 1
    row_sums = broadcasted_matrix.sum(axis=1, keepdims=True)
    normalized_matrix = broadcasted_matrix / row_sums
    
    return normalized_matrix

normalized_result = create_and_normalize_matrix()
print("Normalized Matrix:\n", normalized_result)