import numpy as np

def create_array():
    '''
    Create a 1D numpy array with values from 0 to 60
    '''
    #start , stop , step
    array = np.arange(1,61).reshape(5,12)
    return array


def row_wise_sum(array):
    '''
    Calculate the sum of each row in the given 2D numpy array
    '''
    # Sum along rows
    row_sums = array.sum(axis=1)
    return row_sums

def column_wise_sum(array):
    '''
    Calculate the sum of each column in the given 2D numpy array
    '''
    # Sum along columns
    column_sums = array.sum(axis=0)
    return column_sums


def global_std(array):
    '''
    Calculate the standard deviation of all elements in the given numpy array
    '''
    # Standard deviation of all elements
    std_dev = array.std()
    return std_dev

generated_array = create_array()
print("Original Array:\n", generated_array)
print("Row-wise Sum:", row_wise_sum(generated_array))
print("Column-wise Sum:", column_wise_sum(generated_array))
print("Global Standard Deviation:", global_std(generated_array))