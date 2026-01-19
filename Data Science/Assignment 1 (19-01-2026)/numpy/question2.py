import numpy as np

def create_array():
    '''
    Create a 1D numpy array with values randomly from 0 to 100 of length 50
    '''
    #start , stop , count
    array = np.random.randint(0, 101, size=50)
    return array

def extract_even_numbers(array):
    '''
    Extract even numbers from the given numpy array
    '''
    # Extract even numbers
    even_numbers = array[array % 2 == 0]
    return even_numbers


def extract_multiples_of_three(array):
    '''
    Extract multiples of 3 from the given numpy array
    '''
    # Extract multiples of 3
    multiples_of_three = array[(array % 3 == 0) & (array > 50)]
    return multiples_of_three

def replace_less_than_twenty(array):
    '''
    Replace all values less than 20 with 20 in the given numpy array
    '''
    # Replace values less than 20 with 20
    array[array < 20] = 20
    return array

generated_array = create_array()
print("Original Array:", generated_array)
print("Even Numbers:", extract_even_numbers(generated_array))
print("Multiples of Three greater than 50:", extract_multiples_of_three(generated_array))
print("Array after replacing values less than 20 with 20:", replace_less_than_twenty(generated_array))