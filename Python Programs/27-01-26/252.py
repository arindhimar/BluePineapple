import cmath

def complex_to_polar(complex_num):
    r, theta = cmath.polar(complex_num)
    return (r, theta)