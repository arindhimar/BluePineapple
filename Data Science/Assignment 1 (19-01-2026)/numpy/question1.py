import numpy as np

def create_array():
    '''
    Create a 1D numpy array with values from 0 to 19
    '''
    #start , stop , step
    array = np.arange(20)
    return array

def reshape_array(array):
    '''
    Reshape the given 1D array into a 2D array with 5 rows and 4 columns
    '''
    # Reshape to 5 rows and 4 columns
    reshaped_array = array.reshape(5, 4)
    return reshaped_array

def dtype_info(array):
    '''
    Get the data type of the given numpy array
    '''
    # return data type of the array
    return array.dtype

def min_max_info(array):
    '''
    Get the minimum and maximum values of the given numpy array
    '''
    # return min and max values of the array
    return array.min(), array.max()

def sum_info(array):
    '''
    Get the sum of all elements in the given numpy array
    '''
    # return sum of all elements in the array
    return array.sum()

def mean_info(array):
    '''
    Get the mean of all elements in the given numpy array
    '''
    # return mean of all elements in the array
    return array.mean()

generated_array = create_array()
print("Original Array:", generated_array)
print(reshape_array(generated_array))
print("Data Type:", dtype_info(generated_array))
print("Min and Max:", min_max_info(generated_array))
print("Sum of Elements:", sum_info(generated_array))
print("Mean of Elements:", mean_info(generated_array))