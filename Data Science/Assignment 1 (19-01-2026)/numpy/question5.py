import numpy as np

def create_matrices():
    '''
    Create two matrices A (3x4) and B (4x2) with random values
    '''
    A = np.random.rand(3, 4)
    B = np.random.rand(4, 2)
    return A, B

def matrix_multiplication(A, B):
    '''
    Compute the matrix multiplication of A and B
    '''
    return A @ B

def verify_transpose_property(A):
    '''
    Verify that (A.T).T equals A
    '''
    return np.array_equal((A.T).T, A)

def verify_identity_property(A):
    '''
    Create an identity matrix I and verify that A @ I equals A
    '''
    I = np.eye(A.shape[1]) 
    product = A @ I
    return np.array_equal(product, A)

A, B = create_matrices()
print("Matrix A:\n", A)
print("Matrix B:\n", B)
C = matrix_multiplication(A, B)
print("Matrix A @ B:\n", C)
print("Transpose Property Verified:", verify_transpose_property(A))
print("Identity Property Verified:", verify_identity_property(A))
