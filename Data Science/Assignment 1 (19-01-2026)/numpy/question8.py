import numpy as np


def create_array():
    '''
    Create a 1D array of length 40
    '''
    array = np.random.randint(0, 100, size=40)
    return array


def set_20_percent_to_nan_randomly(array):
    '''
    Set 20% of the elements in the array to NaN randomly
    '''
    total_elements = array.shape[0]
    num_elements_to_set = total_elements // 5  
    random_indices = np.random.choice(total_elements, size=num_elements_to_set, replace=False)
    array[random_indices] = np.nan
    return array

def mean_excluding_nan(array):
    '''
    Calculate the mean of the array excluding NaN values
    '''
    mean_value = np.nanmean(array)
    return mean_value

def fill_nan_with_median(array):
    '''
    Fill NaN values in the array with the median of the non-NaN elements
    '''
    median_value = np.nanmedian(array)
    array[np.isnan(array)] = median_value
    return array

generated_array = create_array()
print("Original Array:", generated_array)
array_with_nans = set_20_percent_to_nan_randomly(generated_array.copy())
print("Array after setting 20% elements to NaN:", array_with_nans)
print("Mean excluding NaN values:", mean_excluding_nan(array_with_nans))
filled_array = fill_nan_with_median(array_with_nans)
print("Array after filling NaN values with median:", filled_array)
