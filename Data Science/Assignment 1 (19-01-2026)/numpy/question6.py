import numpy as np


def create_array():
    '''
    create a 1D numpy array with int values with 30 random values 
    '''
    array = np.random.randint(0, 100, size=30)
    return array

def select_random_elements(array):
    '''
    Select 8 random elements from the given numpy array and set them as 1
    '''
    random_indices = np.random.choice(array.shape[0], size=8, replace=False)
    random_elements = array[random_indices]
    array[random_indices] = 1
    return random_elements

def set_positions_divisible_by_five(array):
    '''
    Set positions divisible by 5 to 9 in the given numpy array
    '''
    array[::5] = 9
    return array


generated_array = create_array()
print("Original Array:", generated_array)
print("Randomly Selected Elements:", select_random_elements(generated_array))
print("Array after setting positions divisible by 5 to 9:", set_positions_divisible_by_five(generated_array))
