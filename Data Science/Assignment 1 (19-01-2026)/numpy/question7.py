import numpy as np

def create_array():
    '''
    Create a 1D numpy array with 100 random float values
    '''
    array = np.random.rand(100)
    return array

def find_top_10_values(array):
    '''
    Find the top 10 values and their indices in the given numpy array
    '''
    # Get the indices of the top 10 values using argpartition
    top_10_indices = np.argpartition(array, -10)[-10:]
    # Get the top 10 values
    top_10_values = array[top_10_indices]
    # Sort the top 10 values and their indices
    sorted_indices = np.argsort(top_10_values)[::-1]
    top_10_values = top_10_values[sorted_indices]
    top_10_indices = top_10_indices[sorted_indices]
    return top_10_values, top_10_indices

generated_array = create_array()
top_10_values, top_10_indices = find_top_10_values(generated_array)
print("Original Array:", generated_array)

print("Top 10 Values:", top_10_values)
print("Indices of Top 10 Values:", top_10_indices)

print("Reversed Top 10 values:", top_10_values[::-1])
print("Reversed Top 10 indices:", top_10_indices[::-1])
