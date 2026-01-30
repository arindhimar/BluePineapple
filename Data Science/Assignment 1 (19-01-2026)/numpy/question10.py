import numpy as np

def create_array():
    '''
    Create a 1D array of length 365 representing daily sales
    '''
    array = np.random.randint(50, 500, size=365)
    return array


def seven_day_rolling_scheme()    